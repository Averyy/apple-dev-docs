# PKPaymentAuthorizationViewControllerDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol  
**Role**: Protocol

Methods that let you respond to user interactions with your payment authorization view controller.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
protocol PKPaymentAuthorizationViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol PKPaymentAuthorizationViewControllerDelegate <NSObject>
```

## Overview

The [`PKPaymentAuthorizationViewControllerDelegate`](./pkpaymentauthorizationviewcontrollerdelegate.md) protocol is implemented by the payment authorization view controller’s delegate. You implement this protocol to respond to user interaction with that view controller.

The payment authorization view controller automatically waits for its delegate to finish responding to one method before it calls other delegate methods. You indicate that the delegate is finished with the current method by calling that method’s completion block. This action tells the pay authorization view controller to proceed with the next step in the authorization process.

There is one exception to this step-by-step procedure: The pay authorization view controller calls the [`paymentAuthorizationViewControllerDidFinish(_:)`](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontrollerdidfinish%28_%29.md) method as soon as the user cancels a payment without authorizing a payment request, or when a payment is canceled after timing out. The controller can call this method at any time.

## Topics

### Handling user’s payment authorization
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didrequestmerchantsessionupdate%29.md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationViewControllerWillAuthorizePayment(PKPaymentAuthorizationViewController)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontrollerwillauthorizepayment%28_%29.md)
  Tells the delegate that the user is authorizing the payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didauthorizepayment,handler%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didauthorizepayment,completion%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationViewControllerDidFinish(PKPaymentAuthorizationViewController)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontrollerdidfinish%28_%29.md)
  Tells the delegate that payment authorization finished.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, handler: (PKPaymentRequestPaymentMethodUpdate) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didselect,handler%29-3bex6.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didselect,completion%29-30s85.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.
### Handling coupons
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didChangeCouponCode: String, handler: (PKPaymentRequestCouponCodeUpdate) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didchangecouponcode,handler%29.md)
  Tells the delegate that the user entered or updated a coupon code.
### Handling shipping information
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didselectshippingcontact,handler%29.md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didselectshippingcontact,completion%29.md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didselect,handler%29-5r0i7.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didselect,completion%29-9otrj.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.
### Deprecated
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingAddress: ABRecord, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](./pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller%28_,didselectshippingaddress,completion%29.md)
  Tells the delegate that the user selected a shipping address.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling user interactions
- [var delegate: (any PKPaymentAuthorizationViewControllerDelegate)?](./pkpaymentauthorizationviewcontroller/delegate.md)
  The view controller’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate)*