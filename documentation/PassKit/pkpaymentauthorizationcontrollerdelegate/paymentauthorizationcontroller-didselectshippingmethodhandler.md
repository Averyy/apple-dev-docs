# paymentAuthorizationController(_:didSelectShippingMethod:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user selected a shipping method.

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
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectShippingMethod shippingMethod: PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate
```

#### Discussion

Use this method to update shipping costs based on the shipping address the user selected, as previously passed to the delegate in the [`paymentAuthorizationController(_:didSelectShippingContact:handler:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:handler:).md) method. If the user didn’t select an address, use the prepopulated address on the payment request.

When the system calls this method, you create a new array of [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) objects that represent the updated cost including shipping. For more information on creating summary items, see the [`PKPaymentRequest`](pkpaymentrequest.md) class’s [`paymentSummaryItems`](pkpaymentrequest/paymentsummaryitems.md) property.

## Parameters

- `controller`: The payment authorization controller.
- `shippingMethod`: The selected shipping method. This parameter contains one of the shipping methods included in the payment request.
- `completion`: The completion handler to call with the updated payment summary items.

## See Also

- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:handler:).md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:completion:).md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingmethod:completion:).md)
  Tells the delegate that the user selected a shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingmethod:handler:))*