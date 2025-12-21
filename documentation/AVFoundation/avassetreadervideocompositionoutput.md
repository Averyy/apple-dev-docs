# AVAssetReaderVideoCompositionOutput

**Framework**: AVFoundation  
**Kind**: class

An object that reads composited video frames from one or more tracks of an asset.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetReaderVideoCompositionOutput
```

## Topics

### Creating a video composition output
- [init(videoTracks: [AVAssetTrack], videoSettings: [String : Any]?)](avassetreadervideocompositionoutput/init(videotracks:videosettings:).md)
  Creates an object that reads composited video frames from the specified video tracks.
### Configuring video settings
- [var videoComposition: AVVideoComposition?](avassetreadervideocompositionoutput/videocomposition.md)
  The video composition to use for the output.
- [var customVideoCompositor: (any AVVideoCompositing)?](avassetreadervideocompositionoutput/customvideocompositor.md)
  A custom video compositor for the output.
### Inspecting an output
- [var videoTracks: [AVAssetTrack]](avassetreadervideocompositionoutput/videotracks.md)
  The tracks from which the output reads the composited video.
- [var videoSettings: [String : Any]?](avassetreadervideocompositionoutput/videosettings.md)
  The video settings that the output uses.

## Relationships

### Inherits From
- [AVAssetReaderOutput](avassetreaderoutput.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Reading multiview 3D video files](reading-multiview-3d-video-files.md)
  Render single images for the left eye and right eye from a multiview High Efficiency Video Coding format file by reading individual video frames.
- [class AVAssetReader](avassetreader.md)
  An object that reads media data from an asset.
- [class AVAssetReaderOutput](avassetreaderoutput.md)
  An abstract class that defines the interface to read media samples from an asset reader.
- [class AVAssetReaderTrackOutput](avassetreadertrackoutput.md)
  An object that reads media data from a single track of an asset.
- [class AVAssetReaderAudioMixOutput](avassetreaderaudiomixoutput.md)
  An object that reads audio samples that result from mixing audio from one or more tracks.
- [class AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md)
  An object that reads sample references from an asset track.
- [class AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md)
  An object that creates timed metadata group objects for an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreadervideocompositionoutput)*