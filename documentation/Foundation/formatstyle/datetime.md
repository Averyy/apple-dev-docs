# dateTime

**Framework**: Foundation  
**Kind**: property

A style for formatting a date and time.

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
static var dateTime: Date.FormatStyle { get }
```

#### Discussion

Use this type property when the call point allows the use of [`Date.FormatStyle`](date/formatstyle.md). You typically do this when calling the [`formatted(_:)`](date/formatted(_:).md) method of [`Date`](date.md).

Customize the date format style using modifier syntax to apply specific date and time formats. For example:

```swift
let meetingDate = Date()
let localeArray = ["en_US", "sv_SE", "en_GB", "th_TH", "fr_BE"]
let formattedDates = localeArray.map { localeID in
    meetingDate.formatted(.dateTime
                          .day(.twoDigits)
                          .month(.wide)
                          .weekday(.short)
                          .hour(.conversationalTwoDigits(amPM: .wide))
                          .locale(Locale(identifier: localeID)))
        } // ["Mo, July 31 at 05 PM", "må 31 juli 17", "Mo, 31 July at 17", "จ. 31 กรกฎาคม เวลา 17", "lu 31 juillet à 17 h"]
```

The default format styles provided are [`numeric`](date/formatstyle/datestyle/numeric.md) date format and [`shortened`](date/formatstyle/timestyle/shortened.md) time format. For example:

```swift
let meetingDate = Date()
let formatted = meetingDate.formatted(.dateTime) // "7/31/2023, 5:15 PM"
```

## See Also

- [struct FormatStyle](date/formatstyle.md)
  A structure that creates a locale-appropriate string representation of a date instance and converts strings of dates and times into date instances.
- [struct ISO8601FormatStyle](date/iso8601formatstyle.md)
  A type that converts between dates and their ISO-8601 string representations.
- [static func verbatim(Date.FormatString, locale: Locale?, timeZone: TimeZone, calendar: Calendar) -> Date.VerbatimFormatStyle](formatstyle/verbatim(_:locale:timezone:calendar:).md)
  Returns a style for formatting a date with an explicitly-specified style.
- [struct VerbatimFormatStyle](date/verbatimformatstyle.md)
  A style that formats a date with an explicitly-specified style.
- [static var interval: Date.IntervalFormatStyle](formatstyle/interval.md)
  A style for formatting a date interval.
- [struct IntervalFormatStyle](date/intervalformatstyle.md)
  A format style that creates string representations of date intervals.
- [static func relative(presentation: Date.RelativeFormatStyle.Presentation, unitsStyle: Date.RelativeFormatStyle.UnitsStyle) -> Self](formatstyle/relative(presentation:unitsstyle:).md)
  Returns a style for formatting a date as relative to the current date.
- [struct RelativeFormatStyle](date/relativeformatstyle.md)
  A format style that forms locale-aware string representations of a relative date or time.
- [static func components(style: Date.ComponentsFormatStyle.Style, fields: Set<Date.ComponentsFormatStyle.Field>?) -> Self](formatstyle/components(style:fields:).md)
  Returns a style for formatting a date interval in terms of specific date components.
- [struct ComponentsFormatStyle](date/componentsformatstyle.md)
  A style for formatting a date interval in terms of specific date components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/formatstyle/datetime)*