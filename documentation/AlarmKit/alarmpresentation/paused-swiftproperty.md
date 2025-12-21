# paused

**Framework**: AlarmKit  
**Kind**: property

The content for the pause mode of the alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var paused: AlarmPresentation.Paused?
```

#### Discussion

This value can be `nil` if the alarm doesn’t support pause mode.

## See Also

- [init(alert: AlarmPresentation.Alert, countdown: AlarmPresentation.Countdown?, paused: AlarmPresentation.Paused?)](alarmpresentation/init(alert:countdown:paused:).md)
  Configures an alert with an optional countdown and paused state.
- [var alert: AlarmPresentation.Alert](alarmpresentation/alert-swift.property.md)
  The content for the alert mode of the alarm.
- [var countdown: AlarmPresentation.Countdown?](alarmpresentation/countdown-swift.property.md)
  The content for the snooze or countdown mode of the alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/paused-swift.property)*