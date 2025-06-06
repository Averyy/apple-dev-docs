# timeZone

**Framework**: ClockKit  
**Kind**: property

The time zone used in the formatted string.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var timeZone: TimeZone? { get set }
```

#### Discussion

The date provider uses the time zone information during formatting to ensure that the date information is displayed correctly. To use the current time zone, set this property to `nil`.

## See Also

- [var date: Date](clkdatetextprovider/date.md)
  The date to display.
- [var calendarUnits: NSCalendar.Unit](clkdatetextprovider/calendarunits.md)
  The calendar units to include in the formatted string.
- [var uppercase: Bool](clkdatetextprovider/uppercase.md)
  A Boolean value that determines whether the date string displays in uppercase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkdatetextprovider/timezone)*