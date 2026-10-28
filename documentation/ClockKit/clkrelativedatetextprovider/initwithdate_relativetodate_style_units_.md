# initWithDate:relativeToDate:style:units:

**Framework**: ClockKit  
**Kind**: method  
**Role**: Instance Method

Creates a text provider that shows the difference in time between the provided dates.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```objc
- (instancetype) initWithDate:(NSDate *) date relativeToDate:(NSDate *) relativeDate style:(CLKRelativeDateStyle) style units:(NSCalendarUnit) calendarUnits;
```

## Discussion

This initializer creates a text provider that produces a fixed, relative date. If you want a text provider that automatically updates as time passes, use [`init(date:style:units:)`](./init%28date,style,units%29.md) instead.

## Parameters

- `date`: The starting date, used to calculate the relative date string.
- `relativeDate`: The end date, used to calculate the relative date string.
- `style`: The style to use when formatting the relative date value. For a list of possible values, see [`CLKRelativeDateStyle`](../clkrelativedatestyle.md).
- `calendarUnits`: The units to include in the resulting date string. For a list of supported calendar units, see [Date Format Options](../clkrelativedatetextprovider.md#Date-Format-Options).

## See Also

### Creating a Text Provider
- [convenience init(date: Date, style: CLKRelativeDateStyle, units: NSCalendar.Unit)](./init%28date,style,units%29.md)
  Creates a text provider that shows the difference between the current time and the specified date.
- [- initWithDate:style:units:](./initwithdate_style_units_.md)
  Creates a text provider that shows the difference between the current time and the specified date.
- [convenience init(date: Date, relativeTo: Date?, style: CLKRelativeDateStyle, units: NSCalendar.Unit)](./init%28date,relativeto,style,units%29.md)
  Creates a text provider that shows the difference in time between the provided dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/initwithdate:relativetodate:style:units:)*