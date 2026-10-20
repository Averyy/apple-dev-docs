# channelAudio

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

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

### Playing audio
- [func playAudio(AudioResource) -> AudioPlaybackController](./playaudio%28_%29.md)
  Prepares and plays a new audio playback instance on this entity.
- [func playAudio(configuration: AudioGeneratorConfiguration, Audio.GeneratorRenderHandler) throws -> AudioGeneratorController](./playaudio%28configuration,_%29.md)
  Prepares and plays a real-time audio playback instance.
- [func prepareAudio(configuration: AudioGeneratorConfiguration, Audio.GeneratorRenderHandler) throws -> AudioGeneratorController](./prepareaudio%28configuration,_%29.md)
  Prepares a real-time audio playback instances.
- [func prepareAudio(AudioResource) -> AudioPlaybackController](./prepareaudio%28_%29.md)
  Prepares an audio resource for playback.
- [func stopAllAudio()](./stopallaudio%28%29.md)
  Stops playback for all audio on this entity.
- [var spatialAudio: SpatialAudioComponent?](./spatialaudio.md)
  The component that configures the spatial rendering of sounds from this entity.
- [var ambientAudio: AmbientAudioComponent?](./ambientaudio.md)
  The component that configures the ambient rendering of sounds from this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/channelaudio)*