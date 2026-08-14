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
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class PKPaymentPass](pkpaymentpass.md)
  An object that represents a provisioned payment card for in-app payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontroller)*