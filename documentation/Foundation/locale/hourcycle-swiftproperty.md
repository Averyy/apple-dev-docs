# hourCycle

**Framework**: Foundation  
**Kind**: property

The hour cycle used by the locale, like one-to-twelve or zero-to-twenty-three.

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
var hourCycle: Locale.HourCycle { get }
```

#### Discussion

When called on the special [`Locale`](locale.md) instances [`current`](locale/current.md) or [`autoupdatingCurrent`](locale/autoupdatingcurrent.md), if the user overrode the default hour cycle, this property provides the user’s preference.

This property corresponds to the `hc` key of the Unicode BCP 47 extension.

For locale instances created with the `hc` specifier (such as `en-US@hc=h23`), or with a custom [`Locale.Components`](locale/components.md), this property represents the custom hour cycle. Otherwise, it represents the locale’s default hour cycle.

## See Also

- [var firstDayOfWeek: Locale.Weekday](locale/firstdayofweek.md)
  The first day of the week as represented by this locale.
- [Locale.Weekday](locale/weekday.md)
  A type that represents weekdays, used for indicating a locale’s first day of the week.
- [Locale.HourCycle](locale/hourcycle-swift.enum.md)
  A type that represents the hour cycle used in a locale, like one-to-twelve or zero-to-twenty-three.
- [var timeZone: TimeZone?](locale/timezone.md)
  The time zone associated with the locale, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/hourcycle-swift.property)*