# isPending

**Framework**: Messages  
**Kind**: property

A Boolean value that indicates whether the message is pending or whether it has been sent or received.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isPending: Bool { get }
```

#### Discussion

Use this property to determine whether an [`MSMessage`](msmessage.md) instance represents an unsent message—for example, to determine whether the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property refers to a message in the transcript ([`false`](https://developer.apple.com/documentation/swift/false)) or to a message in the Messages app’s input field ([`true`](https://developer.apple.com/documentation/swift/true)).

This property’s value is set based on the following rules:

- This property is set to [`true`](https://developer.apple.com/documentation/swift/true) when your app calls the [`insert(_:completionHandler:)`](msconversation/insert(_:completionhandler:)-3g248.md) method to place the message in the Messages app’s input field.
- It’s set to [`false`](https://developer.apple.com/documentation/swift/false) when the system calls the [`didStartSending(_:conversation:)`](msmessagesappviewcontroller/didstartsending(_:conversation:).md) method (either because the user sent the message from the input field or because you called the [`send(_:completionHandler:)`](msconversation/send(_:completionhandler:)-9krz.md) method to send it directly).
- This property is set to [`false`](https://developer.apple.com/documentation/swift/false) on messages received from other participants.

In other words, the property is [`true`](https://developer.apple.com/documentation/swift/true) only for the selected method of the active conversation when there’s an [`MSMessagesAppViewController`](msmessagesappviewcontroller.md) instance in the Messages app’s input field.

## See Also

- [var accessibilityLabel: String?](msmessage/accessibilitylabel.md)
  A localized string that describes the message.
- [var error: (any Error)?](msmessage/error.md)
  An error object describing why the system failed to send the message.
- [var layout: MSMessageLayout?](msmessage/layout.md)
  A layout object that defines the message’s appearance.
- [var senderParticipantIdentifier: UUID](msmessage/senderparticipantidentifier.md)
  A UUID identifying the participant that sent the message.
- [var session: MSSession?](msmessage/session.md)
  The session that this message belongs to.
- [var shouldExpire: Bool](msmessage/shouldexpire.md)
  A Boolean value that determines whether the message should expire after being read.
- [var summaryText: String?](msmessage/summarytext.md)
  A succinct description of the message.
- [var url: URL?](msmessage/url.md)
  A URL that encodes data to be transmitted with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/ispending)*