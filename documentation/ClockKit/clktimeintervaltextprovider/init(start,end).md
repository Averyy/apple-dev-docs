# init(start:end:)

**Framework**: ClockKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a text provider with the specified start and end dates.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
convenience init(start startDate: Date, end endDate: Date)
```

```objc
+ (instancetype) textProviderWithStartDate:(NSDate *) startDate endDate:(NSDate *) endDate;
```

#### Return Value

A text provider initialized with the specified start and end dates.

#### Discussion

The returned text provider uses the default calendar and time zone information for the current user. Date and time values are formatted according to the user’s current locale information.

## Parameters

- `startDate`: The start date for the time range. This parameter must not be `nil`.
- `endDate`: The end date for the time range. The specified date must come after the date in the `startDate` parameter. This parameter must not be `nil`.

## See Also

### Creating the Text Provider
- [convenience init(start: Date, end: Date, timeZone: TimeZone?)](./init%28start,end,timezone%29.md)
  Creates and returns a text provider with the specified dates and time zone information.
- [- initWithStartDate:endDate:](./initwithstartdate_enddate_.md)
  Creates and returns a text provider with the specified start and end dates.
- [- initWithStartDate:endDate:timeZone:](./initwithstartdate_enddate_timezone_.md)
  Creates and returns a text provider with the specified dates and time zone information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/init(start:end:))*