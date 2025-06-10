# linear

**Framework**: RealityKit  
**Kind**: property

A timing function that produces a linear transition.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
static var linear: AnimationTimingFunction { get }
```

## See Also

- [static var `default`: AnimationTimingFunction](animationtimingfunction/default.md)
  A timing function that produces the default curve for the transition.
- [static var easeIn: AnimationTimingFunction](animationtimingfunction/easein.md)
  A timing function that produces a gradual starting transition.
- [static var easeInOut: AnimationTimingFunction](animationtimingfunction/easeinout.md)
  A timing function that produces a gradual starting and ending transition.
- [static var easeOut: AnimationTimingFunction](animationtimingfunction/easeout.md)
  A timing function that produces a gradual ending transition.
- [static func cubicBezier(controlPoint1: SIMD2<Float>, controlPoint2: SIMD2<Float>) -> AnimationTimingFunction](animationtimingfunction/cubicbezier(controlpoint1:controlpoint2:).md)
  Creates a timing function that accelerates and then decelerates towards the target value with the cubic bezier shape specified by two control points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationtimingfunction/linear)*