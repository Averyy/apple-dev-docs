# AudioPlaybackGroupController

**Framework**: RealityKit  
**Kind**: class

A controller that manages synchronized playback for a group of audio resources.

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
@preconcurrency class AudioPlaybackGroupController
```

#### Overview

You obtain an audio playback group controller by calling [`prepareAudio(_:)`](audio/prepareaudio(_:).md) or [`playAudio(_:)`](audio/playaudio(_:).md) with multiple [`AudioResource`](audioresource.md)/[`Entity`](entity.md) pairs. The controller coordinates all sources so they remain synchronized through playback, pause, seek, and rate changes.

Each source plays from its associated entity, so RealityKit applies that entity’s spatial audio characteristics independently. The same entity may appear multiple times with different resources, and a single entity can participate in multiple groups simultaneously.

```swift
// Load multiple audio resources.
let drums = try AudioFileResource.load(named: "Drums")
let bass  = try AudioFileResource.load(named: "Bass")
let lead  = try AudioFileResource.load(named: "Lead")

// Pair each resource with the entity that should emit it.
let pairs: [(AudioResource, Entity)] = [
    (drums, drumsEntity),
    (bass,  bassEntity),
    (lead,  leadEntity),
]

// Prepare and start synchronized playback.
let controller = try Audio.playAudio(pairs)

// Adjust the whole group together.
controller.fade(to: -6, duration: 0.5)
```

> **Note**: Playback commences only after the entities are parented and placed within a scene.

Use [`play(at:)`](audioplaybackgroupcontroller/play(at:).md) to schedule a synchronized start at a future `AVAudioTime`, which is useful for aligning a group with other audio sources or external clocks.

To be notified when the group finishes playing, subscribe to [`AudioEvents.PlaybackGroupCompleted`](audioevents/playbackgroupcompleted.md) on the scene. The event fires once when playback reaches the end of the group’s audio stream.

## Topics

### Controlling playback
- [func play(at: AVAudioTime) throws](audioplaybackgroupcontroller/play(at:).md)
  Plays all audio resources in the group asynchronously at a specified time.
- [func seek(to: Duration)](audioplaybackgroupcontroller/seek(to:).md)
  Sets the playback position to the specified time.
### Accessing playback state
- [let resourcesAndEntities: [(AudioResource, Entity)]](audioplaybackgroupcontroller/resourcesandentities.md)
  The resource and entity tuples that comprise the playback group
### Instance Properties
- [var gain: Audio.Decibel](audioplaybackgroupcontroller/gain.md)
  The individual gain in decibels for all audio resources in the group.
- [var isPlaying: Bool](audioplaybackgroupcontroller/isplaying.md)
  A Boolean value that indicates whether playback is currently active.
- [var speed: Double](audioplaybackgroupcontroller/speed.md)
  The rate of playback for all audio resources in the group, with a range of `[.25, 4]`
### Instance Methods
- [func fade(to: Audio.Decibel, duration: TimeInterval)](audioplaybackgroupcontroller/fade(to:duration:).md)
  Transitions the gain to the given value over a time interval using a linear curve for all audio resources in the group.
- [func pause()](audioplaybackgroupcontroller/pause.md)
  Pauses playback of the audio resource while maintaining the position in the audio stream.
- [func play()](audioplaybackgroupcontroller/play.md)
  Plays the audio resource.
- [func stop()](audioplaybackgroupcontroller/stop.md)
  Stops playback of the audio resource and discards the location in the audio stream.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Identifiable](../swift/identifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class ReverbMeshResource](reverbmeshresource.md)
  A high-level representation of a collection of vertices and edges that define a shape used for simulating reverb.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/audioplaybackgroupcontroller)*