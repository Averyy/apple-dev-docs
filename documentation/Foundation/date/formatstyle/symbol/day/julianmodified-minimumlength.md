# julianModified(minimumLength:)

**Framework**: Foundation  
**Kind**: method

Creates a custom day format style representing the modified Julian day.

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
static func julianModified(minimumLength: Int = 1) -> Date.FormatStyle.Symbol.Day
```

#### Return Value

The minimum length specifies the minimum number of digits, zero-padded if necessary. For example, `002451334`.

## Parameters

- `minimumLength`: Specifies the minimum number of digits.

## See Also

- [static var defaultDigits: Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/defaultdigits.md)
  Custom format style portraying the minimum number of digits that represents the numeric day of month.
- [static var ordinalOfDayInMonth: Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/ordinalofdayinmonth.md)
  Custom format style portraying the ordinal of the day in the month.
- [static var twoDigits: Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day/twodigits.md)
  Custom format style portraying the two-digit numeric day of month, zero-padded if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/day/julianmodified(minimumlength:))*