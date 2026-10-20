# cubic

**Framework**: Core Animation  
**Kind**: property  
**Role**: Type Property

Smooth spline calculation between keyframe values.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let cubic: CAAnimationCalculationMode
```

```c
extern CAAnimationCalculationMode const kCAAnimationCubic;
```

#### Discussion

Intermediate frames are computed using a Catmull-Rom spline that passes through the keyframes. You can adjust the shape of the spline by specifying an optional set of tension, continuity, and bias values, which modify the spline using the standard Kochanek-Bartels form.

The following code shows how to create a keyframe animation object using cubic interpolation.

```swift
let keyframeAnimation = CAKeyframeAnimation(keyPath: "position.y")
keyframeAnimation.calculationMode = kCAAnimationCubic
keyframeAnimation.keyTimes = [0, 0.25, 0.5, 0.75, 1]
keyframeAnimation.values = [310, 60, 120, 60, 310]
```

A layer animated with the keyframe animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Tracing the path of an animation using cubic spline interpolated keyframes](https://developer.apple.com/tutorials/images/com.apple.quartzcore/media-2776790@2x.png)

## See Also

### Constants
- [static let linear: CAAnimationCalculationMode](./linear.md)
  Simple linear calculation between keyframe values.
- [static let discrete: CAAnimationCalculationMode](./discrete.md)
  Each keyframe value is used in turn, no interpolated values are calculated.
- [static let paced: CAAnimationCalculationMode](./paced.md)
  Linear keyframe values are interpolated to produce an even pace throughout the animation.
- [static let cubicPaced: CAAnimationCalculationMode](./cubicpaced.md)
  Cubic keyframe values are interpolated to produce an even pace throughout the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode/cubic)*