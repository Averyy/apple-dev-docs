# interpolate(towards:amount:)

**Framework**: SwiftUI  
**Kind**: method

Interpolates this value with `other` by the specified `amount`.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
mutating func interpolate(towards other: Self, amount: Double)
```

#### Discussion

This is equivalent to `self = self + (other - self) * amount`.

## See Also

- [var magnitudeSquared: Double](vectorarithmetic/magnitudesquared.md)
  Returns the dot-product of this vector arithmetic instance with itself.
- [func scale(by: Double)](vectorarithmetic/scale(by:).md)
  Multiplies each component of this value by the given value.
- [func scaled(by: Double) -> Self](vectorarithmetic/scaled(by:).md)
  Returns a value with each component of this value multiplied by the given value.
- [func interpolated(towards: Self, amount: Double) -> Self](vectorarithmetic/interpolated(towards:amount:).md)
  Returns this value interpolated with `other` by the specified `amount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/vectorarithmetic/interpolate(towards:amount:))*