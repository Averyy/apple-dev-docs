# paymentAuthorizationViewController(_:didSelectShippingContact:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a shipping address, and asks for an updated payment request.

**Availability**:
- iOS 9.0+ - Deprecated in 11.0
- iPadOS 9.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`paymentAuthorizationViewController(_:didSelectShippingContact:handler:)`](./paymentauthorizationviewcontroller%28_,didselectshippingcontact,handler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingContact contact: PKContact, completion: @escaping @Sendable (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)
```

*Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingContact contact: PKContact) async -> (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem])
```

```objc
- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *) controller didSelectShippingContact:(PKContact *) contact completion:(void (^)(PKPaymentAuthorizationStatus status, NSArray<PKShippingMethod *> *shippingMethods, NSArray<PKPaymentSummaryItem *> *summaryItems)) completion;
```

## Discussion

Use this method to update the available shipping methods and, if a shipping method has been selected, the current shipping cost.

When this method is called, you create a new array of valid [`PKShippingMethod`](../pkshippingmethod.md) objects for the specified address. You also create an array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that represent the updated cost. The summary items should include the shipping cost if a valid shipping method has been selected. For more information on updating these values, see the [`PKPaymentRequest`](../pkpaymentrequest.md) class’s [`shippingMethods`](../pkpaymentrequest/shippingmethods.md) and [`paymentSummaryItems`](../pkpaymentrequest/paymentsummaryitems.md) properties.

## Parameters

- `controller`: The payment authorization view controller.
- `contact`: A contact object representing the new shipping address. To maintain privacy, the shipping information is anonymized. For example, in the United States it only includes the city, state, and zip code. This provides enough information to calculate shipping costs, without revealing sensitive information until the user actually approves the purchase.
- `completion`: The completion block to call with the updated payment summary items and shipping methods.

  This block takes the following parameters:

  - **`status`**: The authorization status for the payment. For values, see [`PKPaymentAuthorizationViewControllerDelegate`](../pkpaymentauthorizationviewcontrollerdelegate.md).
  - **`shippingMethods`**: An array of [`PKShippingMethod`](../pkshippingmethod.md) objects that replaces the shipping methods for the current payment request.
  - **`summaryItems`**: An array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that replaces the summary items for the current payment request.

## See Also

### Handling shipping information
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didselectshippingcontact,handler%29.md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,handler%29-5r0i7.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,completion%29-9otrj.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingcontact:completion:))*