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

For a list of supported units, see [Date Format Options](../clkrelativedatetextprovider.md#Date-Format-Options).

## See Also

### Getting the Date Information
- [var date: Date](./date.md)
  The target date to use for calculations.
- [var relativeToDate: Date?](./relativetodate.md)
  The end date that the text provider uses when calculating a fixed, relative date.
- [var relativeDateStyle: CLKRelativeDateStyle](./relativedatestyle.md)
  The formatting style to use for the relative time value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/calendarunits)*