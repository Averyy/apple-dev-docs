# channelAudio

**Framework**: RealityKit  
**Kind**: property

The component that configures the channel-based rendering of sounds from this entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var channelAudio: ChannelAudioComponent? { get set }
```

## See Also

- [func playAudio(AudioResource) -> AudioPlaybackController](entity/playaudio(_:).md)
  Prepares and plays a new audio playback instance on this entity.
- [func playAudio(configuration: AudioGeneratorConfiguration, Audio.GeneratorRenderHandler) throws -> AudioGeneratorController](entity/playaudio(configuration:_:).md)
  Prepares and plays a real-time audio playback instance.
- [func prepareAudio(configuration: AudioGeneratorConfiguration, Audio.GeneratorRenderHandler) throws -> AudioGeneratorController](entity/prepareaudio(configuration:_:).md)
  Prepares a real-time audio playback instances.
- [func prepareAudio(AudioResource) -> AudioPlaybackController](entity/prepareaudio(_:).md)
  Prepares an audio resource for playback.
- [func stopAllAudio()](entity/stopallaudio.md)
  Stops playback for all audio on this entity.
- [var spatialAudio: SpatialAudioComponent?](entity/spatialaudio.md)
  The component that configures the spatial rendering of sounds from this entity.
- [var ambientAudio: AmbientAudioComponent?](entity/ambientaudio.md)
  The component that configures the ambient rendering of sounds from this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/channelaudio)*