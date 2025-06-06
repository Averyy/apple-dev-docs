# fixed(soundStageSize:)

**Framework**: AVFoundation  
**Kind**: method

Returns a fixed spatial experience configured for the specified sound stage size.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func fixed(soundStageSize: AVAudioSession.SoundStageSize) -> Self
```

#### Return Value

A new spatial experience.

## Parameters

- `soundStageSize`: The size of the sound stage.

## See Also

- [static func headTracked(soundStageSize: AVAudioSession.SoundStageSize, anchoringStrategy: AVAudioSession.AnchoringStrategy) -> Self](avaudiosessionspatialexperience/headtracked(soundstagesize:anchoringstrategy:).md)
  Returns a head-tracked spatial experience configured for the specified sound stage size and anchoring strategy.
- [AVAudioSession.SoundStageSize](../AVFAudio/AVAudioSession/SoundStageSize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](../AVFAudio/AVAudioSession/AnchoringStrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [static var bypassed: AVAudioSession.BypassedSpatialExperience](avaudiosessionspatialexperience/bypassed.md)
  A nonspatial experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiosessionspatialexperience/fixed(soundstagesize:))*