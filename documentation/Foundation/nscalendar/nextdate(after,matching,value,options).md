# nextDate(after:matching:value:options:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the next date after a given date matching the given calendar unit value.

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
func nextDate(after date: Date, matching unit: NSCalendar.Unit, value: Int, options: NSCalendar.Options = []) -> Date?
```

```objc
- (NSDate *) nextDateAfterDate:(NSDate *) date matchingUnit:(NSCalendarUnit) unit value:(NSInteger) value options:(NSCalendarOptions) options;
```

## Return Value

A new `NSDate` object.

## Parameters

- `date`: The date for which to perform the calculation.
- `unit`: The component to use. For possible values, see [`NSCalendar.Unit`](./unit.md).
- `value`: The value for the given component.
- `options`: Options for the calculation. For possible values, see [`NSCalendar.Options`](./options.md).

## See Also

### Scanning Dates
- [func startOfDay(for: Date) -> Date](./startofday%28for%29.md)
  Returns the first moment of a given date as a date instance.
- [func enumerateDates(startingAfter: Date, matching: DateComponents, options: NSCalendar.Options, using: (Date?, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratedates%28startingafter,matching,options,using%29.md)
  Computes the dates that match (or most closely match) a given set of components, and calls the block once for each of them, until the enumeration is stopped.
- [func nextDate(after: Date, matching: DateComponents, options: NSCalendar.Options) -> Date?](./nextdate%28after,matching,options%29.md)
  Returns the next date after a given date matching the given components.
- [func nextDate(after: Date, matchingHour: Int, minute: Int, second: Int, options: NSCalendar.Options) -> Date?](./nextdate%28after,matchinghour,minute,second,options%29.md)
  Returns the next date after a given date that matches the given hour, minute, and second, component values.
- [NSCalendar.Options](./options.md)
  The options for arithmetic operations involving calendars.
- [NSWrapCalendarComponents](../nswrapcalendarcomponents-api.md)
  A legacy constant used to control overflow in date calculations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/nextdate(after:matching:value:options:))*