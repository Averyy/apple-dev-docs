# padded(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a custom format style that represents the three or more digits of the year in week-of-year calendars, zero-padded if necessary.

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
static func padded(_ length: Int) -> Date.FormatStyle.Symbol.YearForWeekOfYear
```

## Return Value

A custom year format style that portrays the year of a week of year calendar system with the provided length.

## Parameters

- `length`: The length of the string to display a calendar year.

## See Also

### Modifying a Year for Week-of-Year
- [static var defaultDigits: Date.FormatStyle.Symbol.YearForWeekOfYear](./defaultdigits.md)
  Custom week of the year format style showing the minimum number of digits that represents the year in week-of-year calendars.
- [static var twoDigits: Date.FormatStyle.Symbol.YearForWeekOfYear](./twodigits.md)
  The custom format style that represents the two-digit numeric year in week-of-year calendars, zero-padded or truncated if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/yearforweekofyear/padded(_:))*