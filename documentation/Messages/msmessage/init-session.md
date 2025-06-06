# init(session:)

**Framework**: Messages  
**Kind**: init

Initializes a new message that is part of the provided session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(session: MSSession)
```

#### Return Value

A newly initialized message.

#### Discussion

Use this initializer to create an updatable message. Messages that are part of a session receive special treatment by the Messages app. When the app receives a message that is part of an existing session, the previous message is moved to the bottom of the transcript and updated with the new message’s content.

## Parameters

- `session`: The session object tracking an updatable exchange of messages.

## See Also

- [init()](msmessage/init.md)
  Initializes a new message that is not part of a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/init(session:))*