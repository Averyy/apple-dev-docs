# init(alert:countdown:paused:)

**Framework**: AlarmKit  
**Kind**: init

Configures an alert with an optional countdown and paused state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(alert: AlarmPresentation.Alert, countdown: AlarmPresentation.Countdown? = nil, paused: AlarmPresentation.Paused? = nil)
```

## Parameters

- `alert`: The required content for the alert mode of the alarm.
- `countdown`: An optional parameter with a default   value.   Provide a   object.
- `paused`: An optional parameter with a default   value.   Provide a   object.

## See Also

- [var alert: AlarmPresentation.Alert](alarmpresentation/alert-swift.property.md)
  The content for the alert mode of the alarm.
- [var countdown: AlarmPresentation.Countdown?](alarmpresentation/countdown-swift.property.md)
  The content for the snooze or countdown mode of the alarm.
- [var paused: AlarmPresentation.Paused?](alarmpresentation/paused-swift.property.md)
  The content for the pause mode of the alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentation/init(alert:countdown:paused:))*