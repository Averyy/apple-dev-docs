# mailComposeDelegate

**Framework**: Message UI  
**Kind**: property  
**Role**: Instance Property

The mail composition view controller’s delegate.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
weak var mailComposeDelegate: (any MFMailComposeViewControllerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<MFMailComposeViewControllerDelegate> mailComposeDelegate;
```

## Discussion

The delegate object is responsible for dismissing the view presented by this view controller at the appropriate time. Therefore, you should always provide a delegate, and that object should implement the methods of the [`MFMailComposeViewControllerDelegate`](../mfmailcomposeviewcontrollerdelegate.md) protocol.

## See Also

### Responding to the view controller dismissal
- [protocol MFMailComposeViewControllerDelegate](../mfmailcomposeviewcontrollerdelegate.md)
  An interface for responding to user interactions with a mail compose view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/mailcomposedelegate)*