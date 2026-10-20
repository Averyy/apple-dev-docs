# Date.FormatStyle.Symbol.TimeZone

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that specifies a format for the time zone in a date format style.

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
struct TimeZone
```

#### Overview

The type [`Date.FormatStyle.Symbol.TimeZone`](./timezone.md) includes static factory variables and methods that create custom [`Date.FormatStyle.Symbol.TimeZone`](./timezone.md) objects:

| Factory variable | Description |
| --- | --- |
| [`specificName(_:)`](./timezone/specificname%28_%29.md) | The specific, non-location representation of a timezone. For example, `CDT` (`short`), `Central Daylight Time` (`long`). |
| [`genericName(_:)`](./timezone/genericname%28_%29.md) | The generic, non-location representation of a timezone. For example, `CT` (`short`), `Central Time` (`long`). |
| [`iso8601(_:)`](./timezone/iso8601%28_%29.md) | The ISO 8601 representation of the timezone with hours, minutes, and optional seconds. For example, `-0500` (`short`), `-05:00` (`long`). |
| [`localizedGMT(_:)`](./timezone/localizedgmt%28_%29.md) | The localized GMT format representation of a timezone. For example, `GMT-5` (`short`), `GMT-05:00` (`long`). |
| [`identifier(_:)`](./timezone/identifier%28_%29.md) | The timezone identifier. For example, `uschi` (`short`), `America/Chicago` (`long`). |
| [`exemplarLocation`](./timezone/exemplarlocation.md) | The exemplar city for a timezone. For example, `Chicago`. |
| [`genericLocation`](./timezone/genericlocation.md) | The generic location representation of a timezone. For example, `Chicago Time`. |

To customize the hour format in a string representation of a `Date`, use [`timeZone(_:)`](../timezone%28_%29.md). The following example shows a variety of [`Date.FormatStyle.Symbol.TimeZone`](./timezone.md) format styles applied to a date.

```swift
let meetingDate = Date() // Feb 9, 2021 at 7:00 PM

meetingDate.formatted(Date.FormatStyle().timeZone(.specificName(.short)))
// CDT
meetingDate.formatted(Date.FormatStyle().timeZone(.specificName(.long)))
// Central Daylight Time

meetingDate.formatted(Date.FormatStyle().timeZone(.genericName(.short)))
// CT
meetingDate.formatted(Date.FormatStyle().timeZone(.genericName(.long)))
// Central Time

meetingDate.formatted(Date.FormatStyle().timeZone(.iso8601(.short)))
// -0500
meetingDate.formatted(Date.FormatStyle().timeZone(.iso8601(.long)))
// -05:00

meetingDate.formatted(Date.FormatStyle().timeZone(.localizedGMT(.short)))
// GMT-5
meetingDate.formatted(Date.FormatStyle().timeZone(.localizedGMT(.long)))
// GMT-05:00

meetingDate.formatted(Date.FormatStyle().timeZone(.identifier(.short)))
// uschi
meetingDate.formatted(Date.FormatStyle().timeZone(.identifier(.long)))
// America/Chicago

meetingDate.formatted(Date.FormatStyle().timeZone(.exemplarLocation))
// Chicago

meetingDate.formatted(Date.FormatStyle().timeZone(.genericLocation))
// Chicago Time

```

If you don’t provide a format, the system formats a timezone using the short [`specificName(_:)`](./timezone/specificname%28_%29.md) static function with the width [`Date.FormatStyle.Symbol.TimeZone.Width.short`](./timezone/width/short.md).

For more information about formatting dates, see the [`Date.FormatStyle`](../../formatstyle.md).

## Topics

### Modifying a Time Zone
- [static func specificName(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](./timezone/specificname%28_%29.md)
  Returns the specific, non-location representation of a timezone.
- [static func genericName(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](./timezone/genericname%28_%29.md)
  Returns the generic, non-location representation of a timezone.
- [static func iso8601(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](./timezone/iso8601%28_%29.md)
  Creates the ISO 8601 representation of the timezone with hours, minutes, and optional seconds.
- [static func localizedGMT(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](./timezone/localizedgmt%28_%29.md)
  Returns the localized GMT format representation of a timezone.
- [static func identifier(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](./timezone/identifier%28_%29.md)
  Returns the timezone identifier.
- [static var exemplarLocation: Date.FormatStyle.Symbol.TimeZone](./timezone/exemplarlocation.md)
  The exemplar city for a timezone.
- [static var genericLocation: Date.FormatStyle.Symbol.TimeZone](./timezone/genericlocation.md)
  The generic location representation of a timezone.
### Comparing Time Zones
- [static func == (Date, Date) -> Bool](../../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.
### Supporting Enumerations
- [Date.FormatStyle.Symbol.TimeZone.Width](./timezone/width.md)
  A type representing the width of a timezone in a format style.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.TimeZone](./timezone/omitted.md)
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
- [Date.FormatStyle.Symbol.Hour](./hour.md)
  A type that specifies a format for the hour in a date format style.
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
- [Date.FormatStyle.Symbol.VerbatimHour](./verbatimhour.md)
  A type that specifies a format for the hour in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/timezone)*