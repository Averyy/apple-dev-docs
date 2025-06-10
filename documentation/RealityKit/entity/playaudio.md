# playAudio(_:)

**Framework**: RealityKit  
**Kind**: method

Prepares and plays a new audio playback instance on this entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func playAudio(_ resource: AudioResource) -> AudioPlaybackController
```

#### Return Value

An [`AudioPlaybackController`](audioplaybackcontroller.md) object that you can use to start and stop audio playback for this specific instance of a resource playing on this entity. You can also use this controller to update playback properties, such as gain and speed, during playback.

#### Discussion

The method prepares the audio by calling [`prepareAudio(_:)`](entity/prepareaudio(_:).md), and then immediately calls the [`play()`](audioplaybackcontroller/play().md) method of the controller that it returns. To begin multiple playback instances you can call `playAudio` multiple times.

## Parameters

- `resource`: The audio resource the method plays.   Load an audio resource from the file system with    ,   or from a URL with   .

## See Also

- [func playAudio(configuration:_:)](entity/playaudio(configuration:_:).md)
  Prepares and plays a real-time audio playback instance.
- [func prepareAudio(configuration:_:)](entity/prepareaudio(configuration:_:).md)
  Prepares a real-time audio playback instances.
- [func prepareAudio(AudioResource) -> AudioPlaybackController](entity/prepareaudio(_:).md)
  Prepares an audio resource for playback.
- [func stopAllAudio()](entity/stopallaudio.md)
  Stops playback for all audio on this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/playaudio(_:))*