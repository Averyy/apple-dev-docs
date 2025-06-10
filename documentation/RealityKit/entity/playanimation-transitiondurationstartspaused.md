# playAnimation(_:transitionDuration:startsPaused:)

**Framework**: RealityKit  
**Kind**: method

Plays the given animation on the entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func playAnimation(_ animation: AnimationResource, transitionDuration: TimeInterval, startsPaused: Bool) -> AnimationPlaybackController
```

#### Return Value

An animation playback controller that you can use to start and stop the animation.

## Parameters

- `animation`: The animation to play.
- `transitionDuration`: The duration in seconds over which the animation   fades in or cross-fades.
- `startsPaused`: A Boolean that you set to   to return from the call   with the animation paused. Set to   to start the animation right away.

## See Also

- [var availableAnimations: [AnimationResource]](entity/availableanimations.md)
  The list of animations associated with the entity.
- [func playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:)](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:).md)
  Plays an animation with the specified options.
- [func playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:handoffType:)](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:handofftype:).md)
  Plays an animation with the specified options.
- [func stopAllAnimations(recursive: Bool)](entity/stopallanimations(recursive:).md)
  Stops all playing of animations on this entity.
- [struct ParameterSet](parameterset.md)
  A reference to general-purpose entity parameters for animations.
- [func playAnimation(named: String, transitionDuration: TimeInterval, startsPaused: Bool, recursive: Bool) -> AnimationPlaybackController](entity/playanimation(named:transitionduration:startspaused:recursive:).md)
  Plays all the animations with the given name on the entity.
- [subscript(_:)](entity/subscript(_:).md)
  Resolves the entity from the given entity path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/playanimation(_:transitionduration:startspaused:))*