# paymentAuthorizationController(_:didSelectPaymentMethod:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user changed the payment method, and asks for an updated payment request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@MainActor
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectPaymentMethod paymentMethod: PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate
```

#### Discussion

The system calls this method when the user selects a payment card.  Use this delegate callback to update the summary items in response to the card type changing (for example, applying credit card surcharges), and then call the completion handler with the updated summary items.

## Parameters

- `controller`: The payment authorization controller.
- `paymentMethod`: The selected payment method.
- `completion`: The completion handler to call with the updated payment summary items.

## See Also

- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectPaymentMethod: PKPaymentMethod, completion: ([PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectpaymentmethod:completion:).md)
  Tells the delegate that the user changed the payment method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectpaymentmethod:handler:))*