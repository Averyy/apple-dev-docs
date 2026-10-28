# dateValue

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The date currently specified in the picker.

**Availability**:
- macOS

## Declaration

```swift
var dateValue: Date { get set }
```

```objc
@property (copy) NSDate * dateValue;
```

## Discussion

Assign a date to this property to set the starting value for the picker. For range-based dates, use the [`timeInterval`](./timeinterval.md) property to set the extent of the time range.

## See Also

### Object Values
- [var timeInterval: TimeInterval](./timeinterval.md)
  The time interval that represents the date range.
- [var calendar: Calendar?](./calendar.md)
  The calendar used by the date picker.
- [var locale: Locale?](./locale.md)
  The locale used to display dates.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone used to display time-related values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/datevalue)*