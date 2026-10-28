# timeZone

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The time zone used by the locale.

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
var timeZone: TimeZone?
```

## Discussion

Set this value to specify a time zone associated with the locale.

This property corresponds to the `tz` key of the Unicode BCP 47 extension.

## See Also

### Specifying date and time components
- [var calendar: Calendar.Identifier?](./calendar.md)
  The calendar used by the locale.
- [Calendar.Identifier](../../calendar/identifier-swift.enum.md)
  An enumeration for the available calendars.
- [var firstDayOfWeek: Locale.Weekday?](./firstdayofweek.md)
  The first day of the week as represented by this locale.
- [Locale.Weekday](../weekday.md)
  A type that represents weekdays, used for indicating a locale’s first day of the week.
- [var hourCycle: Locale.HourCycle?](./hourcycle.md)
  The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [Locale.HourCycle](../hourcycle-swift.enum.md)
  A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/components/timezone)*