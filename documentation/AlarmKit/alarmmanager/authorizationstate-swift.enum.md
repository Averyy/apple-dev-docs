# AlarmManager.AuthorizationState

**Framework**: AlarmKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration describing all authorization states for the client process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
enum AuthorizationState
```

## Topics

### Describing an authorization state
- [AlarmManager.AuthorizationState.authorized](./authorizationstate-swift.enum/authorized.md)
  The person authorized the client to use alarms and timers.
- [AlarmManager.AuthorizationState.denied](./authorizationstate-swift.enum/denied.md)
  The client previously requested authorization from the person, but they declined.
- [AlarmManager.AuthorizationState.notDetermined](./authorizationstate-swift.enum/notdetermined.md)
  The client hasn’t requested authorization from a person.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Checking authorization status
- [AlarmManager.AlarmAuthorizationStateUpdates](./alarmauthorizationstateupdates.md)
  An asynchronous sequence that publishes a new value when authorization for the alarms and timers system changes.
- [var authorizationUpdates: some AsyncSequence<AlarmManager.AuthorizationState, Never>](./authorizationupdates.md)
  An asynchronous sequence that emits events when authorization to use alarms changes.
- [var authorizationState: AlarmManager.AuthorizationState](./authorizationstate-swift.property.md)
  Returns the current authorization state for this client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/authorizationstate-swift.enum)*