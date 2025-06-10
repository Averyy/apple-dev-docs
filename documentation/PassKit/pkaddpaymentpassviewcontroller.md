# PKAddPaymentPassViewController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

Displays an interface that lets users add cards to Apple Pay from within your app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class PKAddPaymentPassViewController
```

#### Overview

> ❗ **Important**:  Adding payment passes requires a special entitlement issued by Apple. Your app must include this entitlement before this class can be instantiated. For more information on requesting this entitlement, see the Card Issuers section at [`developer.apple.com/apple-pay/`](https://developer.apple.comhttps://developer.apple.com/apple-pay/).

## Topics

### Determining if payment passes can be added
- [class func canAddPaymentPass() -> Bool](pkaddpaymentpassviewcontroller/canaddpaymentpass.md)
  Returns a Boolean value that indicates whether the app can add cards to Apple Pay.
### Working with add payment view controllers
- [var delegate: (any PKAddPaymentPassViewControllerDelegate)?](pkaddpaymentpassviewcontroller/delegate.md)
  The object that acts as the delegate for the add payment view controller.
- [protocol PKAddPaymentPassViewControllerDelegate](pkaddpaymentpassviewcontrollerdelegate.md)
  Methods that let the system prompt you for an add payment request, and inform you when a request has succeeded or failed.
### Creating an add-payment-pass view controller
- [init?(requestConfiguration: PKAddPaymentPassRequestConfiguration, delegate: (any PKAddPaymentPassViewControllerDelegate)?)](pkaddpaymentpassviewcontroller/init(requestconfiguration:delegate:).md)
  Returns an initialized add payment view controller object, using the provided configuration and delegate.
- [class PKAddPaymentPassRequestConfiguration](pkaddpaymentpassrequestconfiguration.md)
  Contains the configuration data for a view controller that lets the user add a payment pass.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class PKPaymentPass](pkpaymentpass.md)
  An object that represents a provisioned payment card for in-app payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller)*