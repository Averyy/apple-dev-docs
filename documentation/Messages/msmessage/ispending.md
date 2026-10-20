# isPending

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the message is pending or whether it has been sent or received.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isPending: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPending) BOOL pending;
```

#### Discussion

Use this property to determine whether an [`MSMessage`](../msmessage.md) instance represents an unsent message—for example, to determine whether the conversation’s [`selectedMessage`](../msconversation/selectedmessage.md) property refers to a message in the transcript ([`false`](../../Swift/false.md)) or to a message in the Messages app’s input field ([`true`](../../Swift/true.md)).

This property’s value is set based on the following rules:

- This property is set to [`true`](../../Swift/true.md) when your app calls the [`insert(_:completionHandler:)`](../msconversation/insert%28_,completionhandler%29-3g248.md) method to place the message in the Messages app’s input field.
- It’s set to [`false`](../../Swift/false.md) when the system calls the [`didStartSending(_:conversation:)`](../msmessagesappviewcontroller/didstartsending%28_,conversation%29.md) method (either because the user sent the message from the input field or because you called the [`send(_:completionHandler:)`](../msconversation/send%28_,completionhandler%29-9krz.md) method to send it directly).
- This property is set to [`false`](../../Swift/false.md) on messages received from other participants.

In other words, the property is [`true`](../../Swift/true.md) only for the selected method of the active conversation when there’s an [`MSMessagesAppViewController`](../msmessagesappviewcontroller.md) instance in the Messages app’s input field.

## See Also

### Message Properties
- [var accessibilityLabel: String?](./accessibilitylabel.md)
  A localized string that describes the message.
- [var error: (any Error)?](./error.md)
  An error object describing why the system failed to send the message.
- [var layout: MSMessageLayout?](./layout.md)
  A layout object that defines the message’s appearance.
- [var senderParticipantIdentifier: UUID](./senderparticipantidentifier.md)
  A UUID identifying the participant that sent the message.
- [var session: MSSession?](./session.md)
  The session that this message belongs to.
- [var shouldExpire: Bool](./shouldexpire.md)
  A Boolean value that determines whether the message should expire after being read.
- [var summaryText: String?](./summarytext.md)
  A succinct description of the message.
- [var url: URL?](./url.md)
  A URL that encodes data to be transmitted with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/ispending)*