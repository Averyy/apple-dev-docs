# paymentAuthorizationViewController(_:didSelect:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user changed the payment method, and asks for an updated payment request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect paymentMethod: PKPaymentMethod, handler completion: @escaping @Sendable (PKPaymentRequestPaymentMethodUpdate) -> Void)
```

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect paymentMethod: PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate
```

```objc
- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *) controller didSelectPaymentMethod:(PKPaymentMethod *) paymentMethod handler:(void (^)(PKPaymentRequestPaymentMethodUpdate *update)) completion;
```

## Discussion

The system calls this method when the user selects a new payment card.  Use this delegate callback to update the summary items in response to the card type changing (for example, applying credit card surcharges), and then call the handler with the updated summary items.

## Parameters

- `controller`: The payment authorization view controller.
- `paymentMethod`: The new payment method.
- `completion`: The completion handler to call with the updated payment summary items.

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
- [func paymentAuthorizationViewControllerDidFinish(PKPaymentAuthorizationViewController)](./paymentauthorizationviewcontrollerdidfinish%28_%29.md)
  Tells the delegate that payment authorization finished.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,completion%29-30s85.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:handler:)-3bex6)*