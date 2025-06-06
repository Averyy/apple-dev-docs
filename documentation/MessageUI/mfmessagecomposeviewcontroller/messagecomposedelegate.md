# messageComposeDelegate

**Framework**: Message UI  
**Kind**: property

The delegate to which message-related notifications should be sent.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var messageComposeDelegate: MFMessageComposeViewControllerDelegate? { get set }
```

#### Discussion

When the user taps a button to send or cancel the message, your delegate is notified and should respond by dismissing the message composition interface. For more information about implementing the methods of your delegate object, see [`MFMessageComposeViewControllerDelegate`](mfmessagecomposeviewcontrollerdelegate.md).

## See Also

- [protocol MFMessageComposeViewControllerDelegate](mfmessagecomposeviewcontrollerdelegate.md)
  An interface for responding to user interactions with a message compose view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/messagecomposedelegate)*