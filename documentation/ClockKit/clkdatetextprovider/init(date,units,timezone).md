# init(date:units:timeZone:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a text provider with the specified date and time zone.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(date: Date, units calendarUnits: NSCalendar.Unit, timeZone: TimeZone?)
```

```objc
+ (instancetype) textProviderWithDate:(NSDate *) date units:(NSCalendarUnit) calendarUnits timeZone:(NSTimeZone *) timeZone;
```

## Return Value

A text provider initialized with the specified date and time zone information.

## Discussion

Date values are formatted according to the user’s current locale information.

## Parameters

- `date`: The date to display. This parameter must not be `nil`.
- `calendarUnits`: The units to include in the resulting date string. For a list of supported calendar units, see [Date Format Options](../clkdatetextprovider.md#Date-Format-Options).
- `timeZone`: The time zone to use when formatting the date. If you specify `nil`, the text provider uses the time zone currently associated with the user.

## See Also

### Creating a Text Provider
- [convenience init(date: Date, units: NSCalendar.Unit)](./init%28date,units%29.md)
  Creates and returns a text provider with the specified date and the default time zone.
- [- initWithDate:units:](./initwithdate_units_.md)
  Creates and returns a text provider with the specified date and the default time zone.
- [- initWithDate:units:timeZone:](./initwithdate_units_timezone_.md)
  Creates and returns a text provider with the specified date and time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/init(date:units:timezone:))*