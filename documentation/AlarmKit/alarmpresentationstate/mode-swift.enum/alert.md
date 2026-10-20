# AlarmPresentationState.Mode.Alert

**Framework**: AlarmKit  
**Kind**: struct  
**Role**: Structure

A value that indicates the current state of an alarm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Alert
```

## Topics

### Creating an alert
- [init(time: Alarm.Schedule.Relative.Time)](./alert/init%28time%29.md)
  Creates an instance of an alert.
- [var time: Alarm.Schedule.Relative.Time](./alert/time.md)
  The time that the alarm emits an alert.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating an alert
- [case alert(AlarmPresentationState.Mode.Alert)](./alert%28_%29.md)
  A mode indicating an alarm emits an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmpresentationstate/mode-swift.enum/alert)*