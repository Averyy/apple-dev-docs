# startDate

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The start date for the time interval.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var startDate: Date { get set }
```

```objc
@property (nonatomic, retain) NSDate * startDate;
```

#### Discussion

The date in this property must come chronologically before the date in the [`endDate`](./enddate.md) property. This property must not be `nil`.

## See Also

### Related Documentation
- [convenience init(start: Date, end: Date, timeZone: TimeZone?)](./init%28start,end,timezone%29.md)
  Creates and returns a text provider with the specified dates and time zone information.
- [convenience init(start: Date, end: Date)](./init%28start,end%29.md)
  Creates and returns a text provider with the specified start and end dates.
### Getting the Time Information
- [var endDate: Date](./enddate.md)
  The end date for the time interval.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone used to format time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/startdate)*