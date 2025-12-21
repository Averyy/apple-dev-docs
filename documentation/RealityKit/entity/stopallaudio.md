# stopAllAudio()

**Framework**: RealityKit  
**Kind**: method

Stops playback for all audio on this entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func stopAllAudio()
```

#### Discussion

You can stop a specific [`AudioPlaybackController`](audioplaybackcontroller.md) instance from playing a particular resource by calling the controller’s [`stop()`](audioplaybackcontroller/stop().md) method.

## See Also

- [func playAudio(AudioResource) -> AudioPlaybackController](entity/playaudio(_:).md)
  Prepares and plays a new audio playback instance on this entity.
- [func playAudio(configuration: AudioGeneratorConfiguration, Audio.GeneratorRenderHandler) throws -> AudioGeneratorController](entity/playaudio(configuration:_:).md)
  Prepares and plays a real-time audio playback instance.
- [func prepareAudio(configuration: AudioGeneratorConfiguration, Audio.GeneratorRenderHandler) throws -> AudioGeneratorController](entity/prepareaudio(configuration:_:).md)
  Prepares a real-time audio playback instances.
- [func prepareAudio(AudioResource) -> AudioPlaybackController](entity/prepareaudio(_:).md)
  Prepares an audio resource for playback.
- [var spatialAudio: SpatialAudioComponent?](entity/spatialaudio.md)
  The component that configures the spatial rendering of sounds from this entity.
- [var ambientAudio: AmbientAudioComponent?](entity/ambientaudio.md)
  The component that configures the ambient rendering of sounds from this entity.
- [var channelAudio: ChannelAudioComponent?](entity/channelaudio.md)
  The component that configures the channel-based rendering of sounds from this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/stopallaudio())*