# timingCurve(_:duration:)

**Framework**: SwiftUI  
**Kind**: method

Creates a new animation with speed controlled by the given curve.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func timingCurve(_ curve: UnitCurve, duration: TimeInterval) -> Animation
```

## Parameters

- `curve`: A curve that describes the speed of the animation over its duration.
- `duration`: The duration of the animation, in seconds.

## See Also

- [init<A>(A)](animation/init(_:).md)
  Create an `Animation` that contains the specified custom animation.
- [static func timingCurve(Double, Double, Double, Double, duration: TimeInterval) -> Animation](animation/timingcurve(_:_:_:_:duration:).md)
  An animation created from a cubic Bézier timing curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/timingcurve(_:duration:))*