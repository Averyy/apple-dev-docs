# NSWrapCalendarComponents

**Framework**: Foundation

A legacy constant used to control overflow in date calculations.

#### Overview

> **Note**:  Use [`wrapComponents`](nscalendar/options/wrapcomponents.md) instead.

 Use [`wrapComponents`](nscalendar/options/wrapcomponents.md) instead.

## Topics

### Constants
- [var NSWrapCalendarComponents: Int](nswrapcalendarcomponents.md)
  Specifies that the components specified for an `NSDateComponents` object should be incremented and wrap around to zero/one on overflow, but should not cause higher units to be incremented.

## See Also

- [func startOfDay(for: Date) -> Date](nscalendar/startofday(for:).md)
  Returns the first moment of a given date as a date instance.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, options: NSCalendar.Options, using: (Date?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nscalendar/enumeratedates(startingafter:matching:options:using:).md)
  Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:options:).md)
  Returns the next date after a given date matching the given components.
- [func nextDate(after: Date, matchingHour: Int, minute: Int, second: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matchinghour:minute:second:options:).md)
  Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [func nextDate(after: Date, matching: NSCalendar.Unit, value: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:value:options:).md)
  Returns the next date after a given date matching the given calendar unit value.
- [NSCalendar.Options](nscalendar/options.md)
  The options for arithmetic operations involving calendars.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nswrapcalendarcomponents-api)*