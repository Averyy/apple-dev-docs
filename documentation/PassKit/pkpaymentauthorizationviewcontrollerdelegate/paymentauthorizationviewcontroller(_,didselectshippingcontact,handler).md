# paymentAuthorizationViewController(_:didSelectShippingContact:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a shipping address, and asks for an updated payment request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingContact contact: PKContact, handler completion: @escaping @Sendable (PKPaymentRequestShippingContactUpdate) -> Void)
```

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingContact contact: PKContact) async -> PKPaymentRequestShippingContactUpdate
```

```objc
- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *) controller didSelectShippingContact:(PKContact *) contact handler:(void (^)(PKPaymentRequestShippingContactUpdate *update)) completion;
```

## Discussion

Use this method to update the available shipping methods by creating a new array of valid [`PKShippingMethod`](../pkshippingmethod.md) objects for the specified address. You also create an array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that represent the updated cost if the user selected a valid shipping method. For more information on updating these values, see the [`PKPaymentRequest`](../pkpaymentrequest.md) class’s [`shippingMethods`](../pkpaymentrequest/shippingmethods.md) and [`paymentSummaryItems`](../pkpaymentrequest/paymentsummaryitems.md) properties.

## Parameters

- `controller`: The payment authorization view controller.
- `contact`: A contact object that represents the new shipping address. To maintain privacy, the shipping information is anonymized. For example, in the United States it only includes the city, state, and zip code. This information provides enough detail to calculate shipping costs, without revealing sensitive information until the user actually approves the purchase.
- `completion`: The completion handler to call with the updated payment summary items and shipping methods.

## See Also

### Handling shipping information
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationviewcontroller%28_,didselectshippingcontact,completion%29.md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,handler%29-5r0i7.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,completion%29-9otrj.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingcontact:handler:))*