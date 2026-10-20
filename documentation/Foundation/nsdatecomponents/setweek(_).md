# setWeek(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the number of weeks.

**Availability**:
- iOS 2.0+ - Deprecated in 7.0
- iPadOS 2.0+ - Deprecated in 7.0
- Mac Catalyst 2.0+ - Deprecated in 7.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`weekOfYear`](./weekofyear.md) or [`weekOfMonth`](./weekofmonth.md) instead, depending on what you intend.

## Declaration

```swift
func setWeek(_ v: Int)
```

```objc
- (void) setWeek:(NSInteger) v;
```

#### Discussion

This value is interpreted in the context of the calendar with which it is used—see [Calendars, Date Components, and Calendar Units](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/Articles/dtCalendars.html#//apple_ref/doc/uid/TP40003470) in [Date and Time Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DatesAndTimes/DatesAndTimes.html#//apple_ref/doc/uid/10000039i).

## Parameters

- `v`: The number of week units.

## See Also

### Accessing Weeks and Days
- [var weekday: Int](./weekday.md)
  The number of the weekdays.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatecomponents/setweek(_:))*