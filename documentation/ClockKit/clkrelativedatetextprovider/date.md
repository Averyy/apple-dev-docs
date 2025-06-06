# date

**Framework**: ClockKit  
**Kind**: property

The target date to use for calculations.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var date: Date { get set }
```

#### Discussion

When creating a text provider that updates automatically,  the provider calculates the relative date between this property and the current date. The value of this property must not be `nil`.

When creating a fixed, relative text provider, the provider calculates the relative date between this property and the [`relativeToDate`](clkrelativedatetextprovider/relativetodate.md) property.

## See Also

- [var relativeToDate: Date?](clkrelativedatetextprovider/relativetodate.md)
  The end date that the text provider uses when calculating a fixed, relative date.
- [var relativeDateStyle: CLKRelativeDateStyle](clkrelativedatetextprovider/relativedatestyle.md)
  The formatting style to use for the relative time value.
- [var calendarUnits: NSCalendar.Unit](clkrelativedatetextprovider/calendarunits.md)
  The calendar units to include in the formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkrelativedatetextprovider/date)*