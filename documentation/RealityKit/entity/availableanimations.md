# availableAnimations

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The list of animations associated with the entity.

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
@preconcurrency var availableAnimations: [AnimationResource] { get }
```

## Discussion

When you import an entity from a file, for example by using the [`load(named:in:)`](./load%28named,in%29.md) method, the entity might contain associated animations. Any that RealityKit supports appear in the [`availableAnimations`](./availableanimations.md) array.

To play a particular animation resource from the list, call the [`playAnimation(_:transitionDuration:startsPaused:)`](./playanimation%28_,transitionduration,startspaused%29.md) method. Alternatively, to play all animations with a given name, call the `playAnimation(named:transitionDuration:startsPaused:)` method instead.

## See Also

### Animating an entity
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
- [func playAnimation(named: String, transitionDuration: TimeInterval, startsPaused: Bool, recursive: Bool) -> AnimationPlaybackController](./playanimation%28named,transitionduration,startspaused,recursive%29.md)
  Plays all the animations with the given name on the entity.
- [var bindableValues: BindableValuesReference](./bindablevalues.md)
- [subscript(BindTarget.EntityPath) -> Entity?](./subscript%28_%29.md)
  Resolves the entity from the given entity path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/availableanimations)*