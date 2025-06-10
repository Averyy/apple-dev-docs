# calendar

**Framework**: UIKit  
**Kind**: property

The calendar to use for the date picker.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var calendar: Calendar! { get set }
```

#### Discussion

The default value of this property corresponds to the user’s current calendar as configured in Settings. This is equivalent to the value returned by calling the [`NSCalendar`](https://developer.apple.com/documentation/Foundation/NSCalendar) class method [`current`](https://developer.apple.com/documentation/Foundation/NSCalendar/current). Setting this property to `nil` is equivalent to setting it to its default value.

Calendars specify the details of cultural systems used for reckoning time; they identify the beginning, length, and divisions of a year.

## See Also

- [var date: Date](uidatepicker/date.md)
  The date displayed by the date picker.
- [var locale: Locale?](uidatepicker/locale.md)
  The locale used by the date picker.
- [func setDate(Date, animated: Bool)](uidatepicker/setdate(_:animated:).md)
  Sets the date to display in the date picker, with an option to animate the setting.
- [var timeZone: TimeZone?](uidatepicker/timezone.md)
  The time zone reflected in the date displayed by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/calendar)*