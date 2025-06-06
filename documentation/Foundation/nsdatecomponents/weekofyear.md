# weekOfYear

**Framework**: Foundation  
**Kind**: property

The ISO 8601 week date of the year.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var weekOfYear: Int { get set }
```

#### Discussion

This value is interpreted in the context of the calendar with which it is used—see [`Calendars, Date Components, and Calendar Units`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [`Date and Time Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

- [var yearForWeekOfYear: Int](nsdatecomponents/yearforweekofyear.md)
  The ISO 8601 week-numbering year.
- [var weekday: Int](nsdatecomponents/weekday.md)
  The number of the weekdays.
- [var weekdayOrdinal: Int](nsdatecomponents/weekdayordinal.md)
  The ordinal number of weekdays.
- [var weekOfMonth: Int](nsdatecomponents/weekofmonth.md)
  The week number of the months.
- [var day: Int](nsdatecomponents/day.md)
  The number of days.
- [func week() -> Int](nsdatecomponents/week.md)
  Returns the number of weeks.
- [func setWeek(Int)](nsdatecomponents/setweek(_:).md)
  Sets the number of weeks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/weekofyear)*