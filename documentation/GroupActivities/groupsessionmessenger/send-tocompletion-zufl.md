# send(_:to:completion:)

**Framework**: Group Activities  
**Kind**: method

Sends a standard data object to other participants in the group session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final func send(_ value: Data, to participants: Participants = .all, completion: @escaping ((any Error)?) -> Void)
```

#### Discussion

Use this method to send data using a standard data object. Your app is responsible for decoding and using the data it receives.

## Parameters

- `participants`: The recipients of the message. The default value   of this parameter is the set of all active participants in the   session. Use the   option   to specify a subset of participants.
- `completion`: The handler block to call with the results of the   delivery attempt. The handler has no return value and takes a single   Error parameter. The value of this parameter is   if delivery   succeeds; otherwise, it contains an appropriate error object.

## See Also

- [func send(Data, to: Participants) async throws](groupsessionmessenger/send(_:to:)-4o52m.md)
  Sends a standard data object asynchronously to other participants in the group session.
- [func send<Message>(Message, to: Participants) async throws](groupsessionmessenger/send(_:to:)-2a4ku.md)
  Sends a custom type asynchronously to other participants in the group session.
- [func send<Message>(Message, to: Participants, completion: ((any Error)?) -> Void)](groupsessionmessenger/send(_:to:completion:)-9e0sn.md)
  Sends a custom type to other participants in the group session.
- [enum Participants](participants.md)
  The set of participants to include in messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/send(_:to:completion:)-zufl)*