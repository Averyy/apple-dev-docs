# padded(_:)

**Framework**: Foundation  
**Kind**: method

Returns a custom format style that portrays the year of the calendar system of the provided length, zero-padded if necessary.

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
static func padded(_ length: Int) -> Date.FormatStyle.Symbol.Year
```

#### Return Value

A custom year format style that portrays the year of the calendar system with the provided length.

#### Discussion

Use [`padded(_:)`](date/formatstyle/symbol/year/padded(_:).md) to display a year using three or more digits, zero-padded if necessary. For example, `002`, `020`, `201`, `2017`.

## Parameters

- `length`: The length of the string to display a calendar year.

## See Also

- [static var defaultDigits: Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/defaultdigits.md)
  The custom year format style showing the minimum number of digits that represents the numeric year.
- [static var twoDigits: Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/twodigits.md)
  The custom format style portraying the two-digit numeric year, zero-padded if necessary.
- [static func relatedGregorian(minimumLength: Int) -> Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/relatedgregorian(minimumlength:).md)
  Returns a custom format style that portrays the year of a non-Gregorian calendar system in the corresponding Gregorian year.
- [static func extended(minimumLength: Int) -> Date.FormatStyle.Symbol.Year](date/formatstyle/symbol/year/extended(minimumlength:).md)
  Returns a custom format style that portrays the year of the calendar system, encompassing all supra-year fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/year/padded(_:))*