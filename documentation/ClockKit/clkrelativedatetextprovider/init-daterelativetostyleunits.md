# init(date:relativeTo:style:units:)

**Framework**: ClockKit  
**Kind**: init

Creates a text provider that shows the difference in time between the provided dates.

**Availability**:
- watchOS 7.0+

## Declaration

```swift
convenience init(date: Date, relativeTo relativeToDate: Date?, style: CLKRelativeDateStyle, units calendarUnits: NSCalendar.Unit)
```

#### Discussion

This initializer creates a text provider that produces a fixed, relative date. If you want a text provider that automatically updates as time passes, use [`init(date:style:units:)`](clkrelativedatetextprovider/init(date:style:units:).md) instead.

## Parameters

- `date`: The starting date, used to calculate the relative date string.
- `relativeToDate`: The end date, used to calculate the relative date string.
- `style`: The style to use when formatting the relative date value. For a list of possible values, see  .
- `calendarUnits`: The units to include in the resulting date string. For a list of supported calendar units, see  .

## See Also

- [convenience init(date: Date, style: CLKRelativeDateStyle, units: NSCalendar.Unit)](clkrelativedatetextprovider/init(date:style:units:).md)
  Creates a text provider that shows the difference between the current time and the specified date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/init(date:relativeto:style:units:))*