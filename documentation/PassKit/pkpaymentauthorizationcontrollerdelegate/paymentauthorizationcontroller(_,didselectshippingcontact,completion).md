# paymentAuthorizationController(_:didSelectShippingContact:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a shipping address.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`paymentAuthorizationController(_:didSelectShippingContact:handler:)`](./paymentauthorizationcontroller%28_,didselectshippingcontact,handler%29.md) instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS*

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectShippingContact contact: PKContact, completion: @escaping @Sendable (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)
```

*Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectShippingContact contact: PKContact) async -> (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem])
```

```objc
- (void) paymentAuthorizationController:(PKPaymentAuthorizationController *) controller didSelectShippingContact:(PKContact *) contact completion:(void (^)(PKPaymentAuthorizationStatus status, NSArray<PKShippingMethod *> *shippingMethods, NSArray<PKPaymentSummaryItem *> *summaryItems)) completion;
```

## Discussion

Use this method to update the available shipping methods and, if a shipping method has been selected, the current shipping cost.

When this method is called, you create a new array of valid [`PKShippingMethod`](../pkshippingmethod.md) objects for the specified address. You also create an array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that represent the updated cost. The summary items should include the shipping cost if a valid shipping method has been selected. For more information on updating these values, see the [`PKPaymentRequest`](../pkpaymentrequest.md) class’s [`shippingMethods`](../pkpaymentrequest/shippingmethods.md) and [`paymentSummaryItems`](../pkpaymentrequest/paymentsummaryitems.md) properties.

> **Note**:  The delegate receives no further callbacks except [`paymentAuthorizationControllerDidFinish(_:)`](./paymentauthorizationcontrollerdidfinish%28_%29.md) until it has invoked the completion block.

## Parameters

- `controller`: The payment authorization controller.
- `contact`: A contact object representing the new shipping address. To maintain privacy, the shipping information is anonymized. For example, in the United States it only includes the city, state, and zip code. This provides enough information to calculate shipping costs, without revealing sensitive information until the user actually approves the purchase.
- `completion`: The completion block to call with the updated payment summary items and shipping methods.

  This block takes the following parameters:

  - **`status`**: The authorization status for the payment. For values, see [`PKPaymentAuthorizationControllerDelegate`](../pkpaymentauthorizationcontrollerdelegate.md).
  - **`shippingMethods`**: An array of [`PKShippingMethod`](../pkshippingmethod.md) objects that replaces the shipping methods for the current payment request.
  - **`summaryItems`**: An array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that replaces the summary items for the current payment request.

## See Also

### Handling shipping information
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](./paymentauthorizationcontroller%28_,didselectshippingcontact,handler%29.md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](./paymentauthorizationcontroller%28_,didselectshippingmethod,handler%29.md)
  Tells the delegate that the user selected a shipping method.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationcontroller%28_,didselectshippingmethod,completion%29.md)
  Tells the delegate that the user selected a shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingcontact:completion:))*