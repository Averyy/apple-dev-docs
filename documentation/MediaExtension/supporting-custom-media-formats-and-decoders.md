# Supporting custom media formats and decoders

**Framework**: MediaExtension

Extend the media formats the system can open by providing a format reader and a video decoder.

**Availability**:
- macOS 15.0+
- Xcode 16.0+

#### Overview

With the MediaExtension framework, you can add support for media formats macOS doesn’t handle on its own, using two kinds of app extension. A format reader turns a file the system doesn’t recognize into tracks that apps can play. A video decoder turns the compressed samples in those tracks into pixel buffers. Write a format reader when the system can’t parse your container, and a video decoder when it can’t decode your samples.

This sample builds a Mac app that plays and exports movies, and embeds one MediaExtension app extension of each kind in its bundle. It defines both formats so you can follow the whole path end to end. The `SimpleContainerReader` extension parses the Simple Container Format, whose files use the `simpl` filename extension, and the `RLEVideoDecoder` extension decodes `XRLE`, a run-length video codec. The app writes test movies in both formats: a `simpl` file needs both extensions, and an `XRLE` QuickTime movie needs only the decoder because AVFoundation already parses the QuickTime container.

#### Configure the Sample Code Project

Each extension declares a MediaExtension entitlement that a provisioning profile has to carry. Both, listed below, are public capabilities. Select the extension’s target, open the Signing & Capabilities tab, click the Add Capability button, and choose the capability that matches the extension:

- **Media Extension Format Reader**: Adds the `com.apple.developer.mediaextension.formatreader` entitlement. For more information, see [`Format reader entitlement`](format-reader-entitlement.md).
- **Media Extension Video Decoder**: Adds the `com.apple.developer.mediaextension.videodecoder` entitlement. For more information, see [`Video decoder entitlement`](video-decoder-entitlement.md).

The sample runs on macOS 15 or later. A wildcard App ID doesn’t carry entitlements, so automatic signing requires an explicit App ID for each extension. Substitute your own reverse-domain prefix for `com.example.apple-samplecode` throughout the project, and then register the following two explicit App IDs:

- An App ID for the format reader, with the Media Extension Format Reader capability
- An App ID for the video decoder, with the Media Extension Video Decoder capability

The host app declares no entitlements of its own, so you can build and run it without any additional setup. Publishing an app that embeds media extensions means registering an App ID for the app as well.

Keep each extension’s bundle identifier prefixed by the host app’s identifier, or the project doesn’t build. Set your team on all three targets, then build and run the host app. The system discovers the extensions from a signed build alone, whether Xcode runs the host app or it sits in `/Applications`, so you don’t need to archive and distribute.

> ❗ **Important**: Registering an extension doesn’t enable it. macOS installs both extensions in a disabled state, and the system can’t play the media until you enable them.

The first build that installs the extensions posts a system notification naming the app, and clicking that notification opens System Settings to the Media Extensions panel. To get there manually, follow these steps:

1. Open System Settings and go to General > Login Items & Extensions.
2. Find Media Extensions in the list and click the Info button.
3. Turn on MediaExtension Simple Container Format Reader and MediaExtension RLE Video Decoder.

The extensions stay on across restarts. To create media that needs them, drag a QuickTime or Simple Container Format movie onto the app’s window, click the Export button in the toolbar, and choose an output format in the save panel.

#### Declare the Container and Codec

An extension’s implementation code alone doesn’t make it reachable. The system learns which files and codecs an extension handles from an `EXAppExtensionAttributes` dictionary in the extension’s information property list, and it doesn’t load anything until that dictionary matches the media at hand.

The format reader’s dictionary names the factory class the system creates, the filename extensions to claim, and the uniform type identifier for the format, as shown here:

```xml
<key>EXAppExtensionAttributes</key>
<dict>
	<key>ClassImplementationID</key>
	<string>com.example.apple-samplecode.formatreader.SimpleContainer</string>
	<key>EXExtensionPointIdentifier</key>
	<string>com.apple.mediaextension.formatreader</string>
	<key>EXPrincipalClass</key>
	<string>ExtensionFormatReaderFactory</string>
	<key>MTFileNameExtensionArray</key>
	<array>
		<string>simpl</string>
	</array>
	<key>MTUTTypeArray</key>
	<array>
		<string>com.example.apple-samplecode.simpleformat</string>
	</array>
	<key>ObjectName</key>
	<string>MediaExtension Simple Container Format Reader</string>
</dict>
```

The format reader’s `Info.plist` also declares a `UTExportedTypeDeclarations` array, which exports the Simple Container Format type to the rest of the system so the Finder recognizes `simpl` files and other apps can open them. For a description of supporting keys, see [`Format reader property list dictionaries`](format-reader-property-list-dictionaries.md).

A decoder claims a codec rather than a container, so its dictionary carries a `CodecInfo` array instead of file types, like this:

```xml
<key>CodecInfo</key>
<array>
	<dict>
		<key>CodecName</key>
		<string>MediaExtension RLE Video Codec</string>
		<key>CodecType</key>
		<string>XRLE</string>
	</dict>
</array>
```

The `CodecType` value is the four-character code that identifies the codec in a video format description. The sample declares the same code a second time in `RLECodec.h`, as `kRLECodecCode`, for the decoder to compare against at instantiation, and the two declarations have to agree. For a description of supporting keys, see [`Video decoder property list dictionary`](video-decoder-property-list-dictionary.md).

#### Parse the Container

Media Toolbox creates a format reader when an app opens a file of a type the extension defines. The extension’s principal class, `ExtensionFormatReaderFactory`, conforms to [`MEFormatReaderExtension`](meformatreaderextension.md), and `formatReaderWithByteSource:options:error:` is its entry point. Media Toolbox creates an [`MEByteSource`](mebytesource.md) around the asset, which is how the extension reads the file’s bytes, and passes it to the method. The method returns an object that conforms to [`MEFormatReader`](meformatreader.md), as shown:

```objc
- (id<MEFormatReader>)formatReaderWithByteSource:(MEByteSource *)primaryByteSource
                                         options:(MEFormatReaderInstantiationOptions *)options
                                           error:(NSError **)error {
	id<MEFormatReader> formatReader;

	formatReader = [[ExtensionFormatReader alloc] initWithByteSource:primaryByteSource options:options error:error];
	return formatReader;
}
```

The `ExtensionFormatReader` protocol parses the container in its initializer rather than waiting for the system to ask for each piece. It retains the byte source and hands it to `SimpleContainerReader`, the class that knows the file layout, then builds the track readers, the file info, and the metadata in a single pass. A format reader has to retain the byte source it receives for as long as it’s active because an extension runs in a separate process from the app that plays the media.

The three `load` protocol methods the system calls afterward return values the initializer previously computed, which keeps each of them to one line. A format that streams, or one too large to parse up front, defers that work into those methods instead and calls each completion handler when the data arrives.

#### Describe the Tracks and the File

A format reader presents a container as a list of tracks. Then `setupTracks` asks `SimpleContainerReader` how many samples each media type holds, and creates one `ExtensionTrackReader` subclass for each type that has samples, like this:

```objc
- (void)setupTracks {
	BOOL hasVideo, hasAudio;
	ExtensionTrackReader *meTrack;

	hasVideo = ([m_reader sampleCountForMediaType:kCMMediaType_Video] > 0);
	hasAudio = ([m_reader sampleCountForMediaType:kCMMediaType_Audio] > 0);

	// Add the video track.
	if (hasVideo) {
		meTrack = [[ExtensionVideoTrackReader alloc] initWithMediaType:kCMMediaType_Video containerReader:m_reader];
		[m_tracks addObject:meTrack];
		meTrack = nil;
	}

	// Add the audio track.
	if (hasAudio) {
		meTrack = [[ExtensionAudioTrackReader alloc] initWithMediaType:kCMMediaType_Audio containerReader:m_reader];
		[m_tracks addObject:meTrack];
		meTrack = nil;
	}

	// Add a timecode track if the movie has video.
	if (hasVideo) {
		meTrack = [[ExtensionTimecodeTrackReader alloc] initWithMediaType:kCMMediaType_TimeCode containerReader:m_reader];
		[m_tracks addObject:meTrack];
		meTrack = nil;
	}
}
```

A file with both media types produces three tracks because the format reader synthesizes a timecode track whenever video is present. The `ExtensionTrackReader` class conforms to [`METrackReader`](metrackreader.md), and each subclass builds an [`METrackInfo`](metrackinfo.md) that describes its media type, track identifier, and format descriptions, then returns it from `loadTrackInfoWithCompletionHandler:`.

An [`MEFileInfo`](mefileinfo.md) object carries the properties a player needs before it can present the media, and duration is the one this format has to compute. The `setupFileInfo` method walks the track readers, totals the duration of each media type, and keeps the longer of video and audio, as shown here:

```objc
// Use the longer of the two durations as the total duration.
if (CMTIME_COMPARE_INLINE(videoDuration, >=, audioDuration)) {
	[m_fileInfo setDuration:videoDuration];
} else {
	[m_fileInfo setDuration:audioDuration];
}

[m_fileInfo setFragmentsStatus:MEFileInfoCouldNotContainFragments];
```

The format reader also reports that this format can’t contain fragments, which tells Media Toolbox not to look for samples appended after the file was written. It parses the format’s two metadata fields, a creation date and a name, into [`AVMutableMetadataItem`](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem) objects the same way, using the common metadata identifiers so that any AVFoundation client can read them.

#### Deliver Sample Data with Cursors

Tracks expose their samples through cursors. A cursor points at one sample, steps forward and backward in decode or presentation order, and delivers that sample’s data. The `ExtensionSampleCursor` class conforms to [`MESampleCursor`](mesamplecursor.md), and `ExtensionVideoSampleCursor`, `ExtensionAudioSampleCursor`, and `ExtensionTimecodeSampleCursor` subclass it, one for each track type. Every sample-data method in that protocol is optional because a cursor delivers data in one of two ways: it reports where the sample lives and lets Core Media read the bytes, or it reads the bytes itself and returns a sample buffer. Reporting the location is the better choice whenever the format allows it because Core Media can then coalesce adjacent reads into a single I/O request.

The video cursor reports locations. The `sampleLocationReturningError:` method looks up the offset and size of the sample at the cursor’s presentation time, and wraps them in an [`MESampleLocation`](mesamplelocation.md) together with the byte source to read from, like this:

```objc
- (MESampleLocation *)sampleLocationReturningError:(NSError **)error {
	int err;
	uint64_t offset, size;
	AVSampleCursorStorageRange storageRange;
	MESampleLocation *sampleLocation = nil;

	err = [m_reader getVideoSampleInfoAtTime:m_pts sampleOffset:&offset sampleSize:&size];
	if (err == noErr) {
		storageRange.offset = offset;
		storageRange.length = size;
		sampleLocation = [[MESampleLocation alloc] initWithByteSource:[m_reader byteSource] sampleLocation:storageRange];
	} else if (error != nil) {
		*error = [NSError errorWithDomain:MediaExtensionErrorDomain code:MEErrorLocationNotAvailable userInfo:nil];
	}

	return sampleLocation;
}
```

A cursor that reports locations implements either that method or the pair `estimatedSampleLocationReturningError:` and `refineSampleLocation:refinementData:refinementDataLength:refinedLocation:error:`, which exist for formats that read part of the file to work out where a sample begins. The video cursor implements the estimating method too, returning an [`MEEstimatedSampleLocation`](meestimatedsamplelocation.md) whose refinement range has zero length to report that its estimate is already exact.

The `chunkDetailsReturningError:` method describes how samples are grouped. Core Media calls it first to learn the grouping, then calls a location method to find an individual sample inside that group. Formats that store samples in contiguous runs need it, which is why the audio cursor treats each of the format’s audio sample groups as a chunk, as shown here:

```objc
// Determine the group info.
err = [m_reader getAudioSampleGroupInfoAtTime:m_pts groupOffset:&offset groupSize:&size indexInGroup:&indexInGroup];
if (err == noErr) {
	// Treat audio sample groups as chunks.
	// All are a uniform size except potentially the last one.
	chunkInfo.chunkSampleCount = size / [m_reader audioSampleSize];
	chunkInfo.chunkHasUniformSampleSizes = YES;
	chunkInfo.chunkHasUniformSampleDurations = YES;
	chunkInfo.chunkHasUniformFormatDescriptions = YES;
	// Set the storage range to point to the group.
	storageRange.offset = offset;
	storageRange.length = size;

	chunk = [[MESampleCursorChunk alloc] initWithByteSource:[m_reader byteSource]
	                                      chunkStorageRange:storageRange
	                                              chunkInfo:chunkInfo
	                                 sampleIndexWithinChunk:indexInGroup];
}
```

For formats that store samples individually, such as video, implementing `chunkDetailsReturningError:` is optional. The video cursor implements it anyway and reports the whole track as a single chunk.

The timecode cursor takes the other path because the Simple Container Format doesn’t store timecode samples at all. With no location to report, it synthesizes a sample from the video track’s first frame number and returns it in a `CMSampleBuffer` through `loadSampleBufferContainingSamplesToEndCursor:completionHandler:`, like this:

```objc
// Set the sample size to 32 bits and the duration to match the track duration.
bbufSize = sizeof(uint32_t);
timingInfo.duration = [m_reader sampleDurationForMediaType:m_mediaType];
timingInfo.presentationTimeStamp = m_pts;
timingInfo.decodeTimeStamp = kCMTimeInvalid;

// Store the timecode counter sample in big-endian format, matching the QuickTime
// file format specification.
*tcCounterPtr = CFSwapInt32HostToBig(firstFrameNumber);

err = CMSampleBufferCreate(NULL, tcCounterbbuf, true, NULL, NULL, tcFormatDescription,
                           1, 1, &timingInfo, 1, &bbufSize, &tcSampleBuf);
```

A cursor implements this method when it doesn’t implement `sampleLocationReturningError:`, and implements both when some of a format’s samples are contiguous and others aren’t. Returning buffers gives up the read coalescing that location reporting allows, so it suits samples the extension has to synthesize or unpack, as it does here.

#### Create the Video Decoder

Video Toolbox creates a decoder when it encounters a video format description whose codec type matches the `CodecType` the extension declares. The decoder’s principal class is `ExtensionRLEDecoderFactory`, which conforms to [`MEVideoDecoderExtension`](mevideodecoderextension.md), as shown here:

```objc
- (id<MEVideoDecoder>)videoDecoderWithCodecType:(CMVideoCodecType)codecType
                         videoFormatDescription:(CMVideoFormatDescriptionRef)videoFormatDescription
                     videoDecoderSpecifications:(NSDictionary<NSString *, id> *)videoDecoderSpecifications
             extensionDecoderPixelBufferManager:(MEVideoDecoderPixelBufferManager *)extensionDecoderPixelBufferManager
                                          error:(NSError **)error {
	id<MEVideoDecoder> videoDecoder;

	videoDecoder = [[ExtensionRLEDecoder alloc] initWithCodecType:codecType
	                                       videoFormatDescription:videoFormatDescription
	                                   videoDecoderSpecifications:videoDecoderSpecifications
	                           extensionDecoderPixelBufferManager:extensionDecoderPixelBufferManager
	                                                        error:error];
	return videoDecoder;
}
```

The factory receives an [`MEVideoDecoderPixelBufferManager`](mevideodecoderpixelbuffermanager.md), which is both how the decoder states the pixel buffers it wants and where it obtains them at decode time. The `ExtensionRLEDecoder` class checks the codec type against `kRLECodecCode` and returns `nil` if it doesn’t match because a mismatch means the system instantiated the extension for media it can’t handle. It then assigns the manager’s `pixelBufferAttributes` property the dictionary that `pixelBufferAttributesDictionary` builds, and creates the `RLEDecompressor` that does the pixel work, like this:

```objc
- (NSDictionary *)pixelBufferAttributesDictionary {
	NSMutableDictionary *attr;
	NSArray *pixFmtArray;

	attr = [NSMutableDictionary dictionary];

	// Under `kCVPixelBufferPixelFormatTypeKey`, add the list of source pixel formats.
	// This can be an `NSNumber` or an `NSArray` of `NSNumber` values.
	pixFmtArray = [NSArray arrayWithObjects:[NSNumber numberWithUnsignedInt:kCVPixelFormatType_422YpCbCr8], nil];
	[attr setObject:pixFmtArray forKey:(__bridge NSString *)kCVPixelBufferPixelFormatTypeKey];

	// Add `kCVPixelBufferWidthKey` and `kCVPixelBufferHeightKey` to specify the dimensions of
	// the source pixel buffers.
	// Normally this matches the compression target dimensions.
	[attr setObject:[NSNumber numberWithInt:m_dimensions.width] forKey:(__bridge NSString *)kCVPixelBufferWidthKey];
	[attr setObject:[NSNumber numberWithInt:m_dimensions.height] forKey:(__bridge NSString *)kCVPixelBufferHeightKey];

	// CoreVideo and Metal are most efficient with rows that are a multiple of 32 bytes.
	[attr setObject:[NSNumber numberWithInt:32] forKey:(__bridge NSString *)kCVPixelBufferBytesPerRowAlignmentKey];

	// Store an empty dictionary for `kCVPixelBufferIOSurfacePropertiesKey` to request
	// IOSurface-backed buffer allocation.
	[attr setObject:[NSDictionary dictionary] forKey:(__bridge NSString *)kCVPixelBufferIOSurfacePropertiesKey];

	// Request Metal compatibility.
	[attr setObject:[NSNumber numberWithBool:YES] forKey:(__bridge NSString *)kCVPixelBufferMetalCompatibilityKey];

	return attr;
}
```

The pixel format, width, and height keys are the ones every decoder sets. This decoder adds three that most codecs also want: a 32-byte row alignment because Core Video and Metal work most efficiently with rows that are a multiple of 32 bytes; an empty IOSurface properties dictionary, which requests IOSurface-backed buffers; and Metal compatibility. Codecs that need a border of extra pixels around each frame add the extended-pixel keys here too.

The `supportedPixelFormatsOrderedByQuality` method answers a different question, reporting the formats the decoder can output so the system can choose one. This decoder outputs a single format, and it decodes only at full size, so it returns an empty array from `pixelFormatsWithReducedResolutionDecodeSupport`, as shown here:

```objc
- (NSArray<NSNumber *> *)supportedPixelFormatsOrderedByQuality {
	// The decoder supports only '2vuy' (`kCVPixelFormatType_422YpCbCr8`).
	return [NSArray arrayWithObject:[NSNumber numberWithUnsignedInt:kCVPixelFormatType_422YpCbCr8]];
}

- (NSArray<NSNumber *> *)pixelFormatsWithReducedResolutionDecodeSupport {
	// This decoder doesn't support reduced-resolution decoding.
	return [NSArray array];
}
```

Reduced-resolution decoding, in which a decoder produces frames smaller than the media’s native size, is available through `setReducedResolution:` and `reducedResolution`. This decoder implements both to report full resolution and to log any request it can’t satisfy.

#### Decode Sample Buffers Into Frames

Decoding happens in `decodeFrameFromSampleBuffer:options:completionHandler:`. Video Toolbox hands the decoder one compressed sample buffer, and the decoder returns a `CVImageBuffer` through the completion handler, like this:

```objc
if (sampleBuffer != NULL && m_decoder != nil && ![options doNotOutputFrame]) {
	// Create the output pixel buffer.
	outputPixelBuffer = [m_pixelBufferManager createPixelBufferAndReturnError:&error];
	// Decode the frame.
	err = [m_decoder decodeFrame:sampleBuffer toBuffer:outputPixelBuffer];
	if (err == noErr) {
		// Add attachments to the buffer.
		fmtDesc = CMSampleBufferGetFormatDescription(sampleBuffer);
		[self addAttachmentsFromFormatDescription:fmtDesc toPixelBuffer:outputPixelBuffer];
	} else {
		// Indicate that an error occurred.
		error = [NSError errorWithDomain:MediaExtensionErrorDomain code:err userInfo:nil];
		status = MEDecodeFrameFrameDropped;
		if (outputPixelBuffer != NULL) {
			CFRelease(outputPixelBuffer);
		}
		outputPixelBuffer = NULL;
	}
}
```

The `addAttachmentsFromFormatDescription:toPixelBuffer:` method transfers the format description’s image extensions onto the output buffer, so that color primaries, transfer function, and matrix travel with the decoded frame. Without it, correctly decoded pixels display with the wrong color.

The [`MEDecodeFrameOptions`](medecodeframeoptions.md) parameter carries the system’s request for this frame, and this decoder acts on `doNotOutputFrame`, skipping the work for a frame the system needs decoded for reference but doesn’t intend to display. A failure reports a dropped-frame [`MEDecodeFrameStatus`](medecodeframestatus.md) and an error in the [`MediaExtensionErrorDomain`](mediaextensionerrordomain.md) domain. The decoder also reports whether it can take more data, like this:

```objc
- (BOOL)isReadyForMoreMediaData {
	return YES;
}
```

Frames in the `XRLE` format carry no interframe dependencies, which the decoder reports from `contentHasInterframeDependencies`, so this decoder is always ready and posts [`MEVideoDecoderReadyForMoreMediaDataDidChangeNotification`](mevideodecoderreadyformoremediadatadidchangenotification.md) after every frame. Building a new decode session for every change in the media isn’t efficient, so the system also asks whether the decoder can continue with the session it has, as shown here:

```objc
- (BOOL)canAcceptFormatDescription:(CMFormatDescriptionRef)formatDescription {
	CMVideoCodecType codec;
	CMVideoDimensions dim;

	codec = CMVideoFormatDescriptionGetCodecType(formatDescription);
	dim = CMVideoFormatDescriptionGetDimensions(formatDescription);

	// The decoder accepts a new format description as long as the codec and dimensions match.
	if (codec == kRLECodecCode && dim.width == m_dimensions.width && dim.height == m_dimensions.height) {
		return YES;
	} else {
		return NO;
	}
}
```

This decoder accepts a new description when the codec type and the dimensions both match the ones it was created with because its pixel buffer attributes and decompressor depend on those. Any other change means the system creates a new decoder instead.

#### Play Extension Backed Media

Media extensions are opt-in, so an app that wants to use them registers for them at launch. The `MovieModel` class makes both calls in a detached task it creates as it initializes:

```swift
// These calls opt the app into every media extension the system installed, so it can
// play any media those extensions support, not only the formats this sample provides.
private let registration = Task.detached {
    VTRegisterProfessionalVideoWorkflowVideoDecoders()
    MTRegisterProfessionalVideoWorkflowFormatReaders()
}
```

[`MTRegisterProfessionalVideoWorkflowFormatReaders()`](https://developer.apple.com/documentation/mediatoolbox/mtregisterprofessionalvideoworkflowformatreaders()) tells Media Toolbox that the app supports format reader extensions, and [`VTRegisterProfessionalVideoWorkflowVideoDecoders()`](https://developer.apple.com/documentation/videotoolbox/vtregisterprofessionalvideoworkflowvideodecoders()) tells Video Toolbox that it supports video decoder extensions. Both functions suit apps built around professional video workflows rather than network-facing apps such as browsers or mail clients. Both also cross XPC to enumerate the installed extensions, which blocks the calling thread long enough to stall a frame, so the model runs them off the main actor and the drop handler awaits `registration.value` before it hands a movie to the player. Extension-backed media doesn’t load until both calls return.

Apart from that wait, those two calls are the whole of the client-side work; the app plays movies with [`AVPlayer`](https://developer.apple.com/documentation/avfoundation/avplayer) afterward, and nothing else in it knows that the formats are custom.

Several system apps register already, which makes them a quick way to check an extension without writing a client. Selecting a test movie in the Finder and pressing the Space bar previews it in Quick Look, and QuickTime Player opens movies in both formats and names the custom codec in its movie inspector. The extensions run in their own processes that the system starts on demand, so playback doesn’t depend on the host app running.

#### Debug the Extensions

Because extensions run as separate processes, debugging one means attaching to a process the system starts on demand rather than launching a target:

1. Set a breakpoint in the extension’s source.
2. Choose Debug > Attach to Process by PID or Name, and enter `SimpleContainerReader` or `RLEVideoDecoder`.
3. Play a test movie in any app that registers for media extensions.

Xcode attaches as soon as the system loads the extension, and the process appears in the list only while it’s handling media. Logging often gets there faster, and both extensions log the unsupported requests and malformed files that otherwise fail silently, like this:

```objc
- (void)setReducedResolution:(CGSize)reducedResolution {
	NSLog(@"Reduced resolution decoding requested at %d x %d, not supported", (int)reducedResolution.width, (int)reducedResolution.height);
}
```

Recording in the Console app while playing a test movie, then filtering on the extension’s process name, shows those messages alongside the extension’s lifecycle events.

## See Also

- [protocol MEFormatReader](meformatreader.md)
  A protocol that defines the requirements for a format reader, which represents a single media asset.
- [protocol MEFormatReaderExtension](meformatreaderextension.md)
  A protocol that defines a factory to create a new format reader with a byte source.
- [class MEFormatReaderInstantiationOptions](meformatreaderinstantiationoptions.md)
  An object that contains options to pass to a format reader extension.
- [class MEFileInfo](mefileinfo.md)
  An object that contains file properties from the media asset.
- [Format reader property list dictionaries](format-reader-property-list-dictionaries.md)
  Include property list dictionaries to describe a format reader and register the formats it supports.
- [Format reader entitlement](format-reader-entitlement.md)
  Include an entitlement to indicate your extension is a MediaExtension format reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/supporting-custom-media-formats-and-decoders)*