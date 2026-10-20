# easeIn

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

A timing function that produces a gradual starting transition.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
static var easeIn: AnimationTimingFunction { get }
```

## See Also

### Creating timing functions
- [static var `default`: AnimationTimingFunction](./default.md)
  A timing function that produces the default curve for the transition.
- [static var easeInOut: AnimationTimingFunction](./easeinout.md)
  A timing function that produces a gradual starting and ending transition.
- [static var easeOut: AnimationTimingFunction](./easeout.md)
  A timing function that produces a gradual ending transition.
- [static var linear: AnimationTimingFunction](./linear.md)
  A timing function that produces a linear transition.
- [static func cubicBezier(controlPoint1: SIMD2<Float>, controlPoint2: SIMD2<Float>) -> AnimationTimingFunction](./cubicbezier%28controlpoint1,controlpoint2%29.md)
  Creates a timing function that accelerates and then decelerates towards the target value with the cubic bezier shape specified by two control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationtimingfunction/easein)*