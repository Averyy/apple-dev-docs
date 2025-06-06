# AVAssetReaderOutput

**Framework**: AVFoundation  
**Kind**: class

An abstract class that defines the interface to read media samples from an asset reader.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetReaderOutput
```

## Mentions

- [Tagging Media with Video Color Information](tagging-media-with-video-color-information.md)

#### Overview

You add concrete output instances, such as [`AVAssetReaderTrackOutput`](avassetreadertrackoutput.md) or [`AVAssetReaderVideoCompositionOutput`](avassetreadervideocompositionoutput.md), to an asset reader to perform specific tasks.

> ❗ **Important**:  If you don’t require modifying sample data in-place, set the value of the [`alwaysCopiesSampleData`](avassetreaderoutput/alwayscopiessampledata.md) property to [`false`](https://developer.apple.com/documentation/swift/false) to prevent the output from making unnecessary copies.

 If you don’t require modifying sample data in-place, set the value of the [`alwaysCopiesSampleData`](avassetreaderoutput/alwayscopiessampledata.md) property to [`false`](https://developer.apple.com/documentation/swift/false) to prevent the output from making unnecessary copies.

## Topics

### Configuring Reading
- [var alwaysCopiesSampleData: Bool](avassetreaderoutput/alwayscopiessampledata.md)
  A Boolean value that indicates whether the output vends copied sample data.
- [var supportsRandomAccess: Bool](avassetreaderoutput/supportsrandomaccess.md)
  A Boolean value that indicates whether the output supports reconfiguring the time ranges it reads.
- [func reset(forReadingTimeRanges: [NSValue])](avassetreaderoutput/reset(forreadingtimeranges:).md)
  Restarts reading with a new set of time ranges.
- [func markConfigurationAsFinal()](avassetreaderoutput/markconfigurationasfinal.md)
  Tells the output that it’s finished reconfiguring time ranges, and allows the asset reader to advance to a completed state.
### Copying Sample Buffers
- [func copyNextSampleBuffer() -> CMSampleBuffer?](avassetreaderoutput/copynextsamplebuffer.md)
  Copies the next sample buffer from the output.
### Inspecting the Media Type
- [var mediaType: AVMediaType](avassetreaderoutput/mediatype.md)
  The media type of samples that the output reads.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md)
- [AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md)
- [AVAssetReaderTrackOutput](avassetreadertrackoutput.md)
- [AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md)
  Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [class AVAssetReader](avassetreader.md)
  An object that reads media data from an asset.
- [class AVAssetReaderTrackOutput](avassetreadertrackoutput.md)
  An object that reads media data from a single track of an asset.
- [class AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md)
  An object that reads audio samples that result from mixing audio from one or more tracks.
- [class AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md)
  An object that reads composited video frames from one or more tracks of an asset.
- [class AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md)
  An object that reads sample references from an asset track.
- [class AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md)
  An object that creates timed metadata group objects for an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutput)*