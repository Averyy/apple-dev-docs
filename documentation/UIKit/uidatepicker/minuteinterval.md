# minuteInterval

**Framework**: UIKit  
**Kind**: property

The interval at which the date picker should display minutes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var minuteInterval: Int { get set }
```

#### Discussion

Use this property to set the interval displayed by the minutes wheel (for example, 15 minutes). The interval value must be evenly divided into 60; if it isn’t, the default value is used. The default and minimum values are 1; the maximum value is 30.

## See Also

- [var maximumDate: Date?](uidatepicker/maximumdate.md)
  The maximum date that a date picker can show.
- [var minimumDate: Date?](uidatepicker/minimumdate.md)
  The minimum date that a date picker can show.
- [var countDownDuration: TimeInterval](uidatepicker/countdownduration.md)
  The value displayed by the date picker when the mode property is set to show a countdown time.
- [var roundsToMinuteInterval: Bool](uidatepicker/roundstominuteinterval.md)
  A Boolean value that determines whether the date rounds to a specific minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidatepicker/minuteinterval)*