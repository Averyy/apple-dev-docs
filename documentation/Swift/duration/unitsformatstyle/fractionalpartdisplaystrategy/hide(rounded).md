# hide(rounded:)

**Framework**: Swift  
**Kind**: method  
**Role**: Type Method

Creates a display strategy that hides any fractional part rounding the unit value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func hide(rounded: FloatingPointRoundingRule = .toNearestOrEven) -> Duration.UnitsFormatStyle.FractionalPartDisplayStrategy
```

## See Also

### Using common strategies
- [static var hide: Duration.UnitsFormatStyle.FractionalPartDisplayStrategy](./hide.md)
  A display strategy that hides any fractional part by truncating it.
- [static func show(length: Int, rounded: FloatingPointRoundingRule, increment: Double?) -> Duration.UnitsFormatStyle.FractionalPartDisplayStrategy](./show%28length,rounded,increment%29.md)
  Creates a display strategy that shows a fractional part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/fractionalpartdisplaystrategy/hide(rounded:))*