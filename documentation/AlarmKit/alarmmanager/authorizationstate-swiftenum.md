# AlarmManager.AuthorizationState

**Framework**: AlarmKit  
**Kind**: enum

An enumeration describing all authorization states for the client process.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

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
### Decoding
- [init(from: any Decoder) throws](alarmmanager/authorizationstate-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (AlarmManager.AuthorizationState, AlarmManager.AuthorizationState) -> Bool](alarmmanager/authorizationstate-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](alarmmanager/authorizationstate-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](alarmmanager/authorizationstate-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](alarmmanager/authorizationstate-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](alarmmanager/authorizationstate-swift.enum/equatable-implementations.md)

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