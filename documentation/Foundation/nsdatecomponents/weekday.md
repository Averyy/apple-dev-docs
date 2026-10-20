# weekday

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property NSInteger weekday;
```

#### Discussion

Weekday units are the numbers 1 through *n*, where *n* is the number of days in the week. For example, in the Gregorian calendar, *n* is 7 and Sunday is represented by 1.

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Weeks and Days
- [var weekdayOrdinal: Int](./weekdayordinal.md)
  The ordinal number of weekdays.
- [var weekOfMonth: Int](./weekofmonth.md)
  The week number of the months.
- [var weekOfYear: Int](./weekofyear.md)
  The ISO 8601 week date of the year.
- [var day: Int](./day.md)
  The number of days.
- [func week() -> Int](./week%28%29.md)
  Returns the number of weeks.
- [func setWeek(Int)](./setweek%28_%29.md)
  Sets the number of weeks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/weekday)*