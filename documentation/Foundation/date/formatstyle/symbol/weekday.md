# Date.FormatStyle.Symbol.Weekday

**Framework**: Foundation  
**Kind**: struct

A type that specifies the format for the weekday name in a date format style.

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
struct Weekday
```

#### Overview

The type [`Date.FormatStyle.Symbol.Weekday`](date/formatstyle/symbol/weekday.md) includes static factory variables that create custom [`Date.FormatStyle.Symbol.Weekday`](date/formatstyle/symbol/weekday.md) objects:

| Factory variable | Description |
| --- | --- |
| [`abbreviated`](date/formatstyle/symbol/month/abbreviated.md) | Abbreviated weekday name. For example, `Tue`. |
| [`wide`](date/formatstyle/symbol/month/wide.md) | Wide weekday name. For example, `Tuesday`. |
| [`narrow`](date/formatstyle/symbol/month/narrow.md) | Narrow weekday name. For example, `T`. |
| [`short`](date/formatstyle/symbol/weekday/short.md) | Short weekday name. For example, `Tu`. |
| [`oneDigit`](date/formatstyle/symbol/weekday/onedigit.md) | Local numeric one-digit day of week. The value depends on the local starting day of the week. For example, this is `2` if Sunday is the first day of the week. |
| [`twoDigits`](date/formatstyle/symbol/weekday/twodigits.md) | Local numeric two-digit day of week, zero-padded if necessary. The value depends on the local starting day of the week. For example, this is `02` if Sunday is the first day of the week. |

To customize the weekday, name format in a string representation of a `Date`, use [`weekday(_:)`](date/formatstyle/weekday(_:).md). This example shows a variety of [`Date.FormatStyle.Symbol.Weekday`](date/formatstyle/symbol/weekday.md) format styles applied to a Thursday, using locale `en_US`:

```swift
let meetingDate = Date() // Feb 18, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().weekday(.abbreviated)) // Thu
meetingDate.formatted(Date.FormatStyle().weekday(.narrow)) // T
meetingDate.formatted(Date.FormatStyle().weekday(.short)) // Th
meetingDate.formatted(Date.FormatStyle().weekday(.wide)) // Thursday
meetingDate.formatted(Date.FormatStyle().weekday(.oneDigit)) // 5
meetingDate.formatted(Date.FormatStyle().weekday(.twoDigits)) // 05
meetingDate.formatted(Date.FormatStyle().weekday()) // Thu
```

If no format is specified as a parameter, the [`abbreviated`](date/formatstyle/symbol/month/abbreviated.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Weekday
- [static var abbreviated: Date.FormatStyle.Symbol.Weekday](date/formatstyle/symbol/weekday/abbreviated.md)
  A shortened weekday representation.
- [static var narrow: Date.FormatStyle.Symbol.Weekday](date/formatstyle/symbol/weekday/narrow.md)
  The shortest weekday representation.
- [static var oneDigit: Date.FormatStyle.Symbol.Weekday](date/formatstyle/symbol/weekday/onedigit.md)
  The one-digit representation of a weekday.
- [static var short: Date.FormatStyle.Symbol.Weekday](date/formatstyle/symbol/weekday/short.md)
  The short weekday representation.
- [static var twoDigits: Date.FormatStyle.Symbol.Weekday](date/formatstyle/symbol/weekday/twodigits.md)
  The two-digit representation of a standalone weekday, zero-padded if necessary.
- [static var wide: Date.FormatStyle.Symbol.Weekday](date/formatstyle/symbol/weekday/wide.md)
  The complete weekday representation.
### Comparing a Weekday
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Weekday](date/formatstyle/symbol/weekday/omitted.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Date.FormatStyle.Symbol.CyclicYear](date/formatstyle/symbol/cyclicyear.md)
  A type that specifies a format for a cyclic year in a date format style.
- [Date.FormatStyle.Symbol.Day](date/formatstyle/symbol/day.md)
  A type that specifies the format for a day in a date format style.
- [Date.FormatStyle.Symbol.DayOfYear](date/formatstyle/symbol/dayofyear.md)
  A type that specifies the format for the day of the year in a date format style.
- [Date.FormatStyle.Symbol.DayPeriod](date/formatstyle/symbol/dayperiod.md)
  A type that specifies a format for the time period in a date format style.
- [Date.FormatStyle.Symbol.Era](date/formatstyle/symbol/era.md)
  A type that specifies a format for the era in a date format style.
- [Date.FormatStyle.Symbol.Hour](date/formatstyle/symbol/hour.md)
  A type that specifies a format for the hour in a date format style.
- [Date.FormatStyle.Symbol.Minute](date/formatstyle/symbol/minute.md)
  A type that specifies the format for the minutes in a date format style.
- [Date.FormatStyle.Symbol.Month](date/formatstyle/symbol/month.md)
  A type that specifies a format for the month in a date format style.
- [Date.FormatStyle.Symbol.Quarter](date/formatstyle/symbol/quarter.md)
  A type that specifies the format for the quarter in a date format style.
- [Date.FormatStyle.Symbol.Second](date/formatstyle/symbol/second.md)
  A type that specifies the format for the seconds in a date format style.
- [Date.FormatStyle.Symbol.SecondFraction](date/formatstyle/symbol/secondfraction.md)
  A type that specifies the format for the second fraction in a date format style.
- [Date.FormatStyle.Symbol.StandaloneMonth](date/formatstyle/symbol/standalonemonth.md)
  A type that specifies the format for a standalone month.
- [Date.FormatStyle.Symbol.StandaloneQuarter](date/formatstyle/symbol/standalonequarter.md)
  A type that specifies the format for a standalone quarter.
- [Date.FormatStyle.Symbol.StandaloneWeekday](date/formatstyle/symbol/standaloneweekday.md)
  A type that specifies the format for a standalone weekday.
- [Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone.md)
  A type that specifies a format for the time zone in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/weekday)*