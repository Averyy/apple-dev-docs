# PKAddPaymentPassRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

Contains the card data needed to add a card to Apple Pay.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+

## Declaration

```swift
class PKAddPaymentPassRequest
```

```objc
@interface PKAddPaymentPassRequest : NSObject
```

## Overview

All sensitive data must be encrypted before being assigned to this object. Because the encryption keys vary depending on the server, create [`PKAddPaymentPassRequest`](./pkaddpaymentpassrequest.md) instances only when your [`PKAddPaymentPassViewControllerDelegate`](./pkaddpaymentpassviewcontrollerdelegate.md) object’s [`addPaymentPassViewController(_:generateRequestWithCertificateChain:nonce:nonceSignature:completionHandler:)`](./pkaddpaymentpassviewcontrollerdelegate/addpaymentpassviewcontroller%28_,generaterequestwithcertificatechain,nonce,noncesignature,completionhandler%29.md) method is called. The required server certificates are provided at that time.

> ❗ **Important**:  Adding payment passes requires a special entitlement issued by Apple. Your app must include this entitlement before you can use this class. For more information on requesting this entitlement, see the Card Issuers section at [developer.apple.com/apple-pay/](https://developer.apple.com/apple-pay/).

## Topics

### Creating an add payment pass request
- [init()](./pkaddpaymentpassrequest/init%28%29.md)
### Accessing request data
- [var activationData: Data?](./pkaddpaymentpassrequest/activationdata.md)
  The request’s activation data.
- [var encryptedPassData: Data?](./pkaddpaymentpassrequest/encryptedpassdata.md)
  An encrypted JSON file containing the sensitive information needed to add a card to Apple Pay.
- [var ephemeralPublicKey: Data?](./pkaddpaymentpassrequest/ephemeralpublickey.md)
  The ephemeral public key used by elliptic curve cryptography (ECC).
- [var wrappedKey: Data?](./pkaddpaymentpassrequest/wrappedkey.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Requesting to add payment cards to Apple Pay
- [func addPaymentPassViewController(PKAddPaymentPassViewController, generateRequestWithCertificateChain: [Data], nonce: Data, nonceSignature: Data, completionHandler: (PKAddPaymentPassRequest) -> Void)](./pkaddpaymentpassviewcontrollerdelegate/addpaymentpassviewcontroller%28_,generaterequestwithcertificatechain,nonce,noncesignature,completionhandler%29.md)
  Asks the delegate to create an add payment request.
- [func addPaymentPassViewController(PKAddPaymentPassViewController, didFinishAdding: PKPaymentPass?, error: (any Error)?)](./pkaddpaymentpassviewcontrollerdelegate/addpaymentpassviewcontroller%28_,didfinishadding,error%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkaddpaymentpassrequest)*