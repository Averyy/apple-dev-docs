# interpolate(towards:amount:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
@export(implementation)
mutating func interpolate(towards other: Self, amount: Double)
```

#### Discussion

This is equivalent to `self = self + (other - self) * amount`.

## See Also

### Manipulating values
- [var magnitudeSquared: Double](./magnitudesquared.md)
  Returns the dot-product of this vector arithmetic instance with itself.
- [func scale(by: Double)](./scale%28by%29.md)
  Multiplies each component of this value by the given value.
- [func scaled(by: Double) -> Self](./scaled%28by%29.md)
  Returns a value with each component of this value multiplied by the given value.
- [func interpolated(towards: Self, amount: Double) -> Self](./interpolated%28towards,amount%29.md)
  Returns this value interpolated with `other` by the specified `amount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/vectorarithmetic/interpolate(towards:amount:))*