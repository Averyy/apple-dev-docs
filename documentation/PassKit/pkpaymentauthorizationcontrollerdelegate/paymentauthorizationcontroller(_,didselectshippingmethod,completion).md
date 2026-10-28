# paymentAuthorizationController(_:didSelectShippingMethod:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a shipping method.

**Availability**:
- iOS 10.0+ - Deprecated in 11.0
- iPadOS 10.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 11.0+
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 4.0

> **Deprecated**: Use [`paymentAuthorizationController(_:didSelectShippingMethod:handler:)`](./paymentauthorizationcontroller%28_,didselectshippingmethod,handler%29.md)  instead.

## Declaration

*iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS*

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectShippingMethod shippingMethod: PKShippingMethod, completion: @escaping @Sendable (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)
```

*Mac Catalyst, macOS, visionOS*

```swift
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectShippingMethod shippingMethod: PKShippingMethod) async -> (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem])
```

```objc
- (void) paymentAuthorizationController:(PKPaymentAuthorizationController *) controller didSelectShippingMethod:(PKShippingMethod *) shippingMethod completion:(void (^)(PKPaymentAuthorizationStatus status, NSArray<PKPaymentSummaryItem *> *summaryItems)) completion;
```

## Discussion

Use this method to update shipping costs based on the shipping address selected by the user, as previously passed to the delegate in the [`paymentAuthorizationController(_:didSelectShippingContact:completion:)`](./paymentauthorizationcontroller%28_,didselectshippingcontact,completion%29.md) method. If no address has been selected, use the prepopulated address on the payment request.

When this method is called, you create a new array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that represent the updated cost including shipping. For more information on creating summary items, see the [`PKPaymentRequest`](../pkpaymentrequest.md) class’s [`paymentSummaryItems`](../pkpaymentrequest/paymentsummaryitems.md) property.

> **Note**:  The delegate receives no further callbacks except [`paymentAuthorizationControllerDidFinish(_:)`](./paymentauthorizationcontrollerdidfinish%28_%29.md) until it has invoked the completion block.

## Parameters

- `controller`: The payment authorization controller.
- `shippingMethod`: The selected shipping method. This parameter contains one of the shipping methods included in the payment request.
- `completion`: The completion block to call with the updated payment summary items.

  This block takes the following parameters:

  - **`status`**: The authorization status for the payment. For values, see [`paymentAuthorizationControllerDidFinish(_:)`](./paymentauthorizationcontrollerdidfinish%28_%29.md).
  - **`summaryItems`**: An array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that replaces the summary items for the current payment request.

## See Also

### Handling shipping information
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](./paymentauthorizationcontroller%28_,didselectshippingcontact,handler%29.md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationcontroller%28_,didselectshippingcontact,completion%29.md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, handler: (PKPaymentRequestShippingMethodUpdate) -> Void)](./paymentauthorizationcontroller%28_,didselectshippingmethod,handler%29.md)
  Tells the delegate that the user selected a shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingmethod:completion:))*