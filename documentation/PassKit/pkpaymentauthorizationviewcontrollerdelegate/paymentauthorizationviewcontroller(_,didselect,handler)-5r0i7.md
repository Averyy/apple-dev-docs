# paymentAuthorizationViewController(_:didSelect:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a shipping method, and asks for an updated payment request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect shippingMethod: PKShippingMethod, handler completion: @escaping @Sendable (PKPaymentRequestShippingMethodUpdate) -> Void)
```

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect shippingMethod: PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate
```

```objc
- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *) controller didSelectShippingMethod:(PKShippingMethod *) shippingMethod handler:(void (^)(PKPaymentRequestShippingMethodUpdate *update)) completion;
```

#### Discussion

Use this method to update shipping costs based on the shipping address the user selected in a call to [`paymentAuthorizationViewController(_:didSelectShippingContact:handler:)`](./paymentauthorizationviewcontroller%28_,didselectshippingcontact,handler%29.md). If the user didn’t select an address, use the prepopulated address of the payment request.

When the system calls this method, you create a new array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that represent the updated cost including shipping. For more information on creating summary items, see the [`PKPaymentRequest`](../pkpaymentrequest.md) class’s [`paymentSummaryItems`](../pkpaymentrequest/paymentsummaryitems.md) property.

## Parameters

- `controller`: The payment authorization view controller.
- `shippingMethod`: The selected shipping method. This parameter contains one of the shipping methods specified in the payment request.
- `completion`: The completion handler to call with the updated payment summary items.

## See Also

### Handling shipping information
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didselectshippingcontact,handler%29.md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationviewcontroller%28_,didselectshippingcontact,completion%29.md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,completion%29-9otrj.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:handler:)-5r0i7)*