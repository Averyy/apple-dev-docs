# alarms

**Framework**: AlarmKit  
**Kind**: property

Fetches all alarms from the daemon that belong to the current client.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
var alarms: [Alarm] { get throws }
```

#### Discussion

As soon as an alarm fires and stops it’s deleted from the daemon’s store.  If you want to determine if a one-shot alarm has fired, persist your alarms in your own store and compare that with the result of this function call.  If the array is missing scheduled alarms, then those alarms fired.

## See Also

- [AlarmManager.AlarmUpdates](alarmmanager/alarmupdates-swift.struct.md)
  An async sequence that publishes whenever an alarm changes.
- [var alarmUpdates: some AsyncSequence<Array<Alarm>, Never>](alarmmanager/alarmupdates-swift.property.md)
  An asynchronous sequence that emits events when the set of alarms changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarms)*