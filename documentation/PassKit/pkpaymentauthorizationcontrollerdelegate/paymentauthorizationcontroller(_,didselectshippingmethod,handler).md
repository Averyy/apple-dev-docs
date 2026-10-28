# paymentAuthorizationController(_:didSelectShippingMethod:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user selected a shipping method.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@MainActor
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectShippingMethod shippingMethod: PKShippingMethod, handler completion: @escaping (PKPaymentRequestShippingMethodUpdate) -> Void)
```

```swift
@MainActor
optional func paymentAuthorizationController(_ controller: PKPaymentAuthorizationController, didSelectShippingMethod shippingMethod: PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate
```

```objc
- (void) paymentAuthorizationController:(PKPaymentAuthorizationController *) controller didSelectShippingMethod:(PKShippingMethod *) shippingMethod handler:(void (^)(PKPaymentRequestShippingMethodUpdate *requestUpdate)) completion;
```

## Discussion

Use this method to update shipping costs based on the shipping address the user selected, as previously passed to the delegate in the [`paymentAuthorizationController(_:didSelectShippingContact:handler:)`](./paymentauthorizationcontroller%28_,didselectshippingcontact,handler%29.md) method. If the user didn’t select an address, use the prepopulated address on the payment request.

When the system calls this method, you create a new array of [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) objects that represent the updated cost including shipping. For more information on creating summary items, see the [`PKPaymentRequest`](../pkpaymentrequest.md) class’s [`paymentSummaryItems`](../pkpaymentrequest/paymentsummaryitems.md) property.

## Parameters

- `controller`: The payment authorization controller.
- `shippingMethod`: The selected shipping method. This parameter contains one of the shipping methods included in the payment request.
- `completion`: The completion handler to call with the updated payment summary items.

## See Also

### Handling shipping information
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, handler: (PKPaymentRequestShippingContactUpdate) -> Void)](./paymentauthorizationcontroller%28_,didselectshippingcontact,handler%29.md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingContact: PKContact, completion: (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationcontroller%28_,didselectshippingcontact,completion%29.md)
  Tells the delegate that the user selected a shipping address.
- [func paymentAuthorizationController(PKPaymentAuthorizationController, didSelectShippingMethod: PKShippingMethod, completion: (PKPaymentAuthorizationStatus, [PKPaymentSummaryItem]) -> Void)](./paymentauthorizationcontroller%28_,didselectshippingmethod,completion%29.md)
  Tells the delegate that the user selected a shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontrollerdelegate/paymentauthorizationcontroller(_:didselectshippingmethod:handler:))*