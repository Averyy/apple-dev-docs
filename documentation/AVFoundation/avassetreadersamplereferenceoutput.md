# AVAssetReaderSampleReferenceOutput

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that reads sample references from an asset track.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetReaderSampleReferenceOutput
```

```objc
@interface AVAssetReaderSampleReferenceOutput : AVAssetReaderOutput
```

#### Overview

Apps can extract information about the location of samples in a track — the file URL and offset — by adding an instance of this class to an asset reader. Read the [`kCMSampleBufferAttachmentKey_SampleReferenceURL`](../CoreMedia/kcmsamplebufferattachmentkey_samplereferenceurl.md) and [`kCMSampleBufferAttachmentKey_SampleReferenceByteOffset`](../CoreMedia/kcmsamplebufferattachmentkey_samplereferencebyteoffset.md) attachments on the extracted sample buffers to get the location of the sample data.

You can also append sample buffers that you extract using this class to an [`AVAssetWriterInput`](./avassetwriterinput.md) instance to create movie tracks that aren’t self-contained and reference data in the original file instead. To write tracks that aren’t self-contained, use instances of [`AVAssetWriter`](./avassetwriter.md) that you configure to write files of type [`mov`](./avfiletype/mov.md).

Because this output doesn’t return sample data, it ignores the value of the [`alwaysCopiesSampleData`](./avassetreaderoutput/alwayscopiessampledata.md) property.

## Topics

### Creating a sample reference output
- [init(track: AVAssetTrack)](./avassetreadersamplereferenceoutput/init%28track%29.md)
  Creates an object that supplies sample references.
- [+ assetReaderSampleReferenceOutputWithTrack:](./avassetreadersamplereferenceoutput/assetreadersamplereferenceoutputwithtrack_.md)
  Returns a new object that supplies sample references.
### Inspecting the track
- [var track: AVAssetTrack](./avassetreadersamplereferenceoutput/track.md)
  The track from which the output reads sample references.

## Relationships

### Inherits From
- [AVAssetReaderOutput](./avassetreaderoutput.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Media reading
- [Reading multiview 3D video files](./reading-multiview-3d-video-files.md)
  Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [class AVAssetReader](./avassetreader.md)
  An object that reads media data from an asset.
- [class AVAssetReaderOutput](./avassetreaderoutput.md)
  An abstract class that defines the interface to read media samples from an asset reader.
- [class AVAssetReaderTrackOutput](./avassetreadertrackoutput.md)
  An object that reads media data from a single track of an asset.
- [class AVAssetReaderAudioMixOutput](./avassetreaderaudiomixoutput.md)
  An object that reads audio samples that result from mixing audio from one or more tracks.
- [class AVAssetReaderVideoCompositionOutput](./avassetreadervideocompositionoutput.md)
  An object that reads composited video frames from one or more tracks of an asset.
- [class AVAssetReaderOutputMetadataAdaptor](./avassetreaderoutputmetadataadaptor.md)
  An object that creates timed metadata group objects for an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadersamplereferenceoutput)*