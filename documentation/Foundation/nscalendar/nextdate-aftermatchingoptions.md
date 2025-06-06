# nextDate(after:matching:options:)

**Framework**: Foundation  
**Kind**: method

Returns the next date after a given date matching the given components.

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
func nextDate(after date: Date, matching comps: DateComponents, options: NSCalendar.Options = []) -> Date?
```

#### Return Value

A new `NSDate` object.

#### Discussion

To compute a sequence of dates, use the [`enumerateDates(startingAfter:matching:options:using:)`](nscalendar/enumeratedates(startingafter:matching:options:using:).md) method instead of calling this method in a loop with the previous loop iteration’s result.

## Parameters

- `date`: The date for which to perform the calculation.
- `comps`: The date components to match.
- `options`: Options for the calculation. For possible values, see  .

## See Also

- [func startOfDay(for: Date) -> Date](nscalendar/startofday(for:).md)
  Returns the first moment of a given date as a date instance.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, options: NSCalendar.Options, using: (Date?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nscalendar/enumeratedates(startingafter:matching:options:using:).md)
  Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matchingHour: Int, minute: Int, second: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matchinghour:minute:second:options:).md)
  Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [func nextDate(after: Date, matching: NSCalendar.Unit, value: Int, options: NSCalendar.Options) -> Date?](nscalendar/nextdate(after:matching:value:options:).md)
  Returns the next date after a given date matching the given calendar unit value.
- [NSCalendar.Options](nscalendar/options.md)
  The options for arithmetic operations involving calendars.
- [NSWrapCalendarComponents](nswrapcalendarcomponents-api.md)
  A legacy constant used to control overflow in date calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/nextdate(after:matching:options:))*