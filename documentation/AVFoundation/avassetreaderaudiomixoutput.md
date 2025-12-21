# AVAssetReaderAudioMixOutput

**Framework**: AVFoundation  
**Kind**: class

An object that reads audio samples that result from mixing audio from one or more tracks.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetReaderAudioMixOutput
```

#### Overview

Read audio data that you mix from one or more asset tracks by adding an audio mix output to an asset reader. You can read the samples in their stored format or you can convert them to an alternative format.

## Topics

### Creating an audio mix output
- [init(audioTracks: [AVAssetTrack], audioSettings: [String : Any]?)](avassetreaderaudiomixoutput/init(audiotracks:audiosettings:).md)
  Creates an object that reads mixed audio from the specified audio tracks.
### Configuring audio settings
- [var audioMix: AVAudioMix?](avassetreaderaudiomixoutput/audiomix.md)
  The audio mix to use with this output.
- [var audioTimePitchAlgorithm: AVAudioTimePitchAlgorithm](avassetreaderaudiomixoutput/audiotimepitchalgorithm.md)
  The processing algorithm to use for scaled audio edits.
### Inspecting an output
- [var audioTracks: [AVAssetTrack]](avassetreaderaudiomixoutput/audiotracks.md)
  The tracks from which the output reads audio.
- [var audioSettings: [String : Any]?](avassetreaderaudiomixoutput/audiosettings.md)
  The audio settings that the output uses.

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
- [class AVAssetReaderVideoCompositionOutput](avassetreadervideocompositionoutput.md)
  An object that reads composited video frames from one or more tracks of an asset.
- [class AVAssetReaderSampleReferenceOutput](avassetreadersamplereferenceoutput.md)
  An object that reads sample references from an asset track.
- [class AVAssetReaderOutputMetadataAdaptor](avassetreaderoutputmetadataadaptor.md)
  An object that creates timed metadata group objects for an asset track.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderaudiomixoutput)*