# playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:)

**Framework**: RealityKit  
**Kind**: method

Plays an animation with the specified options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func playAnimation(_ animation: AnimationResource, transitionDuration: TimeInterval = 0, blendLayerOffset: Int = 0, separateAnimatedValue: Bool = false, startsPaused: Bool = false, clock: CMClockOrTimebase? = nil) -> AnimationPlaybackController
```

#### Discussion

Call this method to play an animation and configure playback options. RealityKit supports blending up to two different animations at the same time. When RealityKit applies multiple animations to an entity, the order in which it applies the animations affects the final animation. Use the `blendLayerOffset` parameter to specify the order of animations when playing multiple animations at the same time.

## Parameters

- `animation`: The animation to play.
- `transitionDuration`: The duration in seconds over which the animation   fades in or cross-fades.
- `blendLayerOffset`: An integer that specifies the order in which to   apply animations when more than one animation is playing. Valid values   are   or  .
- `separateAnimatedValue`: When set to false, this value indicates that the   animation will write directly to the entity’s base value. When set to true,   this value indicates that the animation will write to an interim value for   the duration of the animation. If this value is set to true then when the   animation completes, the entity’s value will be reset to the base value.
- `startsPaused`: A Boolean that pauses the progress of an animation when   set to  .
- `clock`: An optional clock to drive the animation with a custom   timescale.

## See Also

- [var availableAnimations: [AnimationResource]](entity/availableanimations.md)
  The list of animations associated with the entity.
- [func playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:handoffType:)](entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:handofftype:).md)
  Plays an animation with the specified options.
- [func playAnimation(AnimationResource, transitionDuration: TimeInterval, startsPaused: Bool) -> AnimationPlaybackController](entity/playanimation(_:transitionduration:startspaused:).md)
  Plays the given animation on the entity.
- [func stopAllAnimations(recursive: Bool)](entity/stopallanimations(recursive:).md)
  Stops all playing of animations on this entity.
- [struct ParameterSet](parameterset.md)
  A reference to general-purpose entity parameters for animations.
- [func playAnimation(named: String, transitionDuration: TimeInterval, startsPaused: Bool, recursive: Bool) -> AnimationPlaybackController](entity/playanimation(named:transitionduration:startspaused:recursive:).md)
  Plays all the animations with the given name on the entity.
- [subscript(_:)](entity/subscript(_:).md)
  Resolves the entity from the given entity path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:))*