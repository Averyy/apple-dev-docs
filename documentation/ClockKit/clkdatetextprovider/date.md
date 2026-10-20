# date

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The date to display.

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

#### Discussion

You set the value of this property at creation time but may change it later.

## See Also

### Getting the Date Information
- [var timeZone: TimeZone?](./timezone.md)
  The time zone used in the formatted string.
- [var calendarUnits: NSCalendar.Unit](./calendarunits.md)
  The calendar units to include in the formatted string.
- [var uppercase: Bool](./uppercase.md)
  A Boolean value that determines whether the date string displays in uppercase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/date)*