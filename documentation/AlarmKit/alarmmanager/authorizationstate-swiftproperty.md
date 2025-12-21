# authorizationState

**Framework**: AlarmKit  
**Kind**: property

Returns the current authorization state for this client.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var authorizationState: AlarmManager.AuthorizationState { get }
```

## See Also

- [AlarmManager.AlarmAuthorizationStateUpdates](alarmmanager/alarmauthorizationstateupdates.md)
  An asynchronous sequence that publishes a new value when authorization for the alarms and timers system changes.
- [var authorizationUpdates: some AsyncSequence<AlarmManager.AuthorizationState, Never>](alarmmanager/authorizationupdates.md)
  An asynchronous sequence that emits events when authorization to use alarms changes.
- [AlarmManager.AuthorizationState](alarmmanager/authorizationstate-swift.enum.md)
  An enumeration describing all authorization states for the client process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/authorizationstate-swift.property)*