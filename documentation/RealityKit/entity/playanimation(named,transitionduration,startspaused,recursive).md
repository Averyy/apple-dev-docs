# playAnimation(named:transitionDuration:startsPaused:recursive:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Plays all the animations with the given name on the entity.

**Availability**:
- iOS 13.0+ - Deprecated
- iPadOS 13.0+ - Deprecated
- Mac Catalyst 13.0+ - Deprecated
- macOS 10.15+ - Deprecated
- visionOS 1.0+ - Deprecated

> **Deprecated**: Use playAnimation functions that take an AnimationResource instead of a name.

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func playAnimation(named animationName: String, transitionDuration: TimeInterval = 0, startsPaused: Bool = false, recursive: Bool = true) -> AnimationPlaybackController
```

#### Return Value

An animation playback controller that you can use to start and stop the animations.

#### Discussion

The method plays all the animations in the [`availableAnimations`](./availableanimations.md) property with a matching name. If there are none, the method returns a controller showing a stopped animation.

## Parameters

- `animationName`: The name of the animation.
- `transitionDuration`: The duration in seconds over which the animation fades in or cross-fades.
- `startsPaused`: A Boolean that you set to `true` to return from the call with the animations paused. Set to `false` to start the animations right away.
- `recursive`: Indicates whether to also play animations on all descendants of the entity.

## See Also

### Animating an entity
- [var availableAnimations: [AnimationResource]](./availableanimations.md)
  The list of animations associated with the entity.
- [func playAnimation(AnimationResource, transitionDuration: TimeInterval, blendLayerOffset: Int, separateAnimatedValue: Bool, startsPaused: Bool, clock: CMClockOrTimebase?) -> AnimationPlaybackController](./playanimation%28_,transitionduration,blendlayeroffset,separateanimatedvalue,startspaused,clock%29.md)
  Plays an animation with the specified options.
- [func playAnimation(AnimationResource, transitionDuration: TimeInterval, blendLayerOffset: Int, separateAnimatedValue: Bool, startsPaused: Bool, clock: CMClockOrTimebase?, handoffType: AnimationHandoffType) -> AnimationPlaybackController](./playanimation%28_,transitionduration,blendlayeroffset,separateanimatedvalue,startspaused,clock,handofftype%29.md)
  Plays an animation with the specified options.
- [func playAnimation(AnimationResource, transitionDuration: TimeInterval, startsPaused: Bool) -> AnimationPlaybackController](./playanimation%28_,transitionduration,startspaused%29.md)
  Plays the given animation on the entity.
- [func stopAllAnimations(recursive: Bool)](./stopallanimations%28recursive%29.md)
  Stops all playing of animations on this entity.
- [var defaultAnimationClock: CMClockOrTimebase](./defaultanimationclock.md)
  Returns the default animation clock for this entity.
- [var parameters: Entity.ParameterSet](./parameters.md)
  Represents a reference to the parameters for a particular entity.
- [Entity.ParameterSet](./parameterset.md)
  Represents a reference to the parameters for a particular entity.
- [var bindableValues: BindableValuesReference](./bindablevalues.md)
- [subscript(BindTarget.EntityPath) -> Entity?](./subscript%28_%29.md)
  Resolves the entity from the given entity path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/playanimation(named:transitionduration:startspaused:recursive:))*