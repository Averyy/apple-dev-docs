# calendar

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The calendar to use for the date picker.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var calendar: Calendar! { get set }
```

```objc
@property (nonatomic, copy, null_resettable) NSCalendar * calendar;
```

## Discussion

The default value of this property corresponds to the user’s current calendar as configured in Settings. This is equivalent to the value returned by calling the [`NSCalendar`](../../Foundation/nscalendar.md) class method [`current`](../../Foundation/nscalendar/current.md). Setting this property to `nil` is equivalent to setting it to its default value.

Calendars specify the details of cultural systems used for reckoning time; they identify the beginning, length, and divisions of a year.

## See Also

### Managing the date and calendar
- [var date: Date](./date.md)
  The date displayed by the date picker.
- [var locale: Locale?](./locale.md)
  The locale used by the date picker.
- [func setDate(Date, animated: Bool)](./setdate%28_,animated%29.md)
  Sets the date to display in the date picker, with an option to animate the setting.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone reflected in the date displayed by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/calendar)*