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

If the value of this property is `nil`, the text provider uses the time zone currently configured for the user.

## See Also

### Related Documentation
- [convenience init(date: Date, timeZone: TimeZone?)](./init%28date,timezone%29.md)
  Creates and returns a text provider for displaying the specified time.
### Getting the Time Information
- [var date: Date](./date.md)
  The date object containing the time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clktimetextprovider/timezone)*