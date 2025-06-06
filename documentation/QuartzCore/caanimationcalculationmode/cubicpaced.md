# cubicPaced

**Framework**: Core Animation  
**Kind**: property

Cubic keyframe values are interpolated to produce an even pace throughout the animation.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let cubicPaced: CAAnimationCalculationMode
```

#### Discussion

`kCAAnimationCubicPaced` gives a linearly interpolated animation, but [`keyTimes`](cakeyframeanimation/keytimes.md) and [`timingFunction`](caanimation/timingfunction.md) are ignored and keyframe times are automatically generated to give the animation a constant velocity.

The following code shows how to create a keyframe animation object using paced cubic interpolation.

```objc
let keyframeAnimation = CAKeyframeAnimation(keyPath: "position.y")
keyframeAnimation.calculationMode = kCAAnimationCubicPaced
keyframeAnimation.values = [310, 60, 120, 60, 310]
```

A layer animated with the keyframe animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Tracing the path of an animation using cubic paced key values](https://docs-assets.developer.apple.com/published/eb23aecda8eb2e1e569d68b1ca5c2938/media-2776794%402x.png)

## See Also

- [static let linear: CAAnimationCalculationMode](caanimationcalculationmode/linear.md)
  Simple linear calculation between keyframe values.
- [static let discrete: CAAnimationCalculationMode](caanimationcalculationmode/discrete.md)
  Each keyframe value is used in turn, no interpolated values are calculated.
- [static let paced: CAAnimationCalculationMode](caanimationcalculationmode/paced.md)
  Linear keyframe values are interpolated to produce an even pace throughout the animation.
- [static let cubic: CAAnimationCalculationMode](caanimationcalculationmode/cubic.md)
  Smooth spline calculation between keyframe values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/cubicpaced)*