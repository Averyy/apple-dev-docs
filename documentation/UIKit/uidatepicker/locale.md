# locale

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The locale used by the date picker.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var locale: Locale? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSLocale * locale;
```

## Discussion

The default value is the current locale as returned by the [`current`](../../Foundation/nslocale/current.md) property of [`NSLocale`](../../Foundation/nslocale.md), or the locale used by the date picker’s calendar. Locales encapsulate information about facets of a language or culture, such as the way dates are formatted.

## See Also

### Managing the date and calendar
- [var calendar: Calendar!](./calendar.md)
  The calendar to use for the date picker.
- [var date: Date](./date.md)
  The date displayed by the date picker.
- [func setDate(Date, animated: Bool)](./setdate%28_,animated%29.md)
  Sets the date to display in the date picker, with an option to animate the setting.
- [var timeZone: TimeZone?](./timezone.md)
  The time zone reflected in the date displayed by the date picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/locale)*