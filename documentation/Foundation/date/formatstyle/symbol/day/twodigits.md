# twoDigits

**Framework**: Foundation  
**Kind**: property

Custom format style portraying the two-digit numeric day of month, zero-padded if necessary.

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
static var twoDigits: Date.FormatStyle.Symbol.Day { get }
```

#### Discussion

This style produces `01` for the first day of the month and `18` for the eighteenth. To use single digits when possible, use [`defaultDigits`](date/formatstyle/symbol/day/defaultdigits.md).

## See Also

- [static var defaultDigits: Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/defaultdigits.md)
  Custom format style portraying the minimum number of digits that represents the numeric day of month.
- [static var ordinalOfDayInMonth: Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/ordinalofdayinmonth.md)
  Custom format style portraying the ordinal of the day in the month.
- [static func julianModified(minimumLength: Int) -> Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/julianmodified(minimumlength:).md)
  Creates a custom day format style representing the modified Julian day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/day/twodigits)*