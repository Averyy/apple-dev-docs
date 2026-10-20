# calendarUnits

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The calendar units to include in the formatted string.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var calendarUnits: NSCalendar.Unit { get set }
```

```objc
@property (nonatomic) NSCalendarUnit calendarUnits;
```

#### Discussion

For a list of supported calendar units, see [Date Format Options](../clkdatetextprovider.md#Date-Format-Options).

## See Also

### Getting the Date Information
- [var date: Date](./date.md)
  The date to display.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone used in the formatted string.
- [var uppercase: Bool](./uppercase.md)
  A Boolean value that determines whether the date string displays in uppercase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/calendarunits)*