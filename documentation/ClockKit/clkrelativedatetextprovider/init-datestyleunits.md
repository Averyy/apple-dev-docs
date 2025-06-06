# init(date:style:units:)

**Framework**: ClockKit  
**Kind**: init

Creates a text provider that shows the difference between the current time and the specified date.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(date: Date, style: CLKRelativeDateStyle, units calendarUnits: NSCalendar.Unit)
```

#### Discussion

This initializer produces a text provider that updates automatically as time passes. To create a text provider that produces a static, relative date, use [`init(date:relativeTo:style:units:)`](clkrelativedatetextprovider/init(date:relativeto:style:units:).md) instead.

The text provider created by this method uses the default time zone information for the current user. The system formats date values according to the user’s current locale information.

## Parameters

- `date`: The date to use for calculations. This parameter must not be  .
- `style`: The style to use when formatting the relative date value. For a list of possible values, see  .
- `calendarUnits`: The units to include in the resulting date string. For a list of supported calendar units, see  .

## See Also

- [convenience init(date: Date, relativeTo: Date?, style: CLKRelativeDateStyle, units: NSCalendar.Unit)](clkrelativedatetextprovider/init(date:relativeto:style:units:).md)
  Creates a text provider that shows the difference in time between the provided dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/init(date:style:units:))*