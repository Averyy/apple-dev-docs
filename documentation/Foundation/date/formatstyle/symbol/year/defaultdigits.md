# defaultDigits

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The custom year format style showing the minimum number of digits that represents the numeric year.

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
static var defaultDigits: Date.FormatStyle.Symbol.Year { get }
```

## Discussion

This style represents years like `1`, `18`, `202`, and `2020`.

## See Also

### Modifying a Year
- [static var twoDigits: Date.FormatStyle.Symbol.Year](./twodigits.md)
  The custom format style portraying the two-digit numeric year, zero-padded if necessary.
- [static func padded(Int) -> Date.FormatStyle.Symbol.Year](./padded%28_%29.md)
  Returns a custom format style that portrays the year of the calendar system of the provided length, zero-padded if necessary.
- [static func relatedGregorian(minimumLength: Int) -> Date.FormatStyle.Symbol.Year](./relatedgregorian%28minimumlength%29.md)
  Returns a custom format style that portrays the year of a non-Gregorian calendar system in the corresponding Gregorian year.
- [static func extended(minimumLength: Int) -> Date.FormatStyle.Symbol.Year](./extended%28minimumlength%29.md)
  Returns a custom format style that portrays the year of the calendar system, encompassing all supra-year fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/year/defaultdigits)*