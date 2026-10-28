# paymentAuthorizationController(_:didSelectPaymentMethod:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user changed the payment method, and asks for an updated payment request.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`paymentAuthorizationController(_:didSelectPaymentMethod:handler:)`](./paymentauthorizationcontroller%28_,didselectpaymentmethod,handler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS*

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectPaymentMethod paymentMethod: PKPaymentMethod, completion: @escaping @Sendable ([PKPaymentSummaryItem]) -> Void)
```

*Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectPaymentMethod paymentMethod: PKPaymentMethod) async -> [PKPaymentSummaryItem]
```

```objc
- (void) paymentAuthorizationController:(PKPaymentAuthorizationController *) controller didSelectPaymentMethod:(PKPaymentMethod *) paymentMethod completion:(void (^)(NSArray<PKPaymentSummaryItem *> *summaryItems)) completion;
```

## Discussion

This method is called when the user has selected a new payment card.  Use this delegate callback to update the summary items in response to the card type changing (for example, applying credit card surcharges), and then call the callback with the updated summary items.

> **Note**:  The delegate receives no further callbacks except [`paymentAuthorizationControllerDidFinish(_:)`](./paymentauthorizationcontrollerdidfinish%28_%29.md) until it has invoked the completion block.

## Parameters

- `controller`: The payment authorization controller.
- `paymentMethod`: The new payment method.
- `completion`: The completion block to call with the updated payment summary items.

  This block takes the following parameters:

  - **`summaryItems`**: An updated array of summary items that include any changes due to fees or credit card surcharges associated with the payment method.

## See Also

### Handling user’s payment method selection
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectPaymentMethod: PKPaymentMethod, handler: (PKPaymentRequestPaymentMethodUpdate) -> Void)](./paymentauthorizationcontroller%28_,didselectpaymentmethod,handler%29.md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectpaymentmethod:completion:))*