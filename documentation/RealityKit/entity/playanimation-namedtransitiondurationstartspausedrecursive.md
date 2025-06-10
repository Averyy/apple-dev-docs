# playAnimation(named:transitionDuration:startsPaused:recursive:)

**Framework**: RealityKit  
**Kind**: method

Plays all the animations with the given name on the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func playAnimation(named animationName: String, transitionDuration: TimeInterval = 0, startsPaused: Bool = false, recursive: Bool = true) -> AnimationPlaybackController
```

#### Return Value

An animation playback controller that you can use to start and stop the animations.

#### Discussion

The method plays all the animations in the [`availableAnimations`](entity/availableanimations.md) property with a matching name. If there are none, the method returns a controller showing a stopped animation.

## Parameters

- `animationName`: The name of the animation.
- `transitionDuration`: The duration in seconds over which the animation   fades in or cross-fades.
- `startsPaused`: A Boolean that you set to   to return from the call   with the animations paused. Set to   to start the animations right   away.
- `recursive`: Indicates whether to also play animations on all   descendants of the entity.

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
- [struct ParameterSet](parameterset.md)
  A reference to general-purpose entity parameters for animations.
- [subscript(_:)](entity/subscript(_:).md)
  Resolves the entity from the given entity path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/playanimation(named:transitionduration:startspaused:recursive:))*