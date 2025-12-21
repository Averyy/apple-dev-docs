# quarter

**Framework**: Foundation  
**Kind**: property

Identifier for the quarter of the calendar.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var quarter: NSCalendar.Unit { get }
```

#### Discussion

The corresponding value is an `NSInteger`. Equal to `kCFCalendarUnitQuarter`.

> ❗ **Important**:  The `NSCalendarUnitQuarter` unit is largely unimplemented, and is not recommended for use.

## See Also

- [static var era: NSCalendar.Unit](nscalendar/unit/era.md)
  Identifier for the era unit.
- [static var year: NSCalendar.Unit](nscalendar/unit/year.md)
  Identifier for the year unit.
- [static var yearForWeekOfYear: NSCalendar.Unit](nscalendar/unit/yearforweekofyear.md)
  Identifier for the week-counting year unit.
- [static var month: NSCalendar.Unit](nscalendar/unit/month.md)
  Identifier for the month unit.
- [static var isLeapMonth: NSCalendar.Unit](nscalendar/unit/isleapmonth.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscalendar/unit/quarter)*