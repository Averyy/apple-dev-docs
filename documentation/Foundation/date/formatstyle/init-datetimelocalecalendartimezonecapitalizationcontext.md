# init(date:time:locale:calendar:timeZone:capitalizationContext:)

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
init(date: Date.FormatStyle.DateStyle? = nil, time: Date.FormatStyle.TimeStyle? = nil, locale: Locale = .autoupdatingCurrent, calendar: Calendar = .autoupdatingCurrent, timeZone: TimeZone = .autoupdatingCurrent, capitalizationContext: FormatStyleCapitalizationContext = .unknown)
```

#### Discussion

Customize the date string by providing a date style, time style, locale, calendar, time zone, and capitalization scheme.

Date style values are [`complete`](date/formatstyle/datestyle/complete.md), [`long`](date/formatstyle/datestyle/long.md), `abbreviated`, [`numeric`](date/formatstyle/datestyle/numeric.md), [`omitted`](date/formatstyle/datestyle/omitted.md), or `none`. Time style values are [`complete`](date/formatstyle/timestyle/complete.md), [`standard`](date/formatstyle/timestyle/standard.md), [`shortened`](date/formatstyle/timestyle/shortened.md), [`omitted`](date/formatstyle/timestyle/omitted.md), or `none`.

## Parameters

- `date`: The   used to create the string representation of the date.
- `time`: The   used to create the string representation of the date.
- `locale`: The   used to create the string representation of the date.
- `calendar`: The   used to create the string representation of the date.
- `timeZone`: The   used to create the string representation of the date.
- `capitalizationContext`: The   used to create the string representation of the date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/init(date:time:locale:calendar:timezone:capitalizationcontext:))*