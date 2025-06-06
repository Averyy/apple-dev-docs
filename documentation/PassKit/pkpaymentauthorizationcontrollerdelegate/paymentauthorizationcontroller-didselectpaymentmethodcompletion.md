# paymentAuthorizationController(_:didSelectPaymentMethod:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user changed the payment method, and asks for an updated payment request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectPaymentMethod paymentMethod: PKPaymentMethod) async -> [PKPaymentSummaryItem]
```

#### Discussion

This method is called when the user has selected a new payment card.  Use this delegate callback to update the summary items in response to the card type changing (for example, applying credit card surcharges), and then call the callback with the updated summary items.

> **Note**:  The delegate receives no further callbacks except [`paymentAuthorizationControllerDidFinish(_:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(_:).md) until it has invoked the completion block.

 The delegate receives no further callbacks except [`paymentAuthorizationControllerDidFinish(_:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(_:).md) until it has invoked the completion block.

## Parameters

- `controller`: The payment authorization controller.
- `paymentMethod`: The new payment method.
- `completion`: This block takes the following parameters:

## See Also

- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectPaymentMethod: PKPaymentMethod, handler: (PKPaymentRequestPaymentMethodUpdate) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectpaymentmethod:handler:).md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectpaymentmethod:completion:))*