# Date.FormatStyle.Symbol.TimeZone

**Framework**: Foundation  
**Kind**: struct

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

The type [`Date.FormatStyle.Symbol.TimeZone`](date/formatstyle/symbol/timezone.md) includes static factory variables and methods that create custom [`Date.FormatStyle.Symbol.TimeZone`](date/formatstyle/symbol/timezone.md) objects:

| Factory variable | Description |
| --- | --- |
| [`specificName(_:)`](date/formatstyle/symbol/timezone/specificname(_:).md) | The specific, non-location representation of a timezone. For example, `CDT` (`short`), `Central Daylight Time` (`long`). |
| [`genericName(_:)`](date/formatstyle/symbol/timezone/genericname(_:).md) | The generic, non-location representation of a timezone. For example, `CT` (`short`), `Central Time` (`long`). |
| [`iso8601(_:)`](date/formatstyle/symbol/timezone/iso8601(_:).md) | The ISO 8601 representation of the timezone with hours, minutes, and optional seconds. For example, `-0500` (`short`), `-05:00` (`long`). |
| [`localizedGMT(_:)`](date/formatstyle/symbol/timezone/localizedgmt(_:).md) | The localized GMT format representation of a timezone. For example, `GMT-5` (`short`), `GMT-05:00` (`long`). |
| [`identifier(_:)`](date/formatstyle/symbol/timezone/identifier(_:).md) | The timezone identifier. For example, `uschi` (`short`), `America/Chicago` (`long`). |
| [`exemplarLocation`](date/formatstyle/symbol/timezone/exemplarlocation.md) | The exemplar city for a timezone. For example, `Chicago`. |
| [`genericLocation`](date/formatstyle/symbol/timezone/genericlocation.md) | The generic location representation of a timezone. For example, `Chicago Time`. |

To customize the hour format in a string representation of a `Date`, use [`timeZone(_:)`](date/formatstyle/timezone(_:).md). The following example shows a variety of [`Date.FormatStyle.Symbol.TimeZone`](date/formatstyle/symbol/timezone.md) format styles applied to a date.

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

If you don’t provide a format, the system formats a timezone using the short [`specificName(_:)`](date/formatstyle/symbol/timezone/specificname(_:).md) static function with the width [`Date.FormatStyle.Symbol.TimeZone.Width.short`](date/formatstyle/symbol/timezone/width/short.md).

For more information about formatting dates, see the [`Date.FormatStyle`](date/formatstyle.md).

## Topics

### Modifying a Time Zone
- [static func specificName(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/specificname(_:).md)
  Returns the specific, non-location representation of a timezone.
- [static func genericName(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/genericname(_:).md)
  Returns the generic, non-location representation of a timezone.
- [static func iso8601(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/iso8601(_:).md)
  Creates the ISO 8601 representation of the timezone with hours, minutes, and optional seconds.
- [static func localizedGMT(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/localizedgmt(_:).md)
  Returns the localized GMT format representation of a timezone.
- [static func identifier(Date.FormatStyle.Symbol.TimeZone.Width) -> Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/identifier(_:).md)
  Returns the timezone identifier.
- [static var exemplarLocation: Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/exemplarlocation.md)
  The exemplar city for a timezone.
- [static var genericLocation: Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/genericlocation.md)
  The generic location representation of a timezone.
### Comparing Time Zones
- [static func != (Self, Self) -> Bool](date/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (Date, Date) -> Bool](date/==(_:_:).md)
  Returns true if the two `Date` values represent the same point in time.
### Supporting Enumerations
- [Date.FormatStyle.Symbol.TimeZone.Width](date/formatstyle/symbol/timezone/width.md)
  A type representing the width of a timezone in a format style.
### Type Properties
- [static let omitted: Date.FormatStyle.Symbol.TimeZone](date/formatstyle/symbol/timezone/omitted.md)

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
- [Date.FormatStyle.Symbol.VerbatimHour](date/formatstyle/symbol/verbatimhour.md)
  A type that specifies a format for the hour in a date format style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/symbol/timezone)*