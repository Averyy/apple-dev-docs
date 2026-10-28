# timeZone

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The time zone used in the formatted string.

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

The date provider uses the time zone information during formatting to ensure that the date information is displayed correctly. To use the current time zone, set this property to `nil`.

## See Also

### Getting the Date Information
- [var date: Date](./date.md)
  The date to display.
- [var calendarUnits: NSCalendar.Unit](./calendarunits.md)
  The calendar units to include in the formatted string.
- [var uppercase: Bool](./uppercase.md)
  A Boolean value that determines whether the date string displays in uppercase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/timezone)*