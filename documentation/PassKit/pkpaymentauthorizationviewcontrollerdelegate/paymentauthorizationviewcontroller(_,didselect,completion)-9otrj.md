# paymentAuthorizationViewController(_:didSelect:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a shipping method, and asks for an updated payment request.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use  [`paymentAuthorizationViewController(_:didSelect:handler:)`](./paymentauthorizationviewcontroller%28_,didselect,handler%29-5r0i7.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect shippingMethod: PKShippingMethod, completion: @escaping @Sendable (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)
```

*Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelect shippingMethod: PKShippingMethod) async -> (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem])
```

```objc
- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *) controller didSelectShippingMethod:(PKShippingMethod *) shippingMethod completion:(void (^)(PKPaymentAuthorizationStatus status, NSArray<PKPaymentSummaryItem *> *summaryItems)) completion;
```

#### Discussion

Use this method to update shipping costs based on the shipping address selected by the user, as previously passed to the delegate in the [`PKPaymentAuthorizationViewControllerDelegate`](../pkpaymentauthorizationviewcontrollerdelegate.md) method. If no address has been selected, use the prepopulated address on the payment request.

When this method is called, you create a new array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that represent the updated cost including shipping. For more information on creating summary items, see the [`PKPaymentRequest`](../pkpaymentrequest.md) class’s [`paymentSummaryItems`](../pkpaymentrequest/paymentsummaryitems.md) property.

## Parameters

- `controller`: The payment authorization view controller.
- `shippingMethod`: The selected shipping method. This parameter contains one of the shipping methods included in the payment request.
- `completion`: The completion block to call with the updated payment summary items.

  This block takes the following parameters:

  - **`status`**: The authorization status for the payment. For values, see [`PKPaymentAuthorizationStatus`](../pkpaymentauthorizationstatus.md).
  - **`summaryItems`**: An array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that replaces the summary items for the current payment request.

## See Also

### Handling shipping information
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didselectshippingcontact,handler%29.md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationviewcontroller%28_,didselectshippingcontact,completion%29.md)
  Tells the delegate that the user selected a shipping address, and asks for an updated payment request.
- [func paymentAuthorizationViewController(PKPaymentAuthorizationViewController, didSelect: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](./paymentauthorizationviewcontroller%28_,didselect,handler%29-5r0i7.md)
  Tells the delegate that the user selected a shipping method, and asks for an updated payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselect:completion:)-9otrj)*