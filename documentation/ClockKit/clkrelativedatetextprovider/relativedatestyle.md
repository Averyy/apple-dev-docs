# relativeDateStyle

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The formatting style to use for the relative time value.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var relativeDateStyle: CLKRelativeDateStyle { get set }
```

```objc
@property (nonatomic) CLKRelativeDateStyle relativeDateStyle;
```

#### Discussion

For a list of possible values, see [`CLKRelativeDateStyle`](../clkrelativedatestyle.md).

## See Also

### Getting the Date Information
- [var date: Date](./date.md)
  The target date to use for calculations.
- [var relativeToDate: Date?](./relativetodate.md)
  The end date that the text provider uses when calculating a fixed, relative date.
- [var calendarUnits: NSCalendar.Unit](./calendarunits.md)
  The calendar units to include in the formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/relativedatestyle)*