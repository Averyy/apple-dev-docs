# defaultDigits

**Framework**: Foundation  
**Kind**: property

Custom week of the year format style showing the minimum number of digits that represents the year in week-of-year calendars.

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
static var defaultDigits: Date.FormatStyle.Symbol.YearForWeekOfYear { get }
```

#### Discussion

This represents week-of-year values like `1` or `18`.

## See Also

- [static var twoDigits: Date.FormatStyle.Symbol.YearForWeekOfYear](date/formatstyle/symbol/yearforweekofyear/twodigits.md)
  The custom format style that represents the two-digit numeric year in week-of-year calendars, zero-padded or truncated if necessary.
- [static func padded(Int) -> Date.FormatStyle.Symbol.YearForWeekOfYear](date/formatstyle/symbol/yearforweekofyear/padded(_:).md)
  Returns a custom format style that represents the three or more digits of the year in week-of-year calendars, zero-padded if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/yearforweekofyear/defaultdigits)*