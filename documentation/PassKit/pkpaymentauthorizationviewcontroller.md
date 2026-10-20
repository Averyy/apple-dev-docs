# PKPaymentAuthorizationViewController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

An object that presents a sheet that prompts the user to authorize a payment request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class PKPaymentAuthorizationViewController
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@interface PKPaymentAuthorizationViewController : UIViewController
```

*macOS*

```objc
@interface PKPaymentAuthorizationViewController : NSViewController
```

#### Overview

After the user authorizes the payment request for a transaction, the delegate is called with a payment token used to authorize the transaction’s payment.

## Topics

### Determining whether the user can make payments
- [class func canMakePayments() -> Bool](./pkpaymentauthorizationviewcontroller/canmakepayments%28%29.md)
  Returns whether the user can make payments.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool](./pkpaymentauthorizationviewcontroller/canmakepayments%28usingnetworks%29.md)
  Returns whether the user can make payments through the specified network.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](./pkpaymentauthorizationviewcontroller/canmakepayments%28usingnetworks,capabilities%29.md)
  Returns whether the user can make payments using a card from the specified network with the specified capabilities.
- [class func supportsDisbursements() -> Bool](./pkpaymentauthorizationviewcontroller/supportsdisbursements%28%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests.
- [class func supportsDisbursements(using: [PKPaymentNetwork]) -> Bool](./pkpaymentauthorizationviewcontroller/supportsdisbursements%28using%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment networks.
- [class func supportsDisbursements(using: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](./pkpaymentauthorizationviewcontroller/supportsdisbursements%28using,capabilities%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment networks and merchant capabilities.
### Handling user interactions
- [var delegate: (any PKPaymentAuthorizationViewControllerDelegate)?](./pkpaymentauthorizationviewcontroller/delegate.md)
  The view controller’s delegate.
- [protocol PKPaymentAuthorizationViewControllerDelegate](./pkpaymentauthorizationviewcontrollerdelegate.md)
  Methods that let you respond to user interactions with your payment authorization view controller.
### Creating a payment authorization view controller
- [init?(paymentRequest: PKPaymentRequest)](./pkpaymentauthorizationviewcontroller/init%28paymentrequest%29.md)
  Initializes and returns a payment authorization view controller.
- [convenience init(disbursementRequest: PKDisbursementRequest)](./pkpaymentauthorizationviewcontroller/init%28disbursementrequest%29.md)
  Initializes and returns a new payment authorization view controller with the provided disbursement request.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Apple Pay availability
- [class PKPaymentAuthorizationController](./pkpaymentauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontroller)*