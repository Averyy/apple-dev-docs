# AnimationPlaybackController

**Framework**: RealityKit  
**Kind**: class

A controller that manages animation playback.

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
@preconcurrency class AnimationPlaybackController
```

#### Overview

This class controls the playback of an entity animation by providing its pause, resume, or stop functions.

The animation starts immediately after you call [`playAnimation(_:transitionDuration:startsPaused:)`](entity/playanimation(_:transitionduration:startspaused:).md), or `Entity/move(to:relativeTo:duration:timingFunction:)-905k`, which both return an instance of this class.

A controller invalidates after its associated animation completes or stops. To play another animation, perform an action that generates another controller.

While an animation plays, you can receive notification of particular playback states by subscribing to an event. For more information, see [`AnimationEvents`](animationevents.md).

## Topics

### Inspecting and controlling playback
- [func pause()](animationplaybackcontroller/pause.md)
  Pauses the animation.
- [func resume()](animationplaybackcontroller/resume.md)
  Resumes a paused animation.
- [func stop()](animationplaybackcontroller/stop.md)
  Stops an animation.
### Managing completion
- [var isComplete: Bool](animationplaybackcontroller/iscomplete.md)
  A Boolean that indicates whether the animation has finished running.
- [var isPaused: Bool](animationplaybackcontroller/ispaused.md)
  A Boolean that indicates whether the animation is paused.
### Accessing the associated entity
- [var entity: Entity?](animationplaybackcontroller/entity.md)
  The entity to which the animation applies.
### Comparing animation playback controllers
- [static func == (AnimationPlaybackController, AnimationPlaybackController) -> Bool](animationplaybackcontroller/==(_:_:).md)
  Indicates whether two animation playback controllers are equal.
- [func hash(into: inout Hasher)](animationplaybackcontroller/hash(into:).md)
  Hashes the essential components of the controller by feeding them into the given hash function.
### Instance Properties
- [var blendFactor: Float](animationplaybackcontroller/blendfactor-5hhc0.md)
  The level of influence the controller gives to its animation.
- [var blendFactor: Float](animationplaybackcontroller/blendfactor-8b8jq.md)
  The level of influence the controller gives to its animation.
- [var clock: CMClockOrTimebase](animationplaybackcontroller/clock-31p38.md)
  A reference clock to synchronize the animation with other events.
- [var clock: CMClockOrTimebase](animationplaybackcontroller/clock-42emj.md)
  A reference clock to synchronize the animation with other events.
- [var duration: TimeInterval](animationplaybackcontroller/duration-33vtf.md)
  The length of time the animation spans, in seconds.
- [var duration: TimeInterval](animationplaybackcontroller/duration-4qtfh.md)
  The length of time the animation spans, in seconds.
- [var isPlaying: Bool](animationplaybackcontroller/isplaying-2n2l0.md)
  A Boolean value that indicates whether the animation plays.
- [var isPlaying: Bool](animationplaybackcontroller/isplaying-72uh9.md)
  A Boolean value that indicates whether the animation plays.
- [var isStopped: Bool](animationplaybackcontroller/isstopped-1jnnw.md)
  A Boolean value that indicates whether the animation stopped.
- [var isStopped: Bool](animationplaybackcontroller/isstopped-4ltj3.md)
  A Boolean value that indicates whether the animation stopped.
- [var isValid: Bool](animationplaybackcontroller/isvalid-8rn7d.md)
  A Boolean value that indicates whether the animation controller is functional.
- [var isValid: Bool](animationplaybackcontroller/isvalid-9tk2f.md)
  A Boolean value that indicates whether the animation controller is functional.
- [var speed: Float](animationplaybackcontroller/speed-1qldh.md)
  The animation’s rate of playback.
- [var speed: Float](animationplaybackcontroller/speed-4qhq5.md)
  The animation’s rate of playback.
- [var time: TimeInterval](animationplaybackcontroller/time-1ooz1.md)
  The animation’s location within the timeline.
- [var time: TimeInterval](animationplaybackcontroller/time-6vpzm.md)
  The animation’s location within the timeline.
### Instance Methods
- [func stop(blendOutDuration:)](animationplaybackcontroller/stop(blendoutduration:).md)
  Stops an animation with a fade-out time.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AnimationResource](animationresource.md)
  An animation for the properties of scenes or entities.
- [struct AnimationLibraryComponent](animationlibrarycomponent.md)
  A component that represents a collection of animations that an entity can play.
- [AnimationLibraryComponent.AnimationCollection](animationlibrarycomponent/animationcollection.md)
  A collection of animations an entity can play.
- [enum AnimationEvents](animationevents.md)
  Notable milestones that the framework signals during animation playback.
- [enum AnimationRepeatMode](animationrepeatmode.md)
  Options that determine whether an animation replays after completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller)*