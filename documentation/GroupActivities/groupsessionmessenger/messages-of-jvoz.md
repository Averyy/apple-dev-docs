# messages(of:)

**Framework**: Group Activities  
**Kind**: method

Returns the asynchronous sequence of messages that match the app-specific type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final func messages<Message>(of type: Message.Type) -> GroupSessionMessenger.Messages<Message> where Message : Decodable, Message : Encodable
```

#### Discussion

Call this method to receive the messages that other participants send to the group. This method returns a [`GroupSessionMessenger.Messages`](groupsessionmessenger/messages.md) structure, which conforms to the `AsyncSequence` protocol. This sequence contains all, some, or none of the messages sent over time. You retrieve messages by iterating over them using an asynchronous `for`-`in` loop, as shown in the following example:

```swift
let sessionMessenger = GroupSessionMessenger(session: groupSession)

async {
    for await move in sessionMessenger.messages(of: TicTacToe.Move.self) {
        self.board.addMove(move)
    }
}
```

## Parameters

- `type`: The class of the custom type you use to package the message contents.

## See Also

- [func messages(of: Data.Type) -> GroupSessionMessenger.Messages<Data>](groupsessionmessenger/messages(of:)-626qo.md)
  Returns the asynchronous sequence of messages that contain a generic data object.
- [GroupSessionMessenger.Messages](groupsessionmessenger/messages.md)
  An asynchronous sequence of messages sent to the session.
- [GroupSessionMessenger.MessageContext](groupsessionmessenger/messagecontext.md)
  A structure that contains additional information about an incoming message, such as which device sent it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/messages(of:)-jvoz)*