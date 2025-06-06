# default

**Framework**: Core Animation  
**Kind**: property

The system default timing function. Use this function to ensure that the timing of your animations matches that of most system animations.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let `default`: CAMediaTimingFunctionName
```

#### Discussion

This is a Bézier timing function with the control points (0.25,0.1) and (0.25,1.0).

The following code shows how to create a basic animation object using default interpolation:

```swift
 let verticalAnimation = CABasicAnimation(keyPath: "position.y")
 verticalAnimation.fromValue = 310
 verticalAnimation.toValue = 10
 verticalAnimation.timingFunction = CAMediaTimingFunction(name: kCAMediaTimingFunctionDefault)
```

A layer animated with the animation created by the code above and with linearly interpolated horizontal movement would describe a path similar to the following figure.

![Path taken using default timing function](https://docs-assets.developer.apple.com/published/6d2d45f802f21dfcfe8293fa2a57596f/media-2776820%402x.png)

## See Also

- [static let linear: CAMediaTimingFunctionName](camediatimingfunctionname/linear.md)
  Linear pacing, which causes an animation to occur evenly over its duration.
- [static let easeIn: CAMediaTimingFunctionName](camediatimingfunctionname/easein.md)
  Ease-in pacing, which causes an animation to begin slowly and then speed up as it progresses.
- [static let easeOut: CAMediaTimingFunctionName](camediatimingfunctionname/easeout.md)
  Ease-out pacing, which causes an animation to begin quickly and then slow as it progresses.
- [static let easeInEaseOut: CAMediaTimingFunctionName](camediatimingfunctionname/easeineaseout.md)
  Ease-in-ease-out pacing, which causes an animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfunctionname/default)*