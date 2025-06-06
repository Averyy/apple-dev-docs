# paymentAuthorizationController(_:didSelectShippingContact:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user selected a shipping address.

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
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectShippingContact contact: PKContact) async -> PKPaymentRequestShippingContactUpdate
```

#### Discussion

Use this method to update the available shipping methods by creating a new array of valid [`PKShippingMethod`](pkshippingmethod.md) objects for the specified address. You also create an array of [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) objects that represent the updated cost if the user selects a valid shipping method. For more information on updating these values, see the [`PKPaymentRequest`](pkpaymentrequest.md) class’s [`shippingMethods`](pkpaymentrequest/shippingmethods.md) and [`paymentSummaryItems`](pkpaymentrequest/paymentsummaryitems.md) properties.

## Parameters

- `controller`: The payment authorization controller.
- `contact`: A contact object that represents the new shipping address. To maintain privacy, the shipping information is anonymized. For example, in the United States it only includes the city, state, and zip code. This provides enough information to calculate shipping costs, without revealing sensitive information until the user actually approves the purchase.
- `completion`: The completion handler to call with the updated payment summary items and shipping methods.

## See Also

- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:completion:).md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingmethod:handler:).md)
  Tells the delegate that the user selected a shipping method.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingmethod:completion:).md)
  Tells the delegate that the user selected a shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:handler:))*