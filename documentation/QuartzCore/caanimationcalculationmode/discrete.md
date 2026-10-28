# discrete

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

Each keyframe value is used in turn, no interpolated values are calculated.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let discrete: CAAnimationCalculationMode
```

```c
extern CAAnimationCalculationMode const kCAAnimationDiscrete;
```

## Discussion

Keyframe animations based on discrete calculation interpolation require one less element in the [`values`](../cakeyframeanimation/values.md) array than the [`keyTimes`](../cakeyframeanimation/keytimes.md) array. Each `value / keyTime` pair represents the value from the specified time until the next keyframe.

For example, given the [`CAKeyframeAnimation`](../cakeyframeanimation.md) created in the following code, the penultimate keyTime, `0.75`, has a related value of `60`. The value of `position.y` will remain at `60` until the animation completes.

```swift
let keyframeAnimation = CAKeyframeAnimation(keyPath: "position.y")
keyframeAnimation.calculationMode = kCAAnimationDiscrete
  
// keyframe 0: (0, 310), keyframe 1: (0.25, 60), keyframe 2: (0.5, 120), keyframe 3: (0.75, 60)
keyframeAnimation.keyTimes = [0, 0.25, 0.5, 0.75, 1]
keyframeAnimation.values = [310, 60, 120, 60]
```

A layer animated with the keyframe animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Tracing the path of an animation using discrete keyframes](https://developer.apple.com/tutorials/images/com.apple.quartzcore/media-2776786@2x.png)

## See Also

### Constants
- [static let linear: CAAnimationCalculationMode](./linear.md)
  Simple linear calculation between keyframe values.
- [static let paced: CAAnimationCalculationMode](./paced.md)
  Linear keyframe values are interpolated to produce an even pace throughout the animation.
- [static let cubic: CAAnimationCalculationMode](./cubic.md)
  Smooth spline calculation between keyframe values.
- [static let cubicPaced: CAAnimationCalculationMode](./cubicpaced.md)
  Cubic keyframe values are interpolated to produce an even pace throughout the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/discrete)*