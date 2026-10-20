# weekOfYear

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property NSInteger weekOfYear;
```

#### Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## See Also

### Related Documentation
- [var yearForWeekOfYear: Int](./yearforweekofyear.md)
  The ISO 8601 week-numbering year.
### Accessing Weeks and Days
- [var weekday: Int](./weekday.md)
  The number of the weekdays.
- [var weekdayOrdinal: Int](./weekdayordinal.md)
  The ordinal number of weekdays.
- [var weekOfMonth: Int](./weekofmonth.md)
  The week number of the months.
- [var day: Int](./day.md)
  The number of days.
- [func week() -> Int](./week%28%29.md)
  Returns the number of weeks.
- [func setWeek(Int)](./setweek%28_%29.md)
  Sets the number of weeks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/weekofyear)*