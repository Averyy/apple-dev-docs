# GroupSessionMessenger.Messages

**Framework**: Group Activities  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence of messages sent to the session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Messages<Message> where Message : Decodable, Message : Encodable
```

## Overview

When you use a [`GroupSessionMessenger`](../groupsessionmessenger.md) to communicate across devices, the `Messages` structure provides the sequence of messages the other devices send. Iterate over the contents of this structure asynchronously to retrieve each message and update your app.

Don’t create this structure directly. Instead, use the [`messages(of:)`](./messages%28of%29-626qo.md) or [`messages(of:)`](./messages%28of%29-jvoz.md) method to retrieve the messages for a given session.

## Topics

### Creating an iterator
- [GroupSessionMessenger.Messages.Iterator](./messages/iterator.md)

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Receiving data from other participants
- [func messages(of: Data.Type) -> GroupSessionMessenger.Messages<Data>](./messages%28of%29-626qo.md)
  Returns the asynchronous sequence of messages that contain a generic data object.
- [func messages<Message>(of: Message.Type) -> GroupSessionMessenger.Messages<Message>](./messages%28of%29-jvoz.md)
  Returns the asynchronous sequence of messages that match the app-specific type.
- [GroupSessionMessenger.MessageContext](./messagecontext.md)
  A structure that contains additional information about an incoming message, such as which device sent it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/messages)*