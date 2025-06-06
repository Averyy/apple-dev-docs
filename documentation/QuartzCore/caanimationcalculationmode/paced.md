# paced

**Framework**: Core Animation  
**Kind**: property

Linear keyframe values are interpolated to produce an even pace throughout the animation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let paced: CAAnimationCalculationMode
```

#### Discussion

`kCAAnimationPaced` gives a linearly interpolated animation, but [`keyTimes`](cakeyframeanimation/keytimes.md) and [`timingFunction`](caanimation/timingfunction.md) are ignored and keyframe times are automatically generated to give the animation a constant velocity.

The following code shows how to create a keyframe animation object using paced interpolation.

Listing 1. Creating paced key values

```objc
let keyframeAnimation = CAKeyframeAnimation(keyPath: "position.y")
keyframeAnimation.calculationMode = kCAAnimationPaced
keyframeAnimation.values = [310, 60, 120, 60, 310]
```

A layer animated with the keyframe animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Tracing the path of an animation using paced key values](https://docs-assets.developer.apple.com/published/59fe9ad7c28a77c4f7d2456ef55d3394/media-2776792%402x.png)

## See Also

- [static let linear: CAAnimationCalculationMode](caanimationcalculationmode/linear.md)
  Simple linear calculation between keyframe values.
- [static let discrete: CAAnimationCalculationMode](caanimationcalculationmode/discrete.md)
  Each keyframe value is used in turn, no interpolated values are calculated.
- [static let cubic: CAAnimationCalculationMode](caanimationcalculationmode/cubic.md)
  Smooth spline calculation between keyframe values.
- [static let cubicPaced: CAAnimationCalculationMode](caanimationcalculationmode/cubicpaced.md)
  Cubic keyframe values are interpolated to produce an even pace throughout the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/paced)*