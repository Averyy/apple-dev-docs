# relativeToDate

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The end date that the text provider uses when calculating a fixed, relative date.

**Availability**:
- watchOS 7.0+ - Deprecated in 27.2

## Declaration

```swift
var relativeToDate: Date? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSDate * relativeToDate;
```

## See Also

### Getting the Date Information
- [var date: Date](./date.md)
  The target date to use for calculations.
- [var relativeDateStyle: CLKRelativeDateStyle](./relativedatestyle.md)
  The formatting style to use for the relative time value.
- [var calendarUnits: NSCalendar.Unit](./calendarunits.md)
  The calendar units to include in the formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/relativetodate)*