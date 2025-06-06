# firstWeekday

**Framework**: Foundation  
**Kind**: property

The first day of the week for the calendar.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var firstWeekday: Int { get set }
```

#### Discussion

The default value of [`firstWeekday`](calendar/firstweekday.md) varies by calendar and locale. Your app can reset this value.

The weekday units are one-based. For Gregorian and ISO 8601 calendars, `1` is Sunday.

## See Also

- [var identifier: Calendar.Identifier](calendar/identifier-swift.property.md)
  The identifier of the calendar.
- [var locale: Locale?](calendar/locale.md)
  The locale of the calendar.
- [var minimumDaysInFirstWeek: Int](calendar/minimumdaysinfirstweek.md)
  The number of minimum days in the first week.
- [var timeZone: TimeZone](calendar/timezone.md)
  The time zone of the calendar.
- [func maximumRange(of: Calendar.Component) -> Range<Int>?](calendar/maximumrange(of:).md)
  The maximum range limits of the values that a given component can take on.
- [func minimumRange(of: Calendar.Component) -> Range<Int>?](calendar/minimumrange(of:).md)
  Returns the minimum range limits of the values that a given component can take on.
- [func ordinality(of: Calendar.Component, in: Calendar.Component, for: Date) -> Int?](calendar/ordinality(of:in:for:).md)
  Returns, for a given absolute time, the ordinal number of a smaller calendar component (such as a day) within a specified larger calendar component (such as a week).
- [func range(of: Calendar.Component, in: Calendar.Component, for: Date) -> Range<Int>?](calendar/range(of:in:for:).md)
  Returns the range of absolute time values that a smaller calendar component (such as a day) can take on in a larger calendar component (such as a month) that includes a specified absolute time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/calendar/firstweekday)*