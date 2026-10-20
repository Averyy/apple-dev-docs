# Participants

**Framework**: Group Activities  
**Kind**: enum  
**Role**: Enumeration

The set of participants to include in messages.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum Participants
```

## Topics

### Getting the set of participants
- [Participants.all](./participants/all.md)
  The set of all participants.
- [case only(Set<Participant>)](./participants/only%28_%29-swift.enum.case.md)
  A custom subset of participants.
- [static func only(Participant) -> Participants](./participants/only%28_%29-swift.type.method.md)
  Returns a set containing the specified participant.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sending data to the group
- [func send(Data, to: Participants) async throws](./groupsessionmessenger/send%28_,to%29-4o52m.md)
  Sends a standard data object asynchronously to other participants in the group session.
- [func send<Message>(Message, to: Participants) async throws](./groupsessionmessenger/send%28_,to%29-2a4ku.md)
  Sends a custom type asynchronously to other participants in the group session.
- [func send(Data, to: Participants, completion: ((any Error)?) -> Void)](./groupsessionmessenger/send%28_,to,completion%29-zufl.md)
  Sends a standard data object to other participants in the group session.
- [func send<Message>(Message, to: Participants, completion: ((any Error)?) -> Void)](./groupsessionmessenger/send%28_,to,completion%29-9e0sn.md)
  Sends a custom type to other participants in the group session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/participants)*