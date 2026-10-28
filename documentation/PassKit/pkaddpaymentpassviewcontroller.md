# PKAddPaymentPassViewController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

Displays an interface that lets users add cards to Apple Pay from within your app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class PKAddPaymentPassViewController
```

```objc
@interface PKAddPaymentPassViewController : UIViewController
```

## Overview

> ❗ **Important**:  Adding payment passes requires a special entitlement issued by Apple. Your app must include this entitlement before this class can be instantiated. For more information on requesting this entitlement, see the Card Issuers section at [developer.apple.com/apple-pay/](https://developer.apple.com/apple-pay/).

## Topics

### Determining if payment passes can be added
- [class func canAddPaymentPass() -> Bool](./pkaddpaymentpassviewcontroller/canaddpaymentpass%28%29.md)
  Returns a Boolean value that indicates whether the app can add cards to Apple Pay.
### Working with add payment view controllers
- [var delegate: (any PKAddPaymentPassViewControllerDelegate)?](./pkaddpaymentpassviewcontroller/delegate.md)
  The object that acts as the delegate for the add payment view controller.
- [protocol PKAddPaymentPassViewControllerDelegate](./pkaddpaymentpassviewcontrollerdelegate.md)
  Methods that let the system prompt you for an add payment request, and inform you when a request has succeeded or failed.
### Creating an add-payment-pass view controller
- [init?(requestConfiguration: PKAddPaymentPassRequestConfiguration, delegate: (any PKAddPaymentPassViewControllerDelegate)?)](./pkaddpaymentpassviewcontroller/init%28requestconfiguration,delegate%29.md)
  Returns an initialized add payment view controller object, using the provided configuration and delegate.
- [class PKAddPaymentPassRequestConfiguration](./pkaddpaymentpassrequestconfiguration.md)
  Contains the configuration data for a view controller that lets the user add a payment pass.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
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

### Payment passes
- [class PKPaymentPass](./pkpaymentpass.md)
  An object that represents a provisioned payment card for in-app payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller)*