# timeInterval

**Framework**: AppKit  
**Kind**: property

The time interval that represents the date range.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var timeInterval: TimeInterval { get set }
```

#### Discussion

The date range begins at the date in the [`dateValue`](nsdatepickercell/datevalue.md) property. The value in this property applies only when the date picker is in the [`NSRangeDateMode`](nsrangedatemode.md) mode.

## See Also

- [var dateValue: Date](nsdatepickercell/datevalue.md)
  The date currently specified in the picker.
- [var calendar: Calendar?](nsdatepickercell/calendar.md)
  The calendar used by the date picker.
- [var locale: Locale?](nsdatepickercell/locale.md)
  The locale used to display dates.
- [var timeZone: TimeZone?](nsdatepickercell/timezone.md)
  The time zone used to display time-related values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/timeinterval)*