# Entity.ParameterSet

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Represents a reference to the parameters for a particular entity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct ParameterSet
```

#### Overview

Note this struct is a reference and does not have copy-on-write semantics.

## Topics

### Subscripts
- [subscript<T>(String, T.Type) -> BindableValue<T>?](./parameterset/subscript%28_,_%29.md)
  Accessor for the parameters, returns a bindable value.

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
- [func playAnimation(named: String, transitionDuration: TimeInterval, startsPaused: Bool, recursive: Bool) -> AnimationPlaybackController](./playanimation%28named,transitionduration,startspaused,recursive%29.md)
  Plays all the animations with the given name on the entity.
- [var bindableValues: BindableValuesReference](./bindablevalues.md)
- [subscript(BindTarget.EntityPath) -> Entity?](./subscript%28_%29.md)
  Resolves the entity from the given entity path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/parameterset)*