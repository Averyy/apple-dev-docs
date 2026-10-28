# paymentAuthorizationViewController(_:didSelectShippingAddress:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a shipping address.

**Availability**:
- iOS 8.0+ - Deprecated in 9.0
- iPadOS 8.0+ - Deprecated in 9.0

> **Deprecated**: This method is deprecated. Use [`paymentAuthorizationViewController(_:didSelectShippingContact:completion:)`](./paymentauthorizationviewcontroller%28_,didselectshippingcontact,completion%29.md) instead.

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingAddress address: ABRecord, completion: @escaping @Sendable (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)
```

```objc
- (void) paymentAuthorizationViewController:(PKPaymentAuthorizationViewController *) controller didSelectShippingAddress:(ABRecordRef) address completion:(void (^)(PKPaymentAuthorizationStatus status, NSArray<PKShippingMethod *> *shippingMethods, NSArray<PKPaymentSummaryItem *> *summaryItems)) completion;
```

## Discussion

Use this method to update the available shipping methods and, if a shipping method has been selected, the current shipping cost.

When this method is called, you create a new array of valid [`PKShippingMethod`](../pkshippingmethod.md) objects for the specified address. You also create an array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that represent the updated cost. The summary items should include the shipping cost if a valid shipping method has been selected. For more information on updating these values, see the [`PKPaymentRequest`](../pkpaymentrequest.md) class’s [`shippingMethods`](../pkpaymentrequest/shippingmethods.md) and [`paymentSummaryItems`](../pkpaymentrequest/paymentsummaryitems.md) properties.

## Parameters

- `controller`: The payment authorization view controller.
- `address`: An address book record representing the selected shipping method.
- `completion`: The completion block to be called with updated shipping information.

  This block takes the following parameters:

  - **`status`**: The authorization status for the payment. For values, see [`PKPaymentAuthorizationViewControllerDelegate`](../pkpaymentauthorizationviewcontrollerdelegate.md).
  - **`shippingMethods`**: An array of [`PKShippingMethod`](../pkshippingmethod.md) objects that replaces the shipping methods for the current payment request.
  - **`summaryItems`**: An array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that replaces the summary items for the current payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingaddress:completion:))*