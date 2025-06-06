# linear

**Framework**: Core Animation  
**Kind**: property

Linear pacing, which causes an animation to occur evenly over its duration.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let linear: CAMediaTimingFunctionName
```

#### Discussion

This is a Bézier timing function with the control points (0.0,0.0) and (1.0,1.0).

The following code shows how to create a basic animation object using linear interpolation.

```swift
 let verticalAnimation = CABasicAnimation(keyPath: "position.y")
 verticalAnimation.fromValue = 310
 verticalAnimation.toValue = 10
 verticalAnimation.timingFunction = CAMediaTimingFunction(name: kCAMediaTimingFunctionLinear)
```

A layer animated with the animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Path taken using linear timing function](https://docs-assets.developer.apple.com/published/df8dce2b4ae224c6fa30b1be18ae35ff/media-2776812%402x.png)

## See Also

- [static let easeIn: CAMediaTimingFunctionName](camediatimingfunctionname/easein.md)
  Ease-in pacing, which causes an animation to begin slowly and then speed up as it progresses.
- [static let easeOut: CAMediaTimingFunctionName](camediatimingfunctionname/easeout.md)
  Ease-out pacing, which causes an animation to begin quickly and then slow as it progresses.
- [static let easeInEaseOut: CAMediaTimingFunctionName](camediatimingfunctionname/easeineaseout.md)
  Ease-in-ease-out pacing, which causes an animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [static let `default`: CAMediaTimingFunctionName](camediatimingfunctionname/default.md)
  The system default timing function. Use this function to ensure that the timing of your animations matches that of most system animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfunctionname/linear)*