# ParameterSet

**Framework**: RealityKit  
**Kind**: struct

A reference to general-purpose entity parameters for animations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct ParameterSet
```

#### Overview

Subscript this structure to access a particular property by name. The return value is [`BindableValue`](bindablevalue.md) `<T>`, where `T` is one of the adopting [`BindableData`](bindabledata.md) types.

As a reference, this structure doesn’t exhibit copy-on-write behavior.

## Topics

### Accessing a parameter by name
- [subscript<T>(String, T.Type) -> BindableValue<T>?](parameterset/subscript(_:_:).md)
  Provides a bindable value for the given name.

## See Also

- [var availableAnimations: [AnimationResource]](entity/availableanimations.md)
  The list of animations associated with the entity.
- [func playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:)](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:).md)
  Plays an animation with the specified options.
- [func playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:handoffType:)](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:handofftype:).md)
  Plays an animation with the specified options.
- [func playAnimation(AnimationResource, transitionDuration: TimeInterval, startsPaused: Bool) -> AnimationPlaybackController](entity/playanimation(_:transitionduration:startspaused:).md)
  Plays the given animation on the entity.
- [func stopAllAnimations(recursive: Bool)](entity/stopallanimations(recursive:).md)
  Stops all playing of animations on this entity.
- [func playAnimation(named: String, transitionDuration: TimeInterval, startsPaused: Bool, recursive: Bool) -> AnimationPlaybackController](entity/playanimation(named:transitionduration:startspaused:recursive:).md)
  Plays all the animations with the given name on the entity.
- [subscript(_:)](entity/subscript(_:).md)
  Resolves the entity from the given entity path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/parameterset)*