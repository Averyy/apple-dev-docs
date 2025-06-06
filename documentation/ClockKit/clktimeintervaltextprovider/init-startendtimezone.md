# init(start:end:timeZone:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a text provider with the specified dates and time zone information.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(start startDate: Date, end endDate: Date, timeZone: TimeZone?)
```

#### Return Value

A text provider initialized with the specified date and time zone values.

#### Discussion

The returned text provider uses the default calendar information for the current user and uses the time zone in the `timeZone` parameter. Date and time values are formatted according to the user’s current locale information.

## Parameters

- `startDate`: The start date for the time range. This parameter must not be  .
- `endDate`: The end date for the time range. The specified date must come after the date in the   parameter. This parameter must not be  .
- `timeZone`: The time zone to use when formatting dates. If you specify  , the text provider uses the time zone currently associated with the user.

## See Also

- [convenience init(start: Date, end: Date)](clktimeintervaltextprovider/init(start:end:).md)
  Creates and returns a text provider with the specified start and end dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/init(start:end:timezone:))*