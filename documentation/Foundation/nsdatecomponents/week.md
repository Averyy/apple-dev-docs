# week()

**Framework**: Foundation  
**Kind**: method

Returns the number of weeks.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func week() -> Int
```

#### Return Value

The number of week units for the receiver.

#### Discussion

This value is interpreted in the context of the calendar with which it is used—see [`Calendars, Date Components, and Calendar Units`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [`Date and Time Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

- [var weekday: Int](nsdatecomponents/weekday.md)
  The number of the weekdays.
- [var weekdayOrdinal: Int](nsdatecomponents/weekdayordinal.md)
  The ordinal number of weekdays.
- [var weekOfMonth: Int](nsdatecomponents/weekofmonth.md)
  The week number of the months.
- [var weekOfYear: Int](nsdatecomponents/weekofyear.md)
  The ISO 8601 week date of the year.
- [var day: Int](nsdatecomponents/day.md)
  The number of days.
- [func setWeek(Int)](nsdatecomponents/setweek(_:).md)
  Sets the number of weeks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/week())*