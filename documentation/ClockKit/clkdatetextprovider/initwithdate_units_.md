# initWithDate:units:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Creates and returns a text provider with the specified date and the default time zone.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithDate:(NSDate *) date units:(NSCalendarUnit) calendarUnits;
```

## Return Value

A text provider initialized with the specified date and time zone information.

## Discussion

The text provider created by this method uses the default time zone information for the current user. Date values are formatted according to the user’s current locale information.

## Parameters

- `date`: The date to display. This parameter must not be `nil`.
- `calendarUnits`: The units to include in the resulting date string. For a list of supported calendar units, see [Date Format Options](../clkdatetextprovider.md#Date-Format-Options).

## See Also

### Creating a Text Provider
- [convenience init(date: Date, units: NSCalendar.Unit)](./init%28date,units%29.md)
  Creates and returns a text provider with the specified date and the default time zone.
- [convenience init(date: Date, units: NSCalendar.Unit, timeZone: TimeZone?)](./init%28date,units,timezone%29.md)
  Creates and returns a text provider with the specified date and time zone.
- [- initWithDate:units:timeZone:](./initwithdate_units_timezone_.md)
  Creates and returns a text provider with the specified date and time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/initwithdate:units:)*