# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Create an `Animation` that contains the specified custom animation.

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
init<A>(_ base: A) where A : CustomAnimation
```

## See Also

### Creating custom animations
- [static func timingCurve(UnitCurve, duration: TimeInterval) -> Animation](./timingcurve%28_,duration%29.md)
  Creates a new animation with speed controlled by the given curve.
- [static func timingCurve(Double, Double, Double, Double, duration: TimeInterval) -> Animation](./timingcurve%28_,_,_,_,duration%29.md)
  An animation created from a cubic Bézier timing curve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animation/init(_:))*