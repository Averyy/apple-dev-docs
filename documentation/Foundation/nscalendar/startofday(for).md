# startOfDay(for:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the first moment of a given date as a date instance.

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
func startOfDay(for date: Date) -> Date
```

```objc
- (NSDate *) startOfDayForDate:(NSDate *) date;
```

## Return Value

An `NSDate` instance representing the first moment date of the given date.

## Discussion

For example, passing `[NSDate date]` for the `date` parameter would give you the start of “today.”

### Special Considerations

If there were two midnights, this method returns the first. If there was none, it returns the first moment that did exist.

## Parameters

- `date`: The date for which to perform the calculation.

## See Also

### Scanning Dates
- [func enumerateDates(startingAfter: Date, matching: DateComponents, options: NSCalendar.Options, using: (Date?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratedates%28startingafter,matching,options,using%29.md)
  Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, options: NSCalendar.Options) -> Date?](./nextdate%28after,matching,options%29.md)
  Returns the next date after a given date matching the given components.
- [func nextDate(after: Date, matchingHour: Int, minute: Int, second: Int, options: NSCalendar.Options) -> Date?](./nextdate%28after,matchinghour,minute,second,options%29.md)
  Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [func nextDate(after: Date, matching: NSCalendar.Unit, value: Int, options: NSCalendar.Options) -> Date?](./nextdate%28after,matching,value,options%29.md)
  Returns the next date after a given date matching the given calendar unit value.
- [NSCalendar.Options](./options.md)
  The options for arithmetic operations involving calendars.
- [NSWrapCalendarComponents](../nswrapcalendarcomponents-api.md)
  A legacy constant used to control overflow in date calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/startofday(for:))*