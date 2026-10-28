# countdown

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

The content for the snooze or countdown mode of the alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var countdown: AlarmPresentation.Countdown?
```

## Discussion

This value can be `nil` if the alarm doesn’t support countdown mode.

## See Also

### Defining the alarm UI
- [init(alert: AlarmPresentation.Alert, countdown: AlarmPresentation.Countdown?, paused: AlarmPresentation.Paused?)](./init%28alert,countdown,paused%29.md)
  Configures an alert with an optional countdown and paused state.
- [var alert: AlarmPresentation.Alert](./alert-swift.property.md)
  The content for the alert mode of the alarm.
- [var paused: AlarmPresentation.Paused?](./paused-swift.property.md)
  The content for the pause mode of the alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/countdown-swift.property)*