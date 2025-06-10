# timeZone

**Framework**: UIKit  
**Kind**: property

The time zone reflected in the date displayed by the date picker.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var timeZone: TimeZone? { get set }
```

#### Discussion

The default value is `nil`, which tells the date picker to use the current time zone as returned by [`local`](https://developer.apple.com/documentation/Foundation/NSTimeZone/local) ([`NSTimeZone`](https://developer.apple.com/documentation/Foundation/NSTimeZone)) or the time zone used by the date picker’s calendar.

## See Also

- [var calendar: Calendar!](uidatepicker/calendar.md)
  The calendar to use for the date picker.
- [var date: Date](uidatepicker/date.md)
  The date displayed by the date picker.
- [var locale: Locale?](uidatepicker/locale.md)
  The locale used by the date picker.
- [func setDate(Date, animated: Bool)](uidatepicker/setdate(_:animated:).md)
  Sets the date to display in the date picker, with an option to animate the setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/timezone)*