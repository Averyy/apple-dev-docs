# prepareAudio(configuration:_:)

**Framework**: RealityKit  
**Kind**: method

Prepares a real-time audio playback instances.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func prepareAudio(configuration: AudioGeneratorConfiguration = .init(), _ generatorRenderHandler: @escaping Audio.GeneratorRenderHandler) throws -> AudioGeneratorController
```

#### Return Value

An [`AudioGeneratorController`](audiogeneratorcontroller.md) instance that you use to manage audio playback. Use the controller to set the volume and start or stop playback.

#### Discussion

If you want to start playback immediately, use the [`playAudio(configuration:_:)`](entity/playaudio(configuration:_:).md) method instead.

> **Note**: See `Audio.GeneratorRenderHandler` for compliance with Swift 6 concurrency.

## Parameters

- `configuration`: A set of configuration parameters necessary for initializing and rendering the  .
- `generatorRenderHandler`: The audio render handler to prepare. The system runs this handler to generate real-time audio.

## See Also

- [func playAudio(AudioResource) -> AudioPlaybackController](entity/playaudio(_:).md)
  Prepares and plays a new audio playback instance on this entity.
- [func playAudio(configuration: AudioGeneratorConfiguration, Audio.GeneratorRenderHandler) throws -> AudioGeneratorController](entity/playaudio(configuration:_:).md)
  Prepares and plays a real-time audio playback instance.
- [func prepareAudio(AudioResource) -> AudioPlaybackController](entity/prepareaudio(_:).md)
  Prepares an audio resource for playback.
- [func stopAllAudio()](entity/stopallaudio.md)
  Stops playback for all audio on this entity.
- [var spatialAudio: SpatialAudioComponent?](entity/spatialaudio.md)
  The component that configures the spatial rendering of sounds from this entity.
- [var ambientAudio: AmbientAudioComponent?](entity/ambientaudio.md)
  The component that configures the ambient rendering of sounds from this entity.
- [var channelAudio: ChannelAudioComponent?](entity/channelaudio.md)
  The component that configures the channel-based rendering of sounds from this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/prepareaudio(configuration:_:))*