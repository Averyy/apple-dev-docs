# authorizationState

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

Returns the current authorization state for this client.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var authorizationState: AlarmManager.AuthorizationState { get }
```

## See Also

### Checking authorization status
- [AlarmManager.AlarmAuthorizationStateUpdates](./alarmauthorizationstateupdates.md)
  An asynchronous sequence that publishes a new value when authorization for the alarms and timers system changes.
- [var authorizationUpdates: some AsyncSequence<AlarmManager.AuthorizationState, Never>](./authorizationupdates.md)
  An asynchronous sequence that emits events when authorization to use alarms changes.
- [AlarmManager.AuthorizationState](./authorizationstate-swift.enum.md)
  An enumeration describing all authorization states for the client process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/authorizationstate-swift.property)*