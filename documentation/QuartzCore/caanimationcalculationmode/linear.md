# linear

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

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

```c
extern CAAnimationCalculationMode const kCAAnimationLinear;
```

## Discussion

The following code shows how to create a keyframe animation object using linear interpolation.

Listing 1. Creating linearly interpolated keyframes

```swift
let keyframeAnimation = CAKeyframeAnimation(keyPath: "position.y")
keyframeAnimation.calculationMode = kCAAnimationLinear
keyframeAnimation.keyTimes = [0, 0.25, 0.5, 0.75, 1]
keyframeAnimation.values = [310, 60, 120, 60, 310]
```

A layer animated with the keyframe animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Tracing the path of an animation using linearly interpolated keyframes](https://developer.apple.com/tutorials/images/com.apple.quartzcore/media-2776788@2x.png)

## See Also

### Constants
- [static let discrete: CAAnimationCalculationMode](./discrete.md)
  Each keyframe value is used in turn, no interpolated values are calculated.
- [static let paced: CAAnimationCalculationMode](./paced.md)
  Linear keyframe values are interpolated to produce an even pace throughout the animation.
- [static let cubic: CAAnimationCalculationMode](./cubic.md)
  Smooth spline calculation between keyframe values.
- [static let cubicPaced: CAAnimationCalculationMode](./cubicpaced.md)
  Cubic keyframe values are interpolated to produce an even pace throughout the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/linear)*