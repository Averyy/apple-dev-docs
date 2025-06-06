# paymentAuthorizationViewController(_:didSelect:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user selected a shipping method, and asks for an updated payment request.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect shippingMethod: PKShippingMethod) async -> (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem])
```

#### Discussion

Use this method to update shipping costs based on the shipping address selected by the user, as previously passed to the delegate in the [`PKPaymentAuthorizationViewControllerDelegate`](pkpaymentauthorizationviewcontrollerdelegate.md) method. If no address has been selected, use the prepopulated address on the payment request.

When this method is called, you create a new array of [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) objects that represent the updated cost including shipping. For more information on creating summary items, see the [`PKPaymentRequest`](pkpaymentrequest.md) class’s [`paymentSummaryItems`](pkpaymentrequest/paymentsummaryitems.md) property.

## Parameters

- `controller`: The payment authorization view controller.
- `shippingMethod`: The selected shipping method. This parameter contains one of the shipping methods included in the payment request.
- `completion`: This block takes the following parameters:

## See Also

- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingcontact:handler:).md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingcontact:completion:).md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:handler:)-5r0i7.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:completion:)-9otrj)*