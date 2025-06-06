# setDate(_:animated:)

**Framework**: UIKit  
**Kind**: method

Sets the date to display in the date picker, with an option to animate the setting.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setDate(_ date: Date, animated: Bool)
```

## Parameters

- `date`: An   object representing the new date to display in the date picker.
- `animated`:   to animate the setting of the new date, otherwise  . The animation rotates the wheels until the new date and time is shown under the highlight rectangle.

## See Also

- [var calendar: Calendar!](uidatepicker/calendar.md)
  The calendar to use for the date picker.
- [var date: Date](uidatepicker/date.md)
  The date displayed by the date picker.
- [var locale: Locale?](uidatepicker/locale.md)
  The locale used by the date picker.
- [var timeZone: TimeZone?](uidatepicker/timezone.md)
  The time zone reflected in the date displayed by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/setdate(_:animated:))*