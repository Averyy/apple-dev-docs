# endDate

**Framework**: ClockKit  
**Kind**: property

The end date for the time interval.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var endDate: Date { get set }
```

#### Discussion

The date in this property must come chronologically after the date in the [`startDate`](clktimeintervaltextprovider/startdate.md) property. This property must not be `nil`.

## See Also

- [convenience init(start: Date, end: Date, timeZone: TimeZone?)](clktimeintervaltextprovider/init(start:end:timezone:).md)
  Creates and returns a text provider with the specified dates and time zone information.
- [convenience init(start: Date, end: Date)](clktimeintervaltextprovider/init(start:end:).md)
  Creates and returns a text provider with the specified start and end dates.
- [var startDate: Date](clktimeintervaltextprovider/startdate.md)
  The start date for the time interval.
- [var timeZone: TimeZone?](clktimeintervaltextprovider/timezone.md)
  The time zone used to format time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/enddate)*