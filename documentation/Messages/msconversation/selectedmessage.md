# selectedMessage

**Framework**: Messages  
**Kind**: property  
**Role**: Instance Property

The message that the user selected in the conversation transcript.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var selectedMessage: MSMessage? { get }
```

```objc
@property (nonatomic, readonly, nullable) MSMessage * selectedMessage;
```

## Discussion

If the user selected one of your extension’s messages in the conversation transcript, this property is set to the selected message object. Otherwise, it is set to `nil`.

If your extension was launched because the user selected the message, then this property is set when the extension is launched.

If the user selects a message while your extension is running, the system takes the following steps:

1. Invokes your [`MSMessagesAppViewController`](../msmessagesappviewcontroller.md) object’s [`willSelect(_:conversation:)`](../msmessagesappviewcontroller/willselect%28_,conversation%29.md) method.
2. Updates the conversation’s `selectedMessage` property.
3. Invokes your [`MSMessagesAppViewController`](../msmessagesappviewcontroller.md) object’s [`didSelect(_:conversation:)`](../msmessagesappviewcontroller/didselect%28_,conversation%29.md) method.

Override [`willSelect(_:conversation:)`](../msmessagesappviewcontroller/willselect%28_,conversation%29.md) or [`didSelect(_:conversation:)`](../msmessagesappviewcontroller/didselect%28_,conversation%29.md) to handle changes to the selected message while your extension is active.

> **Note**:  This property is always set to the message object selected by the user. If this message belongs to a session, then the selected message might not contain the most current data. The selected message is not updated when you receive new messages. Instead, override your view controller’s [`didReceive(_:conversation:)`](../msmessagesappviewcontroller/didreceive%28_,conversation%29.md) message to handle updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msconversation/selectedmessage)*