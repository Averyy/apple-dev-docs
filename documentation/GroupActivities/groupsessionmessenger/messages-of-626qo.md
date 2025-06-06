# messages(of:)

**Framework**: Group Activities  
**Kind**: method

Returns the asynchronous sequence of messages that contain a generic data object.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
final func messages(of type: Data.Type) -> GroupSessionMessenger.Messages<Data>
```

#### Discussion

Call this method to receive the messages that other participants send to the group. This method returns a [`GroupSessionMessenger.Messages`](groupsessionmessenger/messages.md) structure, which conforms to the `AsyncSequence` protocol. This sequence contains all, some, or none of the messages sent over time. You retrieve messages by iterating over them using an asynchronous `for`-`in` loop, as shown in the following example:

```swift
let sessionMessenger = GroupSessionMessenger(session: groupSession)

async {
    for await dataMessage in sessionMessenger.messages(of: Data.self) {
        self.processDataMessage(dataMessage)
    }
}
```

## Parameters

- `type`: The type of the    class. Specify  .

## See Also

- [func messages<Message>(of: Message.Type) -> GroupSessionMessenger.Messages<Message>](groupsessionmessenger/messages(of:)-jvoz.md)
  Returns the asynchronous sequence of messages that match the app-specific type.
- [GroupSessionMessenger.Messages](groupsessionmessenger/messages.md)
  An asynchronous sequence of messages sent to the session.
- [GroupSessionMessenger.MessageContext](groupsessionmessenger/messagecontext.md)
  A structure that contains additional information about an incoming message, such as which device sent it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/messages(of:)-626qo)*