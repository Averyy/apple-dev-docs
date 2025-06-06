# interpolated(towards:amount:)

**Framework**: SwiftUI  
**Kind**: method

Returns this value interpolated with `other` by the specified `amount`.

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
func interpolated(towards other: Self, amount: Double) -> Self
```

#### Discussion

This result is equivalent to `self + (other - self) * amount`.

## See Also

- [var magnitudeSquared: Double](vectorarithmetic/magnitudesquared.md)
  Returns the dot-product of this vector arithmetic instance with itself.
- [func scale(by: Double)](vectorarithmetic/scale(by:).md)
  Multiplies each component of this value by the given value.
- [func scaled(by: Double) -> Self](vectorarithmetic/scaled(by:).md)
  Returns a value with each component of this value multiplied by the given value.
- [func interpolate(towards: Self, amount: Double)](vectorarithmetic/interpolate(towards:amount:).md)
  Interpolates this value with `other` by the specified `amount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/vectorarithmetic/interpolated(towards:amount:))*