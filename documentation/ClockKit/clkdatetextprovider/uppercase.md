# uppercase

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the date string displays in uppercase.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var uppercase: Bool { get set }
```

```objc
@property (nonatomic) BOOL uppercase;
```

## Discussion

By default, this property is set to [`false`](../../Swift/false.md). Set it to [`true`](../../Foundation/nsexpression/true.md) if you want the text provider to produce uppercase text.

## See Also

### Getting the Date Information
- [var date: Date](./date.md)
  The date to display.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone used in the formatted string.
- [var calendarUnits: NSCalendar.Unit](./calendarunits.md)
  The calendar units to include in the formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/uppercase)*