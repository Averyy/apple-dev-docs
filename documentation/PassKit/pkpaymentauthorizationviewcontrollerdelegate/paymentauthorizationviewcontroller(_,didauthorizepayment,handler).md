# paymentAuthorizationViewController(_:didAuthorizePayment:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user authorized the payment request, and asks for a result.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment, handler completion: @escaping @Sendable (PKPaymentAuthorizationResult) -> Void)
```

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didAuthorizePayment payment: PKPayment) async -> PKPaymentAuthorizationResult
```

```objc
- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *) controller didAuthorizePayment:(PKPayment *) payment handler:(void (^)(PKPaymentAuthorizationResult *result)) completion;
```

## Discussion

The system calls this method after it authorizes the payment request. You submit the payment information to your payment processor to authorize the transaction, and then call the completion handler.

## Parameters

- `controller`: The payment authorization view controller.
- `payment`: The authorized payment. This object contains the payment token you need to submit to your payment processor, as well as the billing and shipping information required by the payment request.
- `completion`: The completion handler to call with the result of authorizing the payment.

## See Also

### Handling user’s payment authorization
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didrequestmerchantsessionupdate%29.md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationViewControllerWillAuthorizePayment(PKPaymentAuthorizationViewController)](./paymentauthorizationviewcontrollerwillauthorizepayment%28_%29.md)
  Tells the delegate that the user is authorizing the payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](./paymentauthorizationviewcontroller%28_,didauthorizepayment,completion%29.md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationViewControllerDidFinish(PKPaymentAuthorizationViewController)](./paymentauthorizationviewcontrollerdidfinish%28_%29.md)
  Tells the delegate that payment authorization finished.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, handler: (PKPaymentRequestPaymentMethodUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,handler%29-3bex6.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,completion%29-30s85.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didauthorizepayment:handler:))*