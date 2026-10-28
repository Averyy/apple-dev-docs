# playAudio(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Prepares and plays a new audio playback instance on this entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func playAudio(_ resource: AudioResource) -> AudioPlaybackController
```

## Return Value

An [`AudioPlaybackController`](../audioplaybackcontroller.md) object that you can use to start and stop audio playback for this specific instance of a resource playing on this entity. You can also use this controller to update playback properties, such as gain and speed, during playback.

## Discussion

The method prepares the audio by calling [`prepareAudio(_:)`](./prepareaudio%28_%29.md), and then immediately calls the [`play()`](../audioplaybackcontroller/play%28%29.md) method of the controller that it returns. To begin multiple playback instances you can call `playAudio` multiple times.

## Parameters

- `resource`: The audio resource the method plays. Load an audio resource from the file system with [`init(named:in:configuration:)`](../audiofileresource/init%28named,in,configuration%29.md) , or from a URL with [`init(contentsOf:withName:configuration:)`](../audiofileresource/init%28contentsof,withname,configuration%29.md).

## See Also

### Playing audio
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
- [var channelAudio: ChannelAudioComponent?](./channelaudio.md)
  The component that configures the channel-based rendering of sounds from this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/playaudio(_:))*