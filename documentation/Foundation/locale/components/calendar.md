# calendar

**Framework**: Foundation  
**Kind**: property

The calendar used by the locale.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var calendar: Calendar.Identifier?
```

#### Discussion

Set this property to override the locale’s default calendar. To request the default calendar used by the locale, use the [`Locale`](locale.md) property [`calendar`](locale/calendar.md).

This property corresponds to the `ca` key of the Unicode BCP 47 extension.

## See Also

- [Calendar.Identifier](calendar/identifier-swift.enum.md)
  An enumeration for the available calendars.
- [var firstDayOfWeek: Locale.Weekday?](locale/components/firstdayofweek.md)
  The first day of the week as represented by this locale.
- [Locale.Weekday](locale/weekday.md)
  A type that represents weekdays, used for indicating a locale’s first day of the week.
- [var hourCycle: Locale.HourCycle?](locale/components/hourcycle.md)
  The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [Locale.HourCycle](locale/hourcycle-swift.enum.md)
  A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [var timeZone: TimeZone?](locale/components/timezone.md)
  The time zone used by the locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/components/calendar)*