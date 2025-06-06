# prepareAudio(_:)

**Framework**: Realitykit  
**Kind**: method

Prepares an audio resource for playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func prepareAudio(_ resource: AudioResource) -> AudioPlaybackController
```

#### Return Value

An [`AudioPlaybackController`](audioplaybackcontroller.md) object that you can use to start and stop audio playback for this specific instance of a resource playing on this entity. You can also use this controller to update playback properties, such as gain and speed, during playback.

#### Discussion

To start playback right away with default `AudioPlaybackController` properties, use the [`playAudio(_:)`](entity/playaudio(_:).md) method instead.

> **Note**: As soon as the system prepares an audio resource, the audio engine begins tracking the position of the entity and allocates rendering resources, which incurs a power cost.

For optimal system resource usage, avoid preparing sounds before they are needed. For example:

```swift
let controller = entity.prepareAudio(anAudioResource)
controller.gain = -10 // Apply a custom gain, if desired.
controller.speed = 1.2 // Apply a custom speed, if desired.
controller.play()
```

## Parameters

- `resource`: The audio resource the method plays.   Load an audio resource from the file system with    ,   or from a URL with   .

## See Also

- [func playAudio(AudioResource) -> AudioPlaybackController](entity/playaudio(_:).md)
  Prepares and plays a new audio playback instance on this entity.
- [func playAudio(configuration: AudioGeneratorConfiguration, Audio.GeneratorRenderHandler) throws -> AudioGeneratorController](entity/playaudio(configuration:_:).md)
  Prepares and plays a real-time audio playback instance.
- [func prepareAudio(configuration: AudioGeneratorConfiguration, Audio.GeneratorRenderHandler) throws -> AudioGeneratorController](entity/prepareaudio(configuration:_:).md)
  Prepares a real-time audio playback instances.
- [func stopAllAudio()](entity/stopallaudio.md)
  Stops playback for all audio on this entity.
- [var spatialAudio: SpatialAudioComponent?](entity/spatialaudio.md)
  The component that configures the spatial rendering of sounds from this entity.
- [var ambientAudio: AmbientAudioComponent?](entity/ambientaudio.md)
  The component that configures the ambient rendering of sounds from this entity.
- [var channelAudio: ChannelAudioComponent?](entity/channelaudio.md)
  The component that configures the channel-based rendering of sounds from this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/prepareaudio(_:))*