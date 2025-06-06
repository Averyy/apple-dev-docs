# startDate

**Framework**: ClockKit  
**Kind**: property

The start date for the time interval.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var startDate: Date { get set }
```

#### Discussion

The date in this property must come chronologically before the date in the [`endDate`](clktimeintervaltextprovider/enddate.md) property. This property must not be `nil`.

## See Also

- [convenience init(start: Date, end: Date, timeZone: TimeZone?)](clktimeintervaltextprovider/init(start:end:timezone:).md)
  Creates and returns a text provider with the specified dates and time zone information.
- [convenience init(start: Date, end: Date)](clktimeintervaltextprovider/init(start:end:).md)
  Creates and returns a text provider with the specified start and end dates.
- [var endDate: Date](clktimeintervaltextprovider/enddate.md)
  The end date for the time interval.
- [var timeZone: TimeZone?](clktimeintervaltextprovider/timezone.md)
  The time zone used to format time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/startdate)*