# AudioPlaybackController

**Framework**: RealityKit  
**Kind**: class

A controller that manages an audio playback instance.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class AudioPlaybackController
```

#### Overview

You can obtain an audio playback controller by calling an entity’s Entity/prepareAudio(:) method which creates a controller with the associated [`AudioResource`](audioresource.md). To play multiple instances of a resource, call [`playAudio(_:)`](entity/playaudio(_:).md) to obtain new AudioPlaybackControllers.

During playback, the audio appears to come from the entity that you used to create the controller. As you move around the MR scene, RealityKit modulates the characteristics of the audio to account for your location.

> **Note**: Playback commences only after the entity is parented and placed within a scene.

After playback completes, or if you call the [`stop()`](audioplaybackcontroller/stop().md) method, the audio resource resets, allowing you to replay the resource from the beginning. Alternatively, you can enable indefinite looping by setting the `loops` property of the audio resource to `true`.

Look for one of the events in [`AudioEvents`](audioevents.md) if you want to be alerted when certain aspects of audio playback occur.

## Topics

### Managing the resource
- [let resource: AudioResource](audioplaybackcontroller/resource.md)
  The resource that provides the audio stream.
### Setting the volume
- [var gain: AudioPlaybackController.Decibel](audioplaybackcontroller/gain.md)
  The individual gain in decibels of the audio playback controller output.
- [func fade(to: AudioPlaybackController.Decibel, duration: TimeInterval)](audioplaybackcontroller/fade(to:duration:).md)
  Transitions the gain to the given value over a time interval using a linear curve.
### Setting the speed
- [var speed: Double](audioplaybackcontroller/speed.md)
  The rate of playback of the audio resource, with a range of `[.25, 4]`
### Setting the reverb
- [var reverbSendLevel: AudioPlaybackController.Decibel](audioplaybackcontroller/reverbsendlevel.md)
  The send level from this playback controller to the reverb system.
### Starting and stopping audio playback
- [func play()](audioplaybackcontroller/play.md)
  Plays the audio resource.
- [func pause()](audioplaybackcontroller/pause.md)
  Pauses playback of the audio resource while maintaining the position in the audio stream.
- [func stop()](audioplaybackcontroller/stop.md)
  Stops playback of the audio resource and discards the location in the audio stream.
- [var isPlaying: Bool](audioplaybackcontroller/isplaying.md)
  A Boolean value that indicates whether playback is currently active.
### Handling completion
- [var completionHandler: (() -> Void)?](audioplaybackcontroller/completionhandler.md)
  A closure that the playback controller executes when it reaches the end of the audio stream.
### Finding the associated entity
- [var entity: Entity?](audioplaybackcontroller/entity.md)
  The entity from which the audio stream emanates.
### Instance Methods
- [func seek(to:)](audioplaybackcontroller/seek(to:).md)
  Sets the playback position to the specified time.
### Type Aliases
- [AudioPlaybackController.Decibel](audioplaybackcontroller/decibel-350si.md)
  A type alias for Double expressing that the value is in Decibels.
- [AudioPlaybackController.Decibel](audioplaybackcontroller/decibel-73aqn.md)
  A type alias for Double expressing that the value is in Decibels.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AudioGeneratorController](audiogeneratorcontroller.md)
  A controller that manages the playback of a real-time audio stream.
- [struct AudioGeneratorConfiguration](audiogeneratorconfiguration.md)
  A container for various settings for preparing and playing an AudioGeneratorController.
- [enum AudioEvents](audioevents.md)
  Events associated with audio playback.
- [struct PlayAudioAction](playaudioaction.md)
  An action which plays an audio resource on the given target entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackcontroller)*