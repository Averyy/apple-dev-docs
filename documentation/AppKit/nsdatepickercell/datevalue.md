# dateValue

**Framework**: AppKit  
**Kind**: property

The date currently specified in the picker.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var dateValue: Date { get set }
```

#### Discussion

Assign a date to this property to set the starting value for the picker. For range-based dates, use the [`timeInterval`](nsdatepickercell/timeinterval.md) property to set the extent of the time range.

## See Also

- [var timeInterval: TimeInterval](nsdatepickercell/timeinterval.md)
  The time interval that represents the date range.
- [var calendar: Calendar?](nsdatepickercell/calendar.md)
  The calendar used by the date picker.
- [var locale: Locale?](nsdatepickercell/locale.md)
  The locale used to display dates.
- [var timeZone: TimeZone?](nsdatepickercell/timezone.md)
  The time zone used to display time-related values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/datevalue)*