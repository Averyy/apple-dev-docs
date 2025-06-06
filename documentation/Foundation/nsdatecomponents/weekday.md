# weekday

**Framework**: Foundation  
**Kind**: property

The number of the weekdays.

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
var weekday: Int { get set }
```

#### Discussion

Weekday units are the numbers 1 through , where  is the number of days in the week. For example, in the Gregorian calendar,  is 7 and Sunday is represented by 1.

This value is interpreted in the context of the calendar with which it is used—see [`Calendars, Date Components, and Calendar Units`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [`Date and Time Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

- [var weekdayOrdinal: Int](nsdatecomponents/weekdayordinal.md)
  The ordinal number of weekdays.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/weekday)*