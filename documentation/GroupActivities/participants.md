# Participants

**Framework**: Group Activities  
**Kind**: enum

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
- [Participants.all](participants/all.md)
  The set of all participants.
- [case only(Set<Participant>)](participants/only(_:)-swift.enum.case.md)
  A custom subset of participants.
- [static func only(Participant) -> Participants](participants/only(_:)-swift.type.method.md)
  Returns a set containing the specified participant.

## See Also

- [func send(Data, to: Participants) async throws](groupsessionmessenger/send(_:to:)-4o52m.md)
  Sends a standard data object asynchronously to other participants in the group session.
- [func send<Message>(Message, to: Participants) async throws](groupsessionmessenger/send(_:to:)-2a4ku.md)
  Sends a custom type asynchronously to other participants in the group session.
- [func send(Data, to: Participants, completion: ((any Error)?) -> Void)](groupsessionmessenger/send(_:to:completion:)-zufl.md)
  Sends a standard data object to other participants in the group session.
- [func send<Message>(Message, to: Participants, completion: ((any Error)?) -> Void)](groupsessionmessenger/send(_:to:completion:)-9e0sn.md)
  Sends a custom type to other participants in the group session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/participants)*