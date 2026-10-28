# timeInterval

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The time interval that represents the date range.

**Availability**:
- macOS

## Declaration

```swift
var timeInterval: TimeInterval { get set }
```

```objc
@property NSTimeInterval timeInterval;
```

## Discussion

The date range begins at the date in the [`dateValue`](./datevalue.md) property. The value in this property applies only when the date picker is in the [`NSRangeDateMode`](../nsrangedatemode.md) mode.

## See Also

### Object Values
- [var dateValue: Date](./datevalue.md)
  The date currently specified in the picker.
- [var calendar: Calendar?](./calendar.md)
  The calendar used by the date picker.
- [var locale: Locale?](./locale.md)
  The locale used to display dates.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone used to display time-related values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdatepickercell/timeinterval)*