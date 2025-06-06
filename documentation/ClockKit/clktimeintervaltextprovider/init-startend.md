# init(start:end:)

**Framework**: ClockKit  
**Kind**: init

Creates and returns a text provider with the specified start and end dates.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
convenience init(start startDate: Date, end endDate: Date)
```

#### Return Value

A text provider initialized with the specified start and end dates.

#### Discussion

The returned text provider uses the default calendar and time zone information for the current user. Date and time values are formatted according to the user’s current locale information.

## Parameters

- `startDate`: The start date for the time range. This parameter must not be  .
- `endDate`: The end date for the time range. The specified date must come after the date in the   parameter. This parameter must not be  .

## See Also

- [convenience init(start: Date, end: Date, timeZone: TimeZone?)](clktimeintervaltextprovider/init(start:end:timezone:).md)
  Creates and returns a text provider with the specified dates and time zone information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/init(start:end:))*