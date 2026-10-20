# setDate(_:animated:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the date to display in the date picker, with an option to animate the setting.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setDate(_ date: Date, animated: Bool)
```

```objc
- (void) setDate:(NSDate *) date animated:(BOOL) animated;
```

## Parameters

- `date`: An `NSDate` object representing the new date to display in the date picker.
- `animated`: [`true`](../../Swift/true.md) to animate the setting of the new date, otherwise [`false`](../../Swift/false.md). The animation rotates the wheels until the new date and time is shown under the highlight rectangle.

## See Also

### Managing the date and calendar
- [var calendar: Calendar!](./calendar.md)
  The calendar to use for the date picker.
- [var date: Date](./date.md)
  The date displayed by the date picker.
- [var locale: Locale?](./locale.md)
  The locale used by the date picker.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone reflected in the date displayed by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/setdate(_:animated:))*