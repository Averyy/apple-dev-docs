# AnimationPlaybackController

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A controller that manages animation playback.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency class AnimationPlaybackController
```

#### Overview

This class controls the playback of an entity animation by providing its pause, resume, or stop functions.

The animation starts immediately after you call [`playAnimation(_:transitionDuration:startsPaused:)`](./entity/playanimation%28_,transitionduration,startspaused%29.md), or `Entity/move(to:relativeTo:duration:timingFunction:)-905k`, which both return an instance of this class.

A controller invalidates after its associated animation completes or stops. To play another animation, perform an action that generates another controller.

While an animation plays, you can receive notification of particular playback states by subscribing to an event. For more information, see [`AnimationEvents`](./animationevents.md).

## Topics

### Inspecting and controlling playback
- [func pause()](./animationplaybackcontroller/pause%28%29.md)
  Pauses the animation.
- [func resume()](./animationplaybackcontroller/resume%28%29.md)
  Resumes a paused animation.
- [func stop()](./animationplaybackcontroller/stop%28%29.md)
  Stops an animation.
- [var isPlaying: Bool](./animationplaybackcontroller/isplaying.md)
  A Boolean value that indicates whether the animation plays.
- [var isStopped: Bool](./animationplaybackcontroller/isstopped.md)
  A Boolean value that indicates whether the animation stopped.
- [var isValid: Bool](./animationplaybackcontroller/isvalid.md)
  A Boolean value that indicates whether the animation controller is functional.
- [var blendFactor: Float](./animationplaybackcontroller/blendfactor.md)
  The level of influence the controller gives to its animation.
### Managing completion
- [var isComplete: Bool](./animationplaybackcontroller/iscomplete.md)
  A Boolean that indicates whether the animation has finished running.
- [var isPaused: Bool](./animationplaybackcontroller/ispaused.md)
  A Boolean that indicates whether the animation is paused.
### Accessing the associated entity
- [var entity: Entity?](./animationplaybackcontroller/entity.md)
  The entity to which the animation applies.
### Timing animation playback
- [var duration: TimeInterval](./animationplaybackcontroller/duration.md)
  The length of time the animation spans, in seconds.
- [var speed: Float](./animationplaybackcontroller/speed.md)
  The animation’s rate of playback.
- [var clock: CMClockOrTimebase](./animationplaybackcontroller/clock.md)
  A reference clock to synchronize the animation with other events.
- [var time: TimeInterval](./animationplaybackcontroller/time.md)
  The animation’s location within the timeline.
### Operators
- [static func == (AnimationPlaybackController, AnimationPlaybackController) -> Bool](./animationplaybackcontroller/eqeq%28_,_%29.md)
  Indicates whether two animation playback controllers are equal.
### Instance Methods
- [func hash(into: inout Hasher)](./animationplaybackcontroller/hash%28into%29.md)
  Hashes the essential components of the controller by feeding them into the given hash function.
- [func stop(blendOutDuration: TimeInterval)](./animationplaybackcontroller/stop%28blendoutduration%29.md)
  Stops an animation with a fade-out time.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Observable](../Observation/observable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Animation playback
- [Automatically animating RealityKit entities](./automatically-animating-realitykit-entities.md)
  Invoke implicit animations by setting the entity’s desired end state.
- [class AnimationResource](./animationresource.md)
  An animation for the properties of scenes or entities.
- [struct AnimationLibraryComponent](./animationlibrarycomponent.md)
  A component that represents a collection of animations that an entity can play.
- [AnimationLibraryComponent.AnimationCollection](./animationlibrarycomponent/animationcollection.md)
  A collection of animations an entity can play.
- [enum AnimationEvents](./animationevents.md)
  Notable milestones that the framework signals during animation playback.
- [enum AnimationRepeatMode](./animationrepeatmode.md)
  Options that determine whether an animation replays after completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller)*