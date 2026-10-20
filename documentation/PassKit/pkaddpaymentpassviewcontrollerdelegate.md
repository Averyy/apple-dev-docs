# PKAddPaymentPassViewControllerDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol  
**Role**: Protocol

Methods that let the system prompt you for an add payment request, and inform you when a request has succeeded or failed.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol PKAddPaymentPassViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol PKAddPaymentPassViewControllerDelegate <NSObject>
```

#### Overview

Delegates for the [`PKAddPaymentPassViewController`](./pkaddpaymentpassviewcontroller.md) class must adopt this protocol.

> ❗ **Important**:  Adding payment passes requires a special entitlement issued by Apple. Your app must include this entitlement before you can use this class. For more information on requesting this entitlement, see the Card Issuers section at [developer.apple.com/apple-pay/](https://developer.apple.com/apple-pay/).

## Topics

### Requesting to add payment cards to Apple Pay
- [func addPaymentPassViewController(PKAddPaymentPassViewController, generateRequestWithCertificateChain: [Data], nonce: Data, nonceSignature: Data, completionHandler: (PKAddPaymentPassRequest) -> Void)](./pkaddpaymentpassviewcontrollerdelegate/addpaymentpassviewcontroller%28_,generaterequestwithcertificatechain,nonce,noncesignature,completionhandler%29.md)
  Asks the delegate to create an add payment request.
- [class PKAddPaymentPassRequest](./pkaddpaymentpassrequest.md)
  Contains the card data needed to add a card to Apple Pay.
- [func addPaymentPassViewController(PKAddPaymentPassViewController, didFinishAdding: PKPaymentPass?, error: (any Error)?)](./pkaddpaymentpassviewcontrollerdelegate/addpaymentpassviewcontroller%28_,didfinishadding,error%29.md)
### Payment pass errors
- [enum PKAddPaymentPassError](./pkaddpaymentpasserror.md)
  Error codes for adding payment passes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with add payment view controllers
- [var delegate: (any PKAddPaymentPassViewControllerDelegate)?](./pkaddpaymentpassviewcontroller/delegate.md)
  The object that acts as the delegate for the add payment view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassviewcontrollerdelegate)*