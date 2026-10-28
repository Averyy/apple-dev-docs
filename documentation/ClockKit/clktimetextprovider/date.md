# date

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The date object containing the time value.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var date: Date { get set }
```

```objc
@property (nonatomic, retain) NSDate * date;
```

## Discussion

You can make changes to this property until you hand off the timeline entry containing it to ClockKit. The value of this property must not be `nil`.

## See Also

### Related Documentation
- [convenience init(date: Date)](./init%28date%29.md)
  Creates and returns a text provider for displaying the specified time.
- [convenience init(date: Date, timeZone: TimeZone?)](./init%28date,timezone%29.md)
  Creates and returns a text provider for displaying the specified time.
### Getting the Time Information
- [var timeZone: TimeZone?](./timezone.md)
  The time zone used to format time values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimetextprovider/date)*