# init(date:time:locale:calendar:timeZone:capitalizationContext:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

## Discussion

Customize the date string by providing a date style, time style, locale, calendar, time zone, and capitalization scheme.

Date style values are [`complete`](./datestyle/complete.md), [`long`](./datestyle/long.md), `abbreviated`, [`numeric`](./datestyle/numeric.md), [`omitted`](./datestyle/omitted.md), or `none`. Time style values are [`complete`](./timestyle/complete.md), [`standard`](./timestyle/standard.md), [`shortened`](./timestyle/shortened.md), [`omitted`](./timestyle/omitted.md), or `none`.

## Parameters

- `date`: The [`Date.FormatStyle.DateStyle`](./datestyle.md) used to create the string representation of the date.
- `time`: The [`Date.FormatStyle.TimeStyle`](./timestyle.md) used to create the string representation of the date.
- `locale`: The [`Locale`](../../locale.md) used to create the string representation of the date.
- `calendar`: The [`Calendar`](../../calendar.md) used to create the string representation of the date.
- `timeZone`: The [`TimeZone`](../../timezone.md) used to create the string representation of the date.
- `capitalizationContext`: The [`FormatStyleCapitalizationContext`](../../formatstylecapitalizationcontext.md) used to create the string representation of the date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstyle/init(date:time:locale:calendar:timezone:capitalizationcontext:))*