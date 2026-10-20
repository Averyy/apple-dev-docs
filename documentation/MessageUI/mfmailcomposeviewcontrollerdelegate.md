# MFMailComposeViewControllerDelegate

**Framework**: Message UI  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MFMailComposeViewControllerDelegate <NSObject>
```

#### Overview

The [`MFMailComposeViewControllerDelegate`](./mfmailcomposeviewcontrollerdelegate.md) protocol defines the method that your delegate must implement to manage the mail composition interface. The method of this protocol notifies your delegate object when the user has finished with the interface and is ready to dismiss it.

Your delegate object is responsible for dismissing the picker when the operation completes. You do this by using the [`dismiss(animated:completion:)`](../UIKit/uiviewcontroller/dismiss%28animated,completion%29.md) method of the parent view controller, which is responsible for displaying the [`MFMailComposeViewController`](./mfmailcomposeviewcontroller.md) object’s interface.

## Topics

### Responding to Email Completion
- [func mailComposeController(MFMailComposeViewController, didFinishWith: MFMailComposeResult, error: (any Error)?)](./mfmailcomposeviewcontrollerdelegate/mailcomposecontroller%28_,didfinishwith,error%29.md)
  Tells the delegate that the user wants to dismiss the mail composition view.
- [enum MFMailComposeResult](./mfmailcomposeresult.md)
  Result codes returned when the mail composition interface is dismissed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to the view controller dismissal
- [var mailComposeDelegate: (any MFMailComposeViewControllerDelegate)?](./mfmailcomposeviewcontroller/mailcomposedelegate.md)
  The mail composition view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontrollerdelegate)*