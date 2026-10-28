# playAnimation(_:transitionDuration:blendLayerOffset:separateAnimatedValue:startsPaused:clock:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Plays an animation with the specified options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func playAnimation(_ animation: AnimationResource, transitionDuration: TimeInterval = 0, blendLayerOffset: Int = 0, separateAnimatedValue: Bool = false, startsPaused: Bool = false, clock: CMClockOrTimebase? = nil) -> AnimationPlaybackController
```

## Discussion

Call this method to play an animation and configure playback options. RealityKit supports blending up to two different animations at the same time. When RealityKit applies multiple animations to an entity, the order in which it applies the animations affects the final animation. Use the `blendLayerOffset` parameter to specify the order of animations when playing multiple animations at the same time.

## Parameters

- `animation`: The animation to play.
- `transitionDuration`: The duration in seconds over which the animation fades in or cross-fades.
- `blendLayerOffset`: An integer that specifies the order in which to apply animations when more than one animation is playing. Valid values are `0` or `1`.
- `separateAnimatedValue`: When set to false, this value indicates that the animation will write directly to the entity’s base value. When set to true, this value indicates that the animation will write to an interim value for the duration of the animation. If this value is set to true then when the animation completes, the entity’s value will be reset to the base value.
- `startsPaused`: A Boolean that pauses the progress of an animation when set to `true`.
- `clock`: An optional clock to drive the animation with a custom timescale.

## See Also

### Animating an entity
- [var availableAnimations: [AnimationResource]](./availableanimations.md)
  The list of animations associated with the entity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/playanimation(_:transitionduration:blendlayeroffset:separateanimatedvalue:startspaused:clock:))*