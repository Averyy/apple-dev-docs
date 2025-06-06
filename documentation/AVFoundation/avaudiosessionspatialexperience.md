# AVAudioSessionSpatialExperience

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines types of spatial audio experiences that the system supports.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
protocol AVAudioSessionSpatialExperience
```

## Topics

### Specifying the experience
- [static func fixed(soundStageSize: AVAudioSession.SoundStageSize) -> Self](avaudiosessionspatialexperience/fixed(soundstagesize:).md)
  Returns a fixed spatial experience configured for the specified sound stage size.
- [static func headTracked(soundStageSize: AVAudioSession.SoundStageSize, anchoringStrategy: AVAudioSession.AnchoringStrategy) -> Self](avaudiosessionspatialexperience/headtracked(soundstagesize:anchoringstrategy:).md)
  Returns a head-tracked spatial experience configured for the specified sound stage size and anchoring strategy.
- [AVAudioSession.SoundStageSize](../AVFAudio/AVAudioSession/SoundStageSize.md)
  Constants that specify the perceived size of sounds the audio session plays.
- [AVAudioSession.AnchoringStrategy](../AVFAudio/AVAudioSession/AnchoringStrategy.md)
  Constants that specify how to set the origin of audio in a head-tracked spatial experience.
- [static var bypassed: AVAudioSession.BypassedSpatialExperience](avaudiosessionspatialexperience/bypassed.md)
  A nonspatial experience.

## See Also

- [Handling audio interruptions](../AVFAudio/handling-audio-interruptions.md)
  Observe audio session notifications to ensure that your app responds appropriately to interruptions.
- [Responding to audio route changes](../AVFAudio/responding-to-audio-route-changes.md)
  Observe audio session notifications to ensure that your app responds appropriately to route changes.
- [Capturing stereo audio from built-In microphones](../AVFAudio/capturing-stereo-audio-from-built-in-microphones.md)
  Configure an iOS device’s built-in microphones to add stereo recording capabilities to your app.
- [class AVAudioSession](../AVFAudio/AVAudioSession.md)
  An object that communicates to the system how you intend to use audio in your app.
- [class AVAudioApplication](../AVFAudio/AVAudioApplication.md)
  An object that manages one or more audio sessions that belong to an app.
- [class AVAudioRoutingArbiter](../AVFAudio/AVAudioRoutingArbiter.md)
  An object for configuring macOS apps to participate in AirPods Automatic Switching.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiosessionspatialexperience)*