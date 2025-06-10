# uppercase

**Framework**: ClockKit  
**Kind**: property

A Boolean value that determines whether the date string displays in uppercase.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var uppercase: Bool { get set }
```

#### Discussion

By default, this property is set to [`false`](https://developer.apple.com/documentation/swift/false). Set it to [`true`](https://developer.apple.com/documentation/Foundation/NSExpression/true) if you want the text provider to produce uppercase text.

## See Also

- [var date: Date](clkdatetextprovider/date.md)
  The date to display.
- [var timeZone: TimeZone?](clkdatetextprovider/timezone.md)
  The time zone used in the formatted string.
- [var calendarUnits: NSCalendar.Unit](clkdatetextprovider/calendarunits.md)
  The calendar units to include in the formatted string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/uppercase)*