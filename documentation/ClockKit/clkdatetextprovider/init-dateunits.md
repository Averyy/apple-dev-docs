# init(date:units:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a text provider with the specified date and the default time zone.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(date: Date, units calendarUnits: NSCalendar.Unit)
```

#### Return Value

A text provider initialized with the specified date and time zone information.

#### Discussion

The text provider created by this method uses the default time zone information for the current user. Date values are formatted according to the user’s current locale information.

## Parameters

- `date`: The date to display. This parameter must not be  .
- `calendarUnits`: The units to include in the resulting date string. For a list of supported calendar units, see  .

## See Also

- [convenience init(date: Date, units: NSCalendar.Unit, timeZone: TimeZone?)](clkdatetextprovider/init(date:units:timezone:).md)
  Creates and returns a text provider with the specified date and time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/init(date:units:))*