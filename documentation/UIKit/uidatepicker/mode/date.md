# UIDatePicker.Mode.date

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A mode that displays the date in months, days of the month, and years. The exact order of these items depends on the locale setting. An example of this mode is “November | 15 | 2007 “.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
case date
```

```c
UIDatePickerModeDate
```

## See Also

### Constants
- [UIDatePicker.Mode.time](./time.md)
  A mode that displays the date in hours, minutes, and (optionally) an AM/PM designation. The exact items shown and their order depend upon the locale set. An example of this mode is “6 | 53 | PM”.
- [UIDatePicker.Mode.dateAndTime](./dateandtime.md)
  A mode that displays the date as unified day of the week, month, and day of the month values, plus hours, minutes, and (optionally) an AM/PM designation. The exact order and format of these items depends on the locale set. An example of this mode is “Wed Nov 15 | 6 | 53 | PM”.
- [UIDatePicker.Mode.yearAndMonth](./yearandmonth.md)
  A mode that displays the date in months and years.
- [UIDatePicker.Mode.countDownTimer](./countdowntimer.md)
  A mode that displays hour and minute values, for example, “1 | 53”. The application must set a timer to fire at the proper interval and set the date picker as the seconds tick down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/mode/date)*