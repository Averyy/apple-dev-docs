# endDate

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The ending time and date for the gauge’s time interval.

**Availability**:
- watchOS 5.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var endDate: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * endDate;
```

#### Discussion

The end date is equal to or later than the start date.

## See Also

### Getting Information about the Gauge
- [var startDate: Date](./startdate.md)
  The starting time and date for the gauge’s time interval.
- [var startFillFraction: Float](./startfillfraction.md)
  The position of the leading edge of the time bar within the specified time interval.
- [var endFillFraction: Float](./endfillfraction.md)
  The position of the trailing edge of the time bar within the specified time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervalgaugeprovider/enddate)*