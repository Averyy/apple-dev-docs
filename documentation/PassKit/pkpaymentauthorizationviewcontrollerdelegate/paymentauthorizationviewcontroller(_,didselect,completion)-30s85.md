# paymentAuthorizationViewController(_:didSelect:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user changed the payment method, and asks for an updated payment request.

**Availability**:
- iOS 9.0+ - Deprecated in 11.0
- iPadOS 9.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`paymentAuthorizationViewController(_:didSelect:handler:)`](./paymentauthorizationviewcontroller%28_,didselect,handler%29-3bex6.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect paymentMethod: PKPaymentMethod, completion: @escaping @Sendable ([PKPaymentSummaryItem]) -> Void)
```

*Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect paymentMethod: PKPaymentMethod) async -> [PKPaymentSummaryItem]
```

```objc
- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *) controller didSelectPaymentMethod:(PKPaymentMethod *) paymentMethod completion:(void (^)(NSArray<PKPaymentSummaryItem *> *summaryItems)) completion;
```

## Discussion

This method is called when the user has selected a new payment card.  Use this delegate callback to update the summary items in response to the card type changing (for example, applying credit card surcharges), and then call the callback with the updated summary items.

> **Note**:  The delegate receives no further callbacks except [`paymentAuthorizationViewControllerDidFinish(_:)`](./paymentauthorizationviewcontrollerdidfinish%28_%29.md) until it has invoked the completion block.

## Parameters

- `controller`: The payment authorization view controller.
- `paymentMethod`: The new payment method.
- `completion`: The completion block to call with the updated payment summary items.

  This block takes the following parameters:

  - **`summaryItems`**: An updated array of summary items that include any changes due to fees or credit card surcharges associated with the payment method.

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
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKPaymentMethod, handler: (PKPaymentRequestPaymentMethodUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,handler%29-3bex6.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:completion:)-30s85)*