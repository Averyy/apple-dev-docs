# scaled(by:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Returns a value with each component of this value multiplied by the given value.

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
func scaled(by rhs: Double) -> Self
```

## See Also

### Manipulating values
- [var magnitudeSquared: Double](./magnitudesquared.md)
  Returns the dot-product of this vector arithmetic instance with itself.
- [func scale(by: Double)](./scale%28by%29.md)
  Multiplies each component of this value by the given value.
- [func interpolate(towards: Self, amount: Double)](./interpolate%28towards,amount%29.md)
  Interpolates this value with `other` by the specified `amount`.
- [func interpolated(towards: Self, amount: Double) -> Self](./interpolated%28towards,amount%29.md)
  Returns this value interpolated with `other` by the specified `amount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/vectorarithmetic/scaled(by:))*