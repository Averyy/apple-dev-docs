# initWithDate:style:units:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Creates a text provider that shows the difference between the current time and the specified date.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithDate:(NSDate *) date style:(CLKRelativeDateStyle) style units:(NSCalendarUnit) calendarUnits;
```

#### Discussion

This initializer produces a text provider that updates automatically as time passes. To create a text provider that produces a static, relative date, use [`init(date:relativeTo:style:units:)`](./init%28date,relativeto,style,units%29.md) instead.

The text provider created by this method uses the default time zone information for the current user. The system formats date values according to the user’s current locale information.

## Parameters

- `date`: The date to use for calculations. This parameter must not be `nil`.
- `style`: The style to use when formatting the relative date value. For a list of possible values, see [`CLKRelativeDateStyle`](../clkrelativedatestyle.md).
- `calendarUnits`: The units to include in the resulting date string. For a list of supported calendar units, see [Date Format Options](../clkrelativedatetextprovider.md#Date-Format-Options).

## See Also

### Creating a Text Provider
- [convenience init(date: Date, style: CLKRelativeDateStyle, units: NSCalendar.Unit)](./init%28date,style,units%29.md)
  Creates a text provider that shows the difference between the current time and the specified date.
- [convenience init(date: Date, relativeTo: Date?, style: CLKRelativeDateStyle, units: NSCalendar.Unit)](./init%28date,relativeto,style,units%29.md)
  Creates a text provider that shows the difference in time between the provided dates.
- [- initWithDate:relativeToDate:style:units:](./initwithdate_relativetodate_style_units_.md)
  Creates a text provider that shows the difference in time between the provided dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/initwithdate:style:units:)*