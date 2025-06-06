# timeZone

**Framework**: ClockKit  
**Kind**: property

The time zone used to format time values.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

#### Discussion

If the value is `nil`, the text provider uses the time zone currently configured for the user.

## See Also

- [convenience init(start: Date, end: Date, timeZone: TimeZone?)](clktimeintervaltextprovider/init(start:end:timezone:).md)
  Creates and returns a text provider with the specified dates and time zone information.
- [var startDate: Date](clktimeintervaltextprovider/startdate.md)
  The start date for the time interval.
- [var endDate: Date](clktimeintervaltextprovider/enddate.md)
  The end date for the time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/timezone)*