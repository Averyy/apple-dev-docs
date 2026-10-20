# fractional(_:)

**Framework**: Foundation  
**Kind**: method

Creates a custom format style representing the fractional seconds component of a date.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func fractional(_ val: Int) -> Date.FormatStyle.Symbol.SecondFraction
```

#### Return Value

Returns the numerical representation of the fractional component of the second.

## Parameters

- `val`: Length of the string representation of the fractional seconds component.

## See Also

- [static func milliseconds(Int) -> Date.FormatStyle.Symbol.SecondFraction](date/formatstyle/symbol/secondfraction/milliseconds(_:).md)
  Creates a custom format style representing the milliseconds elapsed in a day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/secondfraction/fractional(_:))*