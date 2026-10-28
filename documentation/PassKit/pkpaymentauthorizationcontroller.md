# PKPaymentAuthorizationController

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

An object that presents a sheet that prompts the user to authorize a payment request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKPaymentAuthorizationController
```

```objc
@interface PKPaymentAuthorizationController : NSObject
```

## Overview

After the user authorizes the payment request for a transaction, the delegate is called with a payment token used to authorize the transaction’s payment.

> ❗ **Important**:  The [`PKPaymentAuthorizationController`](./pkpaymentauthorizationcontroller.md) class performs the same role as the [`PKPaymentAuthorizationViewController`](./pkpaymentauthorizationviewcontroller.md) class, but it does not depend on the UIKit framework. This means that the authorization controller can be used in places where a view controller cannot (for example, in watchOS apps or in SiriKit extensions).

## Topics

### Creating a payment authorization controller
- [init(paymentRequest: PKPaymentRequest)](./pkpaymentauthorizationcontroller/init%28paymentrequest%29.md)
  Initializes and returns a payment authorization controller.
- [convenience init(disbursementRequest: PKDisbursementRequest)](./pkpaymentauthorizationcontroller/init%28disbursementrequest%29.md)
  Creates a new payment authorization controller with the disbursement request you provide.
### Determining whether the user can make payments or disbursements
- [class func canMakePayments() -> Bool](./pkpaymentauthorizationcontroller/canmakepayments%28%29.md)
  Returns whether the user can make payments.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork]) -> Bool](./pkpaymentauthorizationcontroller/canmakepayments%28usingnetworks%29.md)
  Returns whether the user can make payments through the specified network.
- [class func canMakePayments(usingNetworks: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](./pkpaymentauthorizationcontroller/canmakepayments%28usingnetworks,capabilities%29.md)
  Returns whether the user can make payments using a card from the specified network with the specified capabilities.
- [class func supportsDisbursements() -> Bool](./pkpaymentauthorizationcontroller/supportsdisbursements%28%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests.
- [class func supportsDisbursements(using: [PKPaymentNetwork]) -> Bool](./pkpaymentauthorizationcontroller/supportsdisbursements%28using%29.md)
  Returns a Boolean value that indicates whether this device can process disbursement requests using the specified payment network brands.
- [class func supportsDisbursements(using: [PKPaymentNetwork], capabilities: PKMerchantCapability) -> Bool](./pkpaymentauthorizationcontroller/supportsdisbursements%28using,capabilities%29.md)
  Returns a Boolean value indicating whether this device can process disbursement requests using the specified payment network brands and capabilities.
### Handling user interactions
- [var delegate: (any PKPaymentAuthorizationControllerDelegate)?](./pkpaymentauthorizationcontroller/delegate.md)
  The controller’s delegate.
- [protocol PKPaymentAuthorizationControllerDelegate](./pkpaymentauthorizationcontrollerdelegate.md)
  Methods that let you respond to user interactions with your payment authorization controller.
- [func present(completion: ((Bool) -> Void)?)](./pkpaymentauthorizationcontroller/present%28completion%29.md)
  Presents the payment sheet modally over your app.
- [func dismiss(completion: (() -> Void)?)](./pkpaymentauthorizationcontroller/dismiss%28completion%29.md)
  Dismisses the payment sheet.

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

### Apple Pay availability
- [class PKPaymentAuthorizationViewController](./pkpaymentauthorizationviewcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller)*