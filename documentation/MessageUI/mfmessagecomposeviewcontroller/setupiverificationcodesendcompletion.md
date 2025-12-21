# setUPIVerificationCodeSendCompletion(_:)

**Framework**: Message UI  
**Kind**: method

Configures the instance of a view for Unified Payments Interface (UPI) device validation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setUPIVerificationCodeSendCompletion(_ completion: @escaping (Bool) -> Void)
```

#### Discussion

If you use the [`com.apple.developer.upi-device-validation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.upi-device-validation) managed entitlement, [`setUPIVerificationCodeSendCompletion(_:)`](mfmessagecomposeviewcontroller/setupiverificationcodesendcompletion(_:).md) configures the instance of [`MFMessageComposeViewController`](mfmessagecomposeviewcontroller.md) with non-editable recipients and body fields.

> **Note**:  The [`setUPIVerificationCodeSendCompletion(_:)`](mfmessagecomposeviewcontroller/setupiverificationcodesendcompletion(_:).md) method is only functional on devices with SMS capability and is only compatible with recipients that don’t use iMessage.

The system invokes the completion handler on the main thread. It only invokes the completion handler after the [`MFMessageComposeViewController`](mfmessagecomposeviewcontroller.md) delegate’s [`messageComposeViewController(_:didFinishWith:)`](mfmessagecomposeviewcontrollerdelegate/messagecomposeviewcontroller(_:didfinishwith:).md) method gets called if a person sends the transaction.

The system calls the send completion handler with the transmission result of the message. The system won’t call the completion handler if:

- The device doesn’t have SMS capability.
- Your app doesn’t have the [`com.apple.developer.upi-device-validation`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.upi-device-validation) entitlement.
- The recipient can use iMessage or the person cancels the transaction.

The following code snippet is an example of how you can create an instance of [`MFMessageComposeViewController`](mfmessagecomposeviewcontroller.md), configure it with a UPI verification phone number and generated token, and set a completion block indicating the use of the controller for UPI device enrollment:

```swift
extension ViewController {
    func presentMessageComposer() {
        let composeController = MFMessageComposeViewController()
        composeController.messageComposeDelegate = self
        composeController.recipients = ["+14081234567"]
        composeController.body = "SomeDeviceVerificationCode123"
        composeController.setUPIVerificationCodeSendCompletion { result in
            NSLog("UPI send callback - message sent: \(result)")
        }
        
        present(composeController, animated: true)
    }
```

The following code snippet is the same as the one above, but in Objective-C:

```objc
@implementation ViewController (MessageComposer)

- (void)presentMessageComposer {
    MFMessageComposeViewController *composeController = [[MFMessageComposeViewController alloc] init];
    composeController.messageComposeDelegate = self;
    composeController.recipients = @[@"+14081234567"];
    composeController.body = @"SomeDeviceVerificationCode123";
    [composeController setUPIVerificationCodeSendCompletion:^(BOOL result) {
        NSLog(@"UPI send callback - message sent: %@", result ? @"YES" : @"NO");
    }];
}

@end
```

In addition, you need to use the existing [`messageComposeViewController(_:didFinishWith:)`](mfmessagecomposeviewcontrollerdelegate/messagecomposeviewcontroller(_:didfinishwith:).md) delegate method to dismiss the [`MFMessageComposeViewController`](mfmessagecomposeviewcontroller.md) instance because sending may take several seconds to complete. You can choose to allow people to continue interacting with your app or display a waiting UI. The following code snippet is an example of using [`messageComposeViewController(_:didFinishWith:)`](mfmessagecomposeviewcontrollerdelegate/messagecomposeviewcontroller(_:didfinishwith:).md)

```swift
extension ViewController: MFMessageComposeViewControllerDelegate {
    func messageComposeViewController(_ controller: MFMessageComposeViewController, didFinishWith result: MessageComposeResult) {
        NSLog("messageComposeViewController didFinishWithResult \(result)")
        controller.dismiss(animated: true)
    }
}

```

## Parameters

- `completion`: A block that’s invoked with a   to determine whether the message was sent. The send completion handler is invoked with   after the SMS successfully transmitted to the sender’s cellular carrier. If the SMS failed to send, the completion handler invoked with  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/setupiverificationcodesendcompletion(_:))*