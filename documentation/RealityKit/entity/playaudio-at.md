# playAudio(_:at:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously prepares and plays a new audio playback instance at a specified time on this entity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func playAudio(_ resource: AudioResource, at time: AVAudioTime) throws -> AudioPlaybackController
```

#### Return Value

An `AudioPlaybackController` object that you can use to start and stop audio playback for this specific instance of a resource playing on this entity. You can also use this controller to update playback properties, such as gain and speed, during playback.

#### Discussion

Use this method to schedule playback of a sound source to a precise time in the future. This method enables sample-accurate timing for individual sounds and synchronization of multiple audio sources. The method prepares the audio by calling `prepareAudio(_:)`, and then immediately calls the `play(at: time)` method of the controller that it returns. Any call to play() will cancel pending scheduled time and play audio immediately, while any call to `playAudio(at: time)` will cancel current scheduled time and schedule for new time.

Audio preparation must complete before the scheduled playback time to maintain precise timing. If preparation is still in progress when the scheduled time arrives, or if the scheduled time is in the past, playback starts immediately, which may result in timing drift. For accurate synchronization, schedule a time sufficiently far in the future.

The returned controller’s `isPlaying` property becomes `true` immediately after calling `playAudio(at: time)`. This ensures that checking the `isPlaying` property immediately returns the correct state for subsequent operations, such as deciding whether to play the audio again.

For synchronizing multiple sounds, use the same base time for all scheduled playback calls.

## Parameters

- `resource`: The audio resource the method plays. Load an audio resource from the file system with `init(named:in:configuration:)`, or from a URL with `init(contentsOf:withName:configuration:)`.
- `time`: The AVAudioTime when the audio file should start playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/playaudio(_:at:))*