# Date.FormatStyle.Symbol.Era

**Framework**: Foundation  
**Kind**: struct

A type that specifies a format for the era in a date format style.

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
struct Era
```

#### Overview

The type [`Date.FormatStyle.Symbol.Era`](date/formatstyle/symbol/era.md) includes static factory variables that create custom [`Date.FormatStyle.Symbol.Era`](date/formatstyle/symbol/era.md) objects.

| Factory variable | Description |
| --- | --- |
| [`abbreviated`](date/formatstyle/symbol/era/abbreviated.md) | An abbreviated representation of an era. For example, `AD`, `BC`. |
| [`narrow`](date/formatstyle/symbol/era/narrow.md) | A narrow era representation. For example, `A`, `B`. |
| [`wide`](date/formatstyle/symbol/era/wide.md) | A full representation of an era. For example, `Anno Domini`, `Before Christ`. |

To customize the era format in a string representation of a `Date`, use [`era(_:)`](date/formatstyle/era(_:).md). The following example shows a variety of [`Date.FormatStyle.Symbol.Era`](date/formatstyle/symbol/era.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 3:00 PM
meetingDate.formatted(Date.FormatStyle().era(.abbreviated)) // AD
meetingDate.formatted(Date.FormatStyle().era(.narrow)) // A
meetingDate.formatted(Date.FormatStyle().era(.wide)) // Anno Domini
meetingDate.formatted(Date.FormatStyle().era()) // AD
```

If no format is specified as a parameter, the [`abbreviated`](date/formatstyle/symbol/era/abbreviated.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying an Era
- [static var abbreviated: Date.FormatStyle.Symbol.Era](date/formatstyle/symbol/era/abbreviated.md)
  An abbreviated representation of an era.
- [static var narrow: Date.FormatStyle.Symbol.Era](date/formatstyle/symbol/era/narrow.md)
  A narrow representation of an era.
- [static var wide: Date.FormatStyle.Symbol.Era](date/formatstyle/symbol/era/wide.md)
  A full representation of an era.
### Comparing an Era
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Era](date/formatstyle/symbol/era/omitted.md)

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
- [Date.FormatStyle.Symbol.VerbatimHour](date/formatstyle/symbol/verbatimhour.md)
  A type that specifies a format for the hour in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/era)*