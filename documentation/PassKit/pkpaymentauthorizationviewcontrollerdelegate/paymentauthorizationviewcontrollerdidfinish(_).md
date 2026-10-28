# paymentAuthorizationViewControllerDidFinish(_:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate that payment authorization finished.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func paymentAuthorizationViewControllerDidFinish(_ controller: PKPaymentAuthorizationViewController)
```

```objc
- (void) paymentAuthorizationViewControllerDidFinish:(PKPaymentAuthorizationViewController *) controller;
```

## Discussion

This delegate method is called every time a payment finishes. A payment may finish because authorization was completed in [`paymentAuthorizationViewController(_:didAuthorizePayment:handler:)`](./paymentauthorizationviewcontroller%28_,didauthorizepayment,handler%29.md), because authorization timed out, or because the user canceled the payment.

> ❗ **Important**:  Make any needed payment-related updates to your app’s state in this delegate method, especially if the payment is canceled or times out. Also, be sure to call [`dismiss(completion:)`](../pkpaymentauthorizationcontroller/dismiss%28completion%29.md) on the payment authorization view controller.

## Parameters

- `controller`: The payment authorization view controller.

## See Also

### Handling user’s payment authorization
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didrequestmerchantsessionupdate%29.md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationViewControllerWillAuthorizePayment(PKPaymentAuthorizationViewController)](./paymentauthorizationviewcontrollerwillauthorizepayment%28_%29.md)
  Tells the delegate that the user is authorizing the payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](./paymentauthorizationviewcontroller%28_,didauthorizepayment,handler%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](./paymentauthorizationviewcontroller%28_,didauthorizepayment,completion%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, handler: (PKPaymentRequestPaymentMethodUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,handler%29-3bex6.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,completion%29-30s85.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontrollerdidfinish(_:))*