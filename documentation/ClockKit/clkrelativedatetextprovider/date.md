# date

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The target date to use for calculations.

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

When creating a text provider that updates automatically,  the provider calculates the relative date between this property and the current date. The value of this property must not be `nil`.

When creating a fixed, relative text provider, the provider calculates the relative date between this property and the [`relativeToDate`](./relativetodate.md) property.

## See Also

### Getting the Date Information
- [var relativeToDate: Date?](./relativetodate.md)
  The end date that the text provider uses when calculating a fixed, relative date.
- [var relativeDateStyle: CLKRelativeDateStyle](./relativedatestyle.md)
  The formatting style to use for the relative time value.
- [var calendarUnits: NSCalendar.Unit](./calendarunits.md)
  The calendar units to include in the formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/date)*