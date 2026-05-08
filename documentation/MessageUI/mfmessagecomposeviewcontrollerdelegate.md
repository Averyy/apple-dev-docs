# MFMessageComposeViewControllerDelegate

**Framework**: Message UI  
**Kind**: protocol

An interface for responding to user interactions with a message compose view controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol MFMessageComposeViewControllerDelegate : NSObjectProtocol
```

#### Overview

The [`MFMessageComposeViewControllerDelegate`](mfmessagecomposeviewcontrollerdelegate.md) protocol defines a single method that custom objects can implement to respond to updates from a message composition view (an instance of the  [`MFMessageComposeViewController`](mfmessagecomposeviewcontroller.md) class). Use the method of this protocol to respond to the end of the user composing an SMS message. The method includes information about whether the user chose to send or cancel the message, or whether the attempt to send it failed.

## Topics

### Responding to the Message Completion
- [func messageComposeViewController(MFMessageComposeViewController, didFinishWith: MessageComposeResult)](mfmessagecomposeviewcontrollerdelegate/messagecomposeviewcontroller(_:didfinishwith:).md)
  Tells the delegate that the user finished composing the message.
- [enum MessageComposeResult](messagecomposeresult.md)
  These constants describe the result of the message-composition interface.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var messageComposeDelegate: (any MFMessageComposeViewControllerDelegate)?](mfmessagecomposeviewcontroller/messagecomposedelegate.md)
  The delegate to which message-related notifications should be sent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerdelegate)*