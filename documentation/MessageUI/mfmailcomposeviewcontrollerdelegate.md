# MFMailComposeViewControllerDelegate

**Framework**: Message UI  
**Kind**: protocol

An interface for responding to user interactions with a mail compose view controller.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol MFMailComposeViewControllerDelegate : NSObjectProtocol
```

#### Overview

The [`MFMailComposeViewControllerDelegate`](mfmailcomposeviewcontrollerdelegate.md) protocol defines the method that your delegate must implement to manage the mail composition interface. The method of this protocol notifies your delegate object when the user has finished with the interface and is ready to dismiss it.

Your delegate object is responsible for dismissing the picker when the operation completes. You do this by using the [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/dismiss(animated:completion:)) method of the parent view controller, which is responsible for displaying the [`MFMailComposeViewController`](mfmailcomposeviewcontroller.md) object’s interface.

## Topics

### Responding to Email Completion
- [func mailComposeController(MFMailComposeViewController, didFinishWith: MFMailComposeResult, error: Error?)](mfmailcomposeviewcontrollerdelegate/mailcomposecontroller(_:didfinishwith:error:).md)
  Tells the delegate that the user wants to dismiss the mail composition view.
- [enum MFMailComposeResult](mfmailcomposeresult.md)
  Result codes returned when the mail composition interface is dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var mailComposeDelegate: MFMailComposeViewControllerDelegate?](mfmailcomposeviewcontroller/mailcomposedelegate.md)
  The mail composition view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontrollerdelegate)*