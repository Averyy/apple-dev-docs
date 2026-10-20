# endDate

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The end date for the time interval.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var endDate: Date { get set }
```

```objc
@property (nonatomic, retain) NSDate * endDate;
```

#### Discussion

The date in this property must come chronologically after the date in the [`startDate`](./startdate.md) property. This property must not be `nil`.

## See Also

### Related Documentation
- [convenience init(start: Date, end: Date, timeZone: TimeZone?)](./init%28start,end,timezone%29.md)
  Creates and returns a text provider with the specified dates and time zone information.
- [convenience init(start: Date, end: Date)](./init%28start,end%29.md)
  Creates and returns a text provider with the specified start and end dates.
### Getting the Time Information
- [var startDate: Date](./startdate.md)
  The start date for the time interval.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone used to format time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/enddate)*