# timeZone

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The time zone used to format time values.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSTimeZone * timeZone;
```

## Discussion

If the value is `nil`, the text provider uses the time zone currently configured for the user.

## See Also

### Related Documentation
- [convenience init(start: Date, end: Date, timeZone: TimeZone?)](./init%28start,end,timezone%29.md)
  Creates and returns a text provider with the specified dates and time zone information.
### Getting the Time Information
- [var startDate: Date](./startdate.md)
  The start date for the time interval.
- [var endDate: Date](./enddate.md)
  The end date for the time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimeintervaltextprovider/timezone)*