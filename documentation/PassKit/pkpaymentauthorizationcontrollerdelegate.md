# PKPaymentAuthorizationControllerDelegate

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: protocol  
**Role**: Protocol

Methods that let you respond to user interactions with your payment authorization controller.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
protocol PKPaymentAuthorizationControllerDelegate : NSObjectProtocol
```

```objc
@protocol PKPaymentAuthorizationControllerDelegate <NSObject>
```

#### Overview

The [`PKPaymentAuthorizationControllerDelegate`](./pkpaymentauthorizationcontrollerdelegate.md) protocol is implemented by the payment authorization controller’s delegate. You implement this protocol to respond to user interaction with that controller.

In most cases, the payment authorization controller automatically waits for its delegate to finish responding to one method before it calls other delegate methods. You indicate that the delegate is finished with the current method by calling that method’s completion block. This action tells the pay authorization controller to proceed with the next step in the authorization process.

There is one exception to this step-by-step procedure: The pay authorization controller calls the [`paymentAuthorizationControllerDidFinish(_:)`](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish%28_%29.md) method as soon as the user cancels a payment without authorizing. The controller can call this method at any time.

## Topics

### Handling user interactions
- [func presentationWindow(for: PKPaymentAuthorizationController) -> UIWindow?](./pkpaymentauthorizationcontrollerdelegate/presentationwindow%28for%29.md)
  Returns the window in which to present a payment authorization sheet.
### Handling user’s payment method selection
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectPaymentMethod: PKPaymentMethod, handler: (PKPaymentRequestPaymentMethodUpdate) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didselectpaymentmethod,handler%29.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectPaymentMethod: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didselectpaymentmethod,completion%29.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.
### Handling coupons
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didChangeCouponCode: String, handler: (PKPaymentRequestCouponCodeUpdate) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didchangecouponcode,handler%29.md)
  Tells the delegate that the user entered or updated a coupon code.
### Handling shipping information
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didselectshippingcontact,handler%29.md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didselectshippingcontact,completion%29.md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didselectshippingmethod,handler%29.md)
  Tells the delegate that the user selected a shipping method.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didselectshippingmethod,completion%29.md)
  Tells the delegate that the user selected a shipping method.
### Handling user’s payment authorization
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didrequestmerchantsessionupdate%29.md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationControllerWillAuthorizePayment(PKPaymentAuthorizationController)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerwillauthorizepayment%28_%29.md)
  Tells the delegate that the user is authorizing the payment request.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didauthorizepayment,handler%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller%28_,didauthorizepayment,completion%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationControllerDidFinish(PKPaymentAuthorizationController)](./pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish%28_%29.md)
  Tells the delegate that payment authorization has completed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Handling user interactions
- [var delegate: (any PKPaymentAuthorizationControllerDelegate)?](./pkpaymentauthorizationcontroller/delegate.md)
  The controller’s delegate.
- [func present(completion: ((Bool) -> Void)?)](./pkpaymentauthorizationcontroller/present%28completion%29.md)
  Presents the payment sheet modally over your app.
- [func dismiss(completion: (() -> Void)?)](./pkpaymentauthorizationcontroller/dismiss%28completion%29.md)
  Dismisses the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate)*