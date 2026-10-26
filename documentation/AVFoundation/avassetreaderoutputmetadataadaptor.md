# AVAssetReaderOutputMetadataAdaptor

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

An object that creates timed metadata group objects for an asset track.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetReader.outputMetadataProvider(for:) instead

## Declaration

```swift
class AVAssetReaderOutputMetadataAdaptor
```

```objc
@interface AVAssetReaderOutputMetadataAdaptor : NSObject
```

## Topics

### Creating a metadata adaptor
- [init(assetReaderTrackOutput: AVAssetReaderTrackOutput)](./avassetreaderoutputmetadataadaptor/init%28assetreadertrackoutput%29.md)
  Creates an object that reads timed metadata groups from an asset reader output.
- [+ assetReaderOutputMetadataAdaptorWithAssetReaderTrackOutput:](./avassetreaderoutputmetadataadaptor/assetreaderoutputmetadataadaptorwithassetreadertrackoutput_.md)
  Returns a new object that reads timed metadata groups from an asset reader output.
### Retrieving timed metadata groups
- [func nextTimedMetadataGroup() -> AVTimedMetadataGroup?](./avassetreaderoutputmetadataadaptor/nexttimedmetadatagroup%28%29.md)
  Returns the next timed metadata group for the asset reader output.
### Inspecting the track output
- [var assetReaderTrackOutput: AVAssetReaderTrackOutput](./avassetreaderoutputmetadataadaptor/assetreadertrackoutput.md)
  The asset reader track output that provides the timed metadata groups.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

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
- [class AVAssetReaderSampleReferenceOutput](./avassetreadersamplereferenceoutput.md)
  An object that reads sample references from an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor)*