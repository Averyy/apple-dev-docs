# locale

**Framework**: Foundation  
**Kind**: property

The locale to use when formatting date and time values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var locale: Locale! { get set }
```

#### Discussion

The default value of this property is the current user’s locale, which is accessible from the [`current`](nslocale/current.md) method of [`NSLocale`](nslocale.md). You can change this value to a different locale to generate strings based on that locale.

## See Also

- [var dateStyle: DateIntervalFormatter.Style](dateintervalformatter/datestyle.md)
  The style to use when formatting day, month, and year information.
- [var timeStyle: DateIntervalFormatter.Style](dateintervalformatter/timestyle.md)
  The style to use when formatting hour, minute, and second information.
- [var dateTemplate: String!](dateintervalformatter/datetemplate.md)
  The template for formatting one date and time value.
- [var calendar: Calendar!](dateintervalformatter/calendar.md)
  The calendar to use for date values.
- [var timeZone: TimeZone!](dateintervalformatter/timezone.md)
  The time zone with which to specify time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dateintervalformatter/locale)*