# paymentAuthorizationViewController(_:didSelect:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user changed the payment method, and asks for an updated payment request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect paymentMethod: PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate
```

#### Discussion

The system calls this method when the user selects a new payment card.  Use this delegate callback to update the summary items in response to the card type changing (for example, applying credit card surcharges), and then call the handler with the updated summary items.

## Parameters

- `controller`: The payment authorization view controller.
- `paymentMethod`: The new payment method.
- `completion`: The completion handler to call with the updated payment summary items.

## See Also

- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didRequestMerchantSessionUpdate: (PKPaymentRequestMerchantSessionUpdate) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didrequestmerchantsessionupdate:).md)
  Requests an object that validates the identity of a merchant for a payment request.
- [func paymentAuthorizationViewControllerWillAuthorizePayment(PKPaymentAuthorizationViewController)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontrollerwillauthorizepayment(_:).md)
  Tells the delegate that the user is authorizing the payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didAuthorizePayment: PKPayment, handler: (PKPaymentAuthorizationResult) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didauthorizepayment:handler:).md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didAuthorizePayment: PKPayment, completion: (PKPaymentAuthorizationStatus) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didauthorizepayment:completion:).md)
  Tells the delegate that the user authorized the payment request, and asks for a result.
- [func paymentAuthorizationViewControllerDidFinish(PKPaymentAuthorizationViewController)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontrollerdidfinish(_:).md)
  Tells the delegate that payment authorization finished.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:completion:)-30s85.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:handler:)-3bex6)*