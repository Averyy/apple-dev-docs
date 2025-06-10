# paymentAuthorizationController(_:didSelectShippingMethod:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user selected a shipping method.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectShippingMethod shippingMethod: PKShippingMethod) async -> (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem])
```

#### Discussion

Use this method to update shipping costs based on the shipping address selected by the user, as previously passed to the delegate in the [`paymentAuthorizationController(_:didSelectShippingContact:completion:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:completion:).md) method. If no address has been selected, use the prepopulated address on the payment request.

When this method is called, you create a new array of [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) objects that represent the updated cost including shipping. For more information on creating summary items, see the [`PKPaymentRequest`](pkpaymentrequest.md) class’s [`paymentSummaryItems`](pkpaymentrequest/paymentsummaryitems.md) property.

> **Note**:  The delegate receives no further callbacks except [`paymentAuthorizationControllerDidFinish(_:)`](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontrollerdidfinish(_:).md) until it has invoked the completion block.

## Parameters

- `controller`: The payment authorization controller.
- `shippingMethod`: The selected shipping method. This parameter contains one of the shipping methods included in the payment request.
- `completion`: This block takes the following parameters:

## See Also

- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:handler:).md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:completion:).md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingmethod:handler:).md)
  Tells the delegate that the user selected a shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingmethod:completion:))*