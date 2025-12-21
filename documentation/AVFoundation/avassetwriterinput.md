# AVAssetWriterInput

**Framework**: AVFoundation  
**Kind**: class

An object that appends media samples to a track in an asset writer’s output file.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetWriterInput
```

## Mentions

- [Tagging media with video color information](tagging-media-with-video-color-information.md)

#### Overview

Create an asset writer input to write a single track of media, and optional track-level metadata, to the output file. To write multiple concurrent tracks with ideal interleaving of media data, observe the value of the [`isReadyForMoreMediaData`](avassetwriterinput/isreadyformoremediadata.md) property of each input.

You can use an asset writer input to create tracks in a QuickTime movie file that aren’t self-contained, and instead reference sample data that exists in another file.

## Topics

### Creating an input
- [convenience init(mediaType: AVMediaType, outputSettings: [String : Any]?)](avassetwriterinput/init(mediatype:outputsettings:).md)
  Creates an input to append sample buffers of the specified type to the output file.
- [init(mediaType: AVMediaType, outputSettings: [String : Any]?, sourceFormatHint: CMFormatDescription?)](avassetwriterinput/init(mediatype:outputsettings:sourceformathint:).md)
  Creates an input that appends sample buffers of the specified type and format hint to the output file.
### Configuring presentation
- [var naturalSize: CGSize](avassetwriterinput/naturalsize.md)
  The natural display dimensions of the output’s visual media.
- [var transform: CGAffineTransform](avassetwriterinput/transform.md)
  The transform to use for display of the output’s visual media.
- [var preferredVolume: Float](avassetwriterinput/preferredvolume.md)
  The volume to prefer for playback of the output’s audio data.
- [var mediaTimeScale: CMTimeScale](avassetwriterinput/mediatimescale.md)
  The time scale of the track in the output file.
- [var marksOutputTrackAsEnabled: Bool](avassetwriterinput/marksoutputtrackasenabled.md)
  A Boolean value that indicates whether to enable a track in the output for playback and processing.
### Configuring language support
- [var languageCode: String?](avassetwriterinput/languagecode.md)
  The language code of the input’s track.
- [var extendedLanguageTag: String?](avassetwriterinput/extendedlanguagetag.md)
  The extended language for the input’s track.
### Configuring metadata
- [var metadata: [AVMetadataItem]](avassetwriterinput/metadata.md)
  The track-level metadata to write to the output.
### Configuring media data layout
- [var preferredMediaChunkAlignment: Int](avassetwriterinput/preferredmediachunkalignment.md)
  The boundary, in bytes, for aligning media chunks.
- [var preferredMediaChunkDuration: CMTime](avassetwriterinput/preferredmediachunkduration.md)
  The duration to use for each chunk of sample data in the output file.
- [var sampleReferenceBaseURL: URL?](avassetwriterinput/samplereferencebaseurl.md)
  The base URL sample references are relative to.
- [var mediaDataLocation: AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.property.md)
  Specifies how the input lays out and interleaves media data.
- [AVAssetWriterInput.MediaDataLocation](avassetwriterinput/mediadatalocation-swift.struct.md)
  A structure that indicates how to lay out and interleave media data.
### Configuring track associations
- [func canAddTrackAssociation(withTrackOf: AVAssetWriterInput, type: String) -> Bool](avassetwriterinput/canaddtrackassociation(withtrackof:type:).md)
  Determines whether it’s valid to associate another input’s track with this input’s track.
- [func addTrackAssociation(withTrackOf: AVAssetWriterInput, type: String)](avassetwriterinput/addtrackassociation(withtrackof:type:).md)
  Adds an association between input tracks.
### Appending media samples
- [var expectsMediaDataInRealTime: Bool](avassetwriterinput/expectsmediadatainrealtime.md)
  A Boolean value that indicates whether the input tailors its processing for real-time sources.
- [var isReadyForMoreMediaData: Bool](avassetwriterinput/isreadyformoremediadata.md)
  A Boolean value that indicates whether the input is ready to accept media data.
- [func requestMediaDataWhenReady(on: dispatch_queue_t, using: () -> Void)](avassetwriterinput/requestmediadatawhenready(on:using:).md)
  Tells the input to request media data, at its convenience, to write to the output file.
- [func append(CMSampleBuffer) -> Bool](avassetwriterinput/append(_:).md)
  Appends a sample buffer to an input to write to the output file.
- [func markAsFinished()](avassetwriterinput/markasfinished.md)
  Marks the input as finished to indicate that you’re done appending samples to it.
- [AVAssetWriterInput.SampleBufferReceiver](avassetwriterinput/samplebufferreceiver.md)
  Provides an interface for writing sample buffers to an input.
- [AVAssetWriterInput.PixelBufferReceiver](avassetwriterinput/pixelbufferreceiver.md)
  Provides an interface for writing pixel buffers to an input.
- [AVAssetWriterInput.TaggedPixelBufferGroupReceiver](avassetwriterinput/taggedpixelbuffergroupreceiver.md)
  Provides an interface for writing tagged pixel buffers to an input.
- [AVAssetWriterInput.MetadataReceiver](avassetwriterinput/metadatareceiver.md)
  Provides an interface for writing timed metadata groups to an input.
- [AVAssetWriterInput.CaptionReceiver](avassetwriterinput/captionreceiver.md)
  Provides an interface for writing caption data to an input.
### Performing multiple-pass encoding
- [var canPerformMultiplePasses: Bool](avassetwriterinput/canperformmultiplepasses.md)
  A Boolean value that indicates whether the input may perform multiple passes over appended media data.
- [var currentPassDescription: AVAssetWriterInputPassDescription?](avassetwriterinput/currentpassdescription.md)
  An object that describes the requirements for the current pass.
- [class AVAssetWriterInputPassDescription](avassetwriterinputpassdescription.md)
  An object that defines the interface to query for the requirements of the current pass.
- [func markCurrentPassAsFinished()](avassetwriterinput/markcurrentpassasfinished.md)
  Tells the input to analyze the appended media to determine whether it can improve the results by reencoding certain segments.
- [var performsMultiPassEncodingIfSupported: Bool](avassetwriterinput/performsmultipassencodingifsupported.md)
  A Boolean value that indicates whether the input attempts to encode the source media data using multiple passes.
- [func respondToEachPassDescription(on: dispatch_queue_t, using: () -> Void)](avassetwriterinput/respondtoeachpassdescription(on:using:).md)
  Tells the input to invoke a callback whenever it begins a new pass.
- [AVAssetWriterInput.MultiPassController](avassetwriterinput/multipasscontroller.md)
  Provides an interface to receive an async sequence of pass descriptions for the writer input receiver, if multi-pass is supported.
### Inspecting an input
- [var mediaType: AVMediaType](avassetwriterinput/mediatype.md)
  The media type of the samples that the input accepts.
- [var outputSettings: [String : Any]?](avassetwriterinput/outputsettings.md)
  The settings to use for encoding media data you append to the output.
- [var sourceFormatHint: CMFormatDescription?](avassetwriterinput/sourceformathint.md)
  A hint about the format of the sample buffers to append to the input.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Converting projected video to Apple Projected Media Profile](converting-projected-video-to-apple-projected-media-profile.md)
  Convert content with equirectangular or half-equirectangular projection to APMP.
- [Converting side-by-side 3D video to multiview HEVC and spatial video](converting-side-by-side-3d-video-to-multiview-hevc-and-spatial-video.md)
  Create video content for visionOS by converting an existing 3D HEVC file to a multiview HEVC format, optionally adding spatial metadata to create a spatial video.
- [Writing fragmented MPEG-4 files for HTTP Live Streaming](writing-fragmented-mpeg-4-files-for-http-live-streaming.md)
  Create an HTTP Live Streaming presentation by turning a movie file into a sequence of fragmented MPEG-4 files.
- [Creating spatial photos and videos with spatial metadata](../ImageIO/Creating-spatial-photos-and-videos-with-spatial-metadata.md)
  Add spatial metadata to stereo photos and videos to create spatial media for viewing on Apple Vision Pro.
- [Tagging media with video color information](tagging-media-with-video-color-information.md)
  Inspect and set video color space information when writing and transcoding media.
- [Evaluating an app’s video color](evaluating-an-app-s-video-color.md)
  Check color reproduction for a video in your app by using test patterns, video test equipment, and light-measurement instruments.
- [class AVOutputSettingsAssistant](avoutputsettingsassistant.md)
  An object that builds audio and video output settings dictionaries.
- [class AVAssetWriter](avassetwriter.md)
  An object that writes media data to a container file.
- [class AVAssetWriterInputPixelBufferAdaptor](avassetwriterinputpixelbufferadaptor.md)
  An object that appends video samples to an asset writer input.
- [class AVAssetWriterInputTaggedPixelBufferGroupAdaptor](avassetwriterinputtaggedpixelbuffergroupadaptor.md)
  An object that appends tagged buffer groups to an asset writer input.
- [class AVAssetWriterInputMetadataAdaptor](avassetwriterinputmetadataadaptor.md)
  An object that appends timed metadata groups to an asset writer input.
- [class AVAssetWriterInputGroup](avassetwriterinputgroup.md)
  A group of inputs with tracks that are mutually exclusive to each other for playback or processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinput)*