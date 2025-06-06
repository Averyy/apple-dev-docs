# firstDayOfWeek

**Framework**: Foundation  
**Kind**: property

The first day of the week as represented by this locale.

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
var firstDayOfWeek: Locale.Weekday { get }
```

#### Discussion

This value is the preferred first day of the week to show in a calendar view. It isn’t necessarily the same as the first day after the weekend; don’t try to determine a first-day-of-week value from weekend information.

This property corresponds to the `fw` key of the Unicode BCP 47 extension.

For locale instances created with the `fw` specifier (such as `en-US@fw=mon`), or with a custom [`Locale.Components`](locale/components.md), this property represents the custom day. Otherwise, it represents the locale’s default first day of the week.

## See Also

- [Locale.Weekday](locale/weekday.md)
  A type that represents weekdays, used for indicating a locale’s first day of the week.
- [var hourCycle: Locale.HourCycle](locale/hourcycle-swift.property.md)
  The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.
- [Locale.HourCycle](locale/hourcycle-swift.enum.md)
  A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [var timeZone: TimeZone?](locale/timezone.md)
  The time zone associated with the locale, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/firstdayofweek)*