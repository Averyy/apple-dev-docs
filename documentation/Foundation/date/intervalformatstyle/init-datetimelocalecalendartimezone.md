# init(date:time:locale:calendar:timeZone:)

**Framework**: Foundation  
**Kind**: init

Creates an instance using the provided date, time, locale, calendar, time zone, and capitalization context.

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
init(date: Date.IntervalFormatStyle.DateStyle? = nil, time: Date.IntervalFormatStyle.TimeStyle? = nil, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, timeZone: TimeZone = .autoupdatingCurrent)
```

#### Discussion

Customize the date interval string by providing a date style, time style, locale, calendar, time zone, and capitalization scheme.

Values for date style are [`complete`](date/formatstyle/datestyle/complete.md), [`long`](date/formatstyle/datestyle/long.md), [`abbreviated`](date/formatstyle/datestyle/abbreviated.md), [`numeric`](date/formatstyle/datestyle/numeric.md), [`omitted`](date/formatstyle/datestyle/omitted.md), or `none`. Time style values are [`complete`](date/formatstyle/timestyle/complete.md), [`standard`](date/formatstyle/timestyle/standard.md), [`shortened`](date/formatstyle/timestyle/shortened.md), [`omitted`](date/formatstyle/timestyle/omitted.md), or `none`.

## Parameters

- `date`: The   for creating the string representation of the date interval.
- `time`: The   for creating the string representation of the date interval.
- `locale`: The   for creating the string representation of the date interval.
- `calendar`: The   for creating the string representation of the date interval.
- `timeZone`: The   for creating the string representation of the date interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/intervalformatstyle/init(date:time:locale:calendar:timezone:))*