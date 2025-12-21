# AlarmManager.AuthorizationState

**Framework**: AlarmKit  
**Kind**: enum

An enumeration describing all authorization states for the client process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
enum AuthorizationState
```

## Topics

### Describing an authorization state
- [AlarmManager.AuthorizationState.authorized](alarmmanager/authorizationstate-swift.enum/authorized.md)
  The person authorized the client to use alarms and timers.
- [AlarmManager.AuthorizationState.denied](alarmmanager/authorizationstate-swift.enum/denied.md)
  The client previously requested authorization from the person, but they declined.
- [AlarmManager.AuthorizationState.notDetermined](alarmmanager/authorizationstate-swift.enum/notdetermined.md)
  The client hasn’t requested authorization from a person.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [AlarmManager.AlarmAuthorizationStateUpdates](alarmmanager/alarmauthorizationstateupdates.md)
  An asynchronous sequence that publishes a new value when authorization for the alarms and timers system changes.
- [var authorizationUpdates: some AsyncSequence<AlarmManager.AuthorizationState, Never>](alarmmanager/authorizationupdates.md)
  An asynchronous sequence that emits events when authorization to use alarms changes.
- [var authorizationState: AlarmManager.AuthorizationState](alarmmanager/authorizationstate-swift.property.md)
  Returns the current authorization state for this client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/authorizationstate-swift.enum)*