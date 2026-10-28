# Date.FormatStyle.Symbol.Hour

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that specifies a format for the hour in a date format style.

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
struct Hour
```

## Overview

The type [`Date.FormatStyle.Symbol.Hour`](./hour.md) includes static factory variables and methods that create custom [`Date.FormatStyle.Symbol.Hour`](./hour.md) objects:

| Factory variable | Description |
| --- | --- |
| [`defaultDigitsNoAMPM`](./hour/defaultdigitsnoampm.md) | The minimum number of digits that represents the full numeric hour. This doesn’t include the day period (a.m. or p.m.). For example, `1`, `11`. |
| [`twoDigitsNoAMPM`](./hour/twodigitsnoampm.md) | Two-digit numeric hour, zero-padded if necessary. This doesn’t include the day period (a.m. or p.m.). For example, `01`, `11`. |
| [`defaultDigits(amPM:)`](./hour/defaultdigits%28ampm%29.md) | The minimum number of digits that represents the full numeric hour. This may include the day period (a.m. or p.m.), depending on locale. For example, `7a` (`narrow`), `7AM` (`abbreviated`), `7A.M.` (`wide`). |
| [`twoDigits(amPM:)`](./hour/twodigits%28ampm%29.md) | Two-digit numeric hour, zero-padded if necessary. This may include the day period (a.m. or p.m.), depending on locale. For example, `07a` (`narrow`), `07AM` (`abbreviated`), `07A.M.` (`wide`). |
| [`conversationalDefaultDigits(amPM:)`](./hour/conversationaldefaultdigits%28ampm%29.md) | The minimum number of digits that represents the full numeric hour. This may include the day period (a.m. or p.m.), depending on locale, and can include conversational period formats. For example, `7a` (`narrow`), `7AM` (`abbreviated`), `7A.M.` (`wide`). |
| [`conversationalTwoDigits(amPM:)`](./hour/conversationaltwodigits%28ampm%29.md) | Two-digit numeric hour, zero-padded if necessary. This may include the day period (a.m. or p.m.), depending on locale, and can include conversational period formats. For example, `07a` (`narrow`), `07AM` (`abbreviated`), `07A.M.` (`wide`). |

To customize the hour format in a string representation of a `Date`, use [`hour(_:)`](../hour%28_%29.md) The example below shows a variety of [`Date.FormatStyle.Symbol.Hour`](./hour.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 7:00 PM
meetingDate.formatted(Date.FormatStyle().hour(.defaultDigitsNoAMPM)) 
// 7

meetingDate.formatted(Date.FormatStyle().hour(.twoDigitsNoAMPM)) 
// 07

meetingDate.formatted(Date.FormatStyle().hour(.defaultDigits(amPM: .narrow))) 
// 7p

meetingDate.formatted(Date.FormatStyle().hour(.twoDigits(amPM: .abbreviated))
// 07 PM

meetingDate.formatted(Date.FormatStyle().hour(.conversationalDefaultDigits(amPM: .wide))
// 7 P.M.
```

If no format is specified as a parameter, the [`defaultDigits`](./minute/defaultdigits.md) static variable is the default format.

For more information about formatting dates, see the [`Date.FormatStyle`](../../formatstyle.md).

## Topics

### Modifying an Hour
- [static var defaultDigitsNoAMPM: Date.FormatStyle.Symbol.Hour](./hour/defaultdigitsnoampm.md)
  Custom format style portraying the minimum number of digits that represents the numeric hour.
- [static var twoDigitsNoAMPM: Date.FormatStyle.Symbol.Hour](./hour/twodigitsnoampm.md)
  Custom format style portraying the numeric hour using two digits.
- [static func conversationalDefaultDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](./hour/conversationaldefaultdigits%28ampm%29.md)
  Custom format style portraying the minimum number of digits that represents the hour and locale-dependent conversational day period formats.
- [static func conversationalTwoDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](./hour/conversationaltwodigits%28ampm%29.md)
  Custom format style portraying two digits that represent the hour and locale-dependent conversational day period formats.
- [static func defaultDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](./hour/defaultdigits%28ampm%29.md)
  Custom format style portraying the minimum number of digits that represents the hour and locale-dependent day period formats.
- [static func twoDigits(amPM: Date.FormatStyle.Symbol.Hour.AMPMStyle) -> Date.FormatStyle.Symbol.Hour](./hour/twodigits%28ampm%29.md)
  Custom format style portraying two digits that represent the hour and locale-dependent day period formats.
### Supporting Structures
- [Date.FormatStyle.Symbol.Hour.AMPMStyle](./hour/ampmstyle.md)
  The format style of the string representation of the day period, before or after noon, in a date.
### Comparing an Hour
- [static func == (Date, Date) -> Bool](../../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.Hour](./hour/omitted.md)
  The option for not including the symbol in the formatted output.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Modifying Date Style Format Symbols
- [Date.FormatStyle.Symbol.CyclicYear](./cyclicyear.md)
  A type that specifies a format for a cyclic year in a date format style.
- [Date.FormatStyle.Symbol.Day](./day.md)
  A type that specifies the format for a day in a date format style.
- [Date.FormatStyle.Symbol.DayOfYear](./dayofyear.md)
  A type that specifies the format for the day of the year in a date format style.
- [Date.FormatStyle.Symbol.DayPeriod](./dayperiod.md)
  A type that specifies a format for the time period in a date format style.
- [Date.FormatStyle.Symbol.Era](./era.md)
  A type that specifies a format for the era in a date format style.
- [Date.FormatStyle.Symbol.Minute](./minute.md)
  A type that specifies the format for the minutes in a date format style.
- [Date.FormatStyle.Symbol.Month](./month.md)
  A type that specifies a format for the month in a date format style.
- [Date.FormatStyle.Symbol.Quarter](./quarter.md)
  A type that specifies the format for the quarter in a date format style.
- [Date.FormatStyle.Symbol.Second](./second.md)
  A type that specifies the format for the seconds in a date format style.
- [Date.FormatStyle.Symbol.SecondFraction](./secondfraction.md)
  A type that specifies the format for the second fraction in a date format style.
- [Date.FormatStyle.Symbol.StandaloneMonth](./standalonemonth.md)
  A type that specifies the format for a standalone month.
- [Date.FormatStyle.Symbol.StandaloneQuarter](./standalonequarter.md)
  A type that specifies the format for a standalone quarter.
- [Date.FormatStyle.Symbol.StandaloneWeekday](./standaloneweekday.md)
  A type that specifies the format for a standalone weekday.
- [Date.FormatStyle.Symbol.TimeZone](./timezone.md)
  A type that specifies a format for the time zone in a date format style.
- [Date.FormatStyle.Symbol.VerbatimHour](./verbatimhour.md)
  A type that specifies a format for the hour in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/hour)*