# authorizationUpdates

**Framework**: AlarmKit  
**Kind**: property  
**Role**: Instance Property

An asynchronous sequence that emits events when authorization to use alarms changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var authorizationUpdates: some AsyncSequence<AlarmManager.AuthorizationState, Never> { get }
```

## See Also

### Checking authorization status
- [AlarmManager.AlarmAuthorizationStateUpdates](./alarmauthorizationstateupdates.md)
  An asynchronous sequence that publishes a new value when authorization for the alarms and timers system changes.
- [AlarmManager.AuthorizationState](./authorizationstate-swift.enum.md)
  An enumeration describing all authorization states for the client process.
- [var authorizationState: AlarmManager.AuthorizationState](./authorizationstate-swift.property.md)
  Returns the current authorization state for this client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/authorizationupdates)*