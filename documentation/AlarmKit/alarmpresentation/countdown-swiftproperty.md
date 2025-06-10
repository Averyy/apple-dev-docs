# countdown

**Framework**: AlarmKit  
**Kind**: property

The content for the snooze or countdown mode of the alarm.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var countdown: AlarmPresentation.Countdown?
```

#### Discussion

This value can be `nil` if the alarm doesn’t support countdown mode.

## See Also

- [init(alert: AlarmPresentation.Alert, countdown: AlarmPresentation.Countdown?, paused: AlarmPresentation.Paused?)](alarmpresentation/init(alert:countdown:paused:).md)
  Configures an alert with an optional countdown and paused state.
- [var alert: AlarmPresentation.Alert](alarmpresentation/alert-swift.property.md)
  The content for the alert mode of the alarm.
- [var paused: AlarmPresentation.Paused?](alarmpresentation/paused-swift.property.md)
  The content for the pause mode of the alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/countdown-swift.property)*