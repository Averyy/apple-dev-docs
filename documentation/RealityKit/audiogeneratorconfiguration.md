# AudioGeneratorConfiguration

**Framework**: RealityKit  
**Kind**: struct

A container for various settings for preparing and playing an AudioGeneratorController.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct AudioGeneratorConfiguration
```

## Topics

### Initializers
- [init(layoutTag: AudioChannelLayoutTag, mixGroupName: String?)](audiogeneratorconfiguration/init(layouttag:mixgroupname:).md)
### Instance Properties
- [var layoutTag: AudioChannelLayoutTag](audiogeneratorconfiguration/layouttag.md)
  The format in which the audio channels are specified.
- [var mixGroupName: String?](audiogeneratorconfiguration/mixgroupname.md)
  An arbitrary name that assigns an audio resource to an audio mix group.

## See Also

- [class AudioPlaybackController](audioplaybackcontroller.md)
  A controller that manages an audio playback instance.
- [class AudioGeneratorController](audiogeneratorcontroller.md)
  A controller that manages the playback of a real-time audio stream.
- [enum AudioEvents](audioevents.md)
  Events associated with audio playback.
- [struct PlayAudioAction](playaudioaction.md)
  An action which plays an audio resource on the given target entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audiogeneratorconfiguration)*