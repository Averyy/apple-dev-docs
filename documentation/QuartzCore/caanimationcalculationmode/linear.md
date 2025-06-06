# linear

**Framework**: Core Animation  
**Kind**: property

Simple linear calculation between keyframe values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let linear: CAAnimationCalculationMode
```

#### Discussion

The following code shows how to create a keyframe animation object using linear interpolation.

Listing 1. Creating linearly interpolated keyframes

```swift
let keyframeAnimation = CAKeyframeAnimation(keyPath: "position.y")
keyframeAnimation.calculationMode = kCAAnimationLinear
keyframeAnimation.keyTimes = [0, 0.25, 0.5, 0.75, 1]
keyframeAnimation.values = [310, 60, 120, 60, 310]
```

A layer animated with the keyframe animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Tracing the path of an animation using linearly interpolated keyframes](https://docs-assets.developer.apple.com/published/0c5d43aa12ef1a5f2a1deb521dc2f0c1/media-2776788%402x.png)

## See Also

- [static let discrete: CAAnimationCalculationMode](caanimationcalculationmode/discrete.md)
  Each keyframe value is used in turn, no interpolated values are calculated.
- [static let paced: CAAnimationCalculationMode](caanimationcalculationmode/paced.md)
  Linear keyframe values are interpolated to produce an even pace throughout the animation.
- [static let cubic: CAAnimationCalculationMode](caanimationcalculationmode/cubic.md)
  Smooth spline calculation between keyframe values.
- [static let cubicPaced: CAAnimationCalculationMode](caanimationcalculationmode/cubicpaced.md)
  Cubic keyframe values are interpolated to produce an even pace throughout the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/linear)*