# milliseconds(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a custom format style representing the milliseconds elapsed in a day.

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
static func milliseconds(_ val: Int) -> Date.FormatStyle.Symbol.SecondFraction
```

#### Return Value

Returns the number of milliseconds elapsed in the day.

## Parameters

- `val`: Length of the string representation of the number of milliseconds elapsed in a day.

## See Also

### Modifying a Second Fraction
- [static func fractional(Int) -> Date.FormatStyle.Symbol.SecondFraction](./fractional%28_%29.md)
  Creates a custom format style representing the fractional seconds component of a date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/secondfraction/milliseconds(_:))*