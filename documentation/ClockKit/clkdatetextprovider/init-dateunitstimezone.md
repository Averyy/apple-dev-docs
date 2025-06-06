# init(date:units:timeZone:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a text provider with the specified date and time zone.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(date: Date, units calendarUnits: NSCalendar.Unit, timeZone: TimeZone?)
```

#### Return Value

A text provider initialized with the specified date and time zone information.

#### Discussion

Date values are formatted according to the user’s current locale information.

## Parameters

- `date`: The date to display. This parameter must not be  .
- `calendarUnits`: The units to include in the resulting date string. For a list of supported calendar units, see  .
- `timeZone`: The time zone to use when formatting the date. If you specify  , the text provider uses the time zone currently associated with the user.

## See Also

- [convenience init(date: Date, units: NSCalendar.Unit)](clkdatetextprovider/init(date:units:).md)
  Creates and returns a text provider with the specified date and the default time zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/init(date:units:timezone:))*