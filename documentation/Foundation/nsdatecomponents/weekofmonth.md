# weekOfMonth

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The week number of the months.

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
var weekOfMonth: Int { get set }
```

```objc
@property NSInteger weekOfMonth;
```

#### Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Accessing Weeks and Days
- [var weekday: Int](./weekday.md)
  The number of the weekdays.
- [var weekdayOrdinal: Int](./weekdayordinal.md)
  The ordinal number of weekdays.
- [var weekOfYear: Int](./weekofyear.md)
  The ISO 8601 week date of the year.
- [var day: Int](./day.md)
  The number of days.
- [func week() -> Int](./week%28%29.md)
  Returns the number of weeks.
- [func setWeek(Int)](./setweek%28_%29.md)
  Sets the number of weeks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/weekofmonth)*