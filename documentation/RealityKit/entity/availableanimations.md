# availableAnimations

**Framework**: RealityKit  
**Kind**: property

The list of animations associated with the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var availableAnimations: [AnimationResource] { get }
```

#### Discussion

When you import an entity from a file, for example by using the [`load(named:in:)`](entity/load(named:in:).md) method, the entity might contain associated animations. Any that RealityKit supports appear in the [`availableAnimations`](entity/availableanimations.md) array.

To play a particular animation resource from the list, call the [`playAnimation(_:transitionDuration:startsPaused:)`](entity/playanimation(_:transitionduration:startspaused:).md) method. Alternatively, to play all animations with a given name, call the `playAnimation(named:transitionDuration:startsPaused:)` method instead.

## See Also

- [func playAnimation(AnimationResource, transitionDuration: TimeInterval, blendLayerOffset: Int, separateAnimatedValue: Bool, startsPaused: Bool, clock: CMClockOrTimebase?) -> AnimationPlaybackController](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:).md)
  Plays an animation with the specified options.
- [func playAnimation(AnimationResource, transitionDuration: TimeInterval, blendLayerOffset: Int, separateAnimatedValue: Bool, startsPaused: Bool, clock: CMClockOrTimebase?, handoffType: AnimationHandoffType) -> AnimationPlaybackController](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:handofftype:).md)
  Plays an animation with the specified options.
- [func playAnimation(AnimationResource, transitionDuration: TimeInterval, startsPaused: Bool) -> AnimationPlaybackController](entity/playanimation(_:transitionduration:startspaused:).md)
  Plays the given animation on the entity.
- [func stopAllAnimations(recursive: Bool)](entity/stopallanimations(recursive:).md)
  Stops all playing of animations on this entity.
- [var defaultAnimationClock: CMClockOrTimebase](entity/defaultanimationclock.md)
  Returns the default animation clock for this entity.
- [var parameters: Entity.ParameterSet](entity/parameters.md)
  Represents a reference to the parameters for a particular entity.
- [Entity.ParameterSet](entity/parameterset.md)
  Represents a reference to the parameters for a particular entity.
- [func playAnimation(named: String, transitionDuration: TimeInterval, startsPaused: Bool, recursive: Bool) -> AnimationPlaybackController](entity/playanimation(named:transitionduration:startspaused:recursive:).md)
  Plays all the animations with the given name on the entity.
- [var bindableValues: BindableValuesReference](entity/bindablevalues.md)
- [subscript(BindTarget.EntityPath) -> Entity?](entity/subscript(_:).md)
  Resolves the entity from the given entity path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/availableanimations)*