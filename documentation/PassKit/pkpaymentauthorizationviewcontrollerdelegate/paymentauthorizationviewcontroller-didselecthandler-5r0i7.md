# paymentAuthorizationViewController(_:didSelect:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user selected a shipping method, and asks for an updated payment request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect shippingMethod: PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate
```

#### Discussion

Use this method to update shipping costs based on the shipping address the user selected in a call to [`paymentAuthorizationViewController(_:didSelectShippingContact:handler:)`](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingcontact:handler:).md). If the user didn’t select an address, use the prepopulated address of the payment request.

When the system calls this method, you create a new array of [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) objects that represent the updated cost including shipping. For more information on creating summary items, see the [`PKPaymentRequest`](pkpaymentrequest.md) class’s [`paymentSummaryItems`](pkpaymentrequest/paymentsummaryitems.md) property.

## Parameters

- `controller`: The payment authorization view controller.
- `shippingMethod`: The selected shipping method. This parameter contains one of the shipping methods specified in the payment request.
- `completion`: The completion handler to call with the updated payment summary items.

## See Also

- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingcontact:handler:).md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingcontact:completion:).md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:completion:)-9otrj.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:handler:)-5r0i7)*