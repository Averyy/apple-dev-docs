# alarmUpdates

**Framework**: AlarmKit  
**Kind**: property

An asynchronous sequence that emits events when the set of alarms changes.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var alarmUpdates: some AsyncSequence<Array<Alarm>, Never> { get }
```

#### Discussion

Use this to receive a notification when an alarm alerts, snoozes, or dismisses.

## See Also

- [AlarmManager.AlarmUpdates](alarmmanager/alarmupdates-swift.struct.md)
  An async sequence that publishes whenever an alarm changes.
- [var alarms: [Alarm]](alarmmanager/alarms.md)
  Fetches all alarms from the daemon that belong to the current client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmupdates-swift.property)*