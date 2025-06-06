# nextDate(after:matchingHour:minute:second:options:)

**Framework**: Foundation  
**Kind**: method

Returns the next date after a given date that matches the given hour, minute, and second, component values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func nextDate(after date: Date, matchingHour hourValue: Int, minute minuteValue: Int, second secondValue: Int, options: NSCalendar.Options = []) -> Date?
```

#### Return Value

A new `NSDate` object.

## Parameters

- `date`: The date for which to perform the calculation.
- `hourValue`: The value for the hour component.
- `minuteValue`: The value for the minute component.
- `secondValue`: The value for the second component.
- `options`: Options for the calculation. For possible values, see  .

## See Also

- [func startOfDay(for: Date) -> Date](nscalendar/startofday(for:).md)
  Returns the first moment of a given date as a date instance.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, options: NSCalendar.Options, using: (Date?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nscalendar/enumeratedates(startingafter:matching:options:using:).md)
  Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:options:).md)
  Returns the next date after a given date matching the given components.
- [func nextDate(after: Date, matching: NSCalendar.Unit, value: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:value:options:).md)
  Returns the next date after a given date matching the given calendar unit value.
- [NSCalendar.Options](nscalendar/options.md)
  The options for arithmetic operations involving calendars.
- [NSWrapCalendarComponents](nswrapcalendarcomponents-api.md)
  A legacy constant used to control overflow in date calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/nextdate(after:matchinghour:minute:second:options:))*