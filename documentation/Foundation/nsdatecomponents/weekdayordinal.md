# weekdayOrdinal

**Framework**: Foundation  
**Kind**: property

The ordinal number of weekdays.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var weekdayOrdinal: Int { get set }
```

#### Discussion

Weekday ordinal units represent the position of the weekday within the next larger calendar unit, such as the month. For example,  is the weekday ordinal unit for the  Friday of the month.

This value is interpreted in the context of the calendar with which it is used—see [`Calendars, Date Components, and Calendar Units`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [`Date and Time Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

- [var weekday: Int](nsdatecomponents/weekday.md)
  The number of the weekdays.
- [var weekOfMonth: Int](nsdatecomponents/weekofmonth.md)
  The week number of the months.
- [var weekOfYear: Int](nsdatecomponents/weekofyear.md)
  The ISO 8601 week date of the year.
- [var day: Int](nsdatecomponents/day.md)
  The number of days.
- [func week() -> Int](nsdatecomponents/week.md)
  Returns the number of weeks.
- [func setWeek(Int)](nsdatecomponents/setweek(_:).md)
  Sets the number of weeks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/weekdayordinal)*