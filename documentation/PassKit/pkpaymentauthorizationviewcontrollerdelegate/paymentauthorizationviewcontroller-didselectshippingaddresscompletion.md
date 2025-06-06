# paymentAuthorizationViewController(_:didSelectShippingAddress:completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user selected a shipping address.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didSelectShippingAddress address: ABRecord, completion: @escaping (PKPaymentAuthorizationStatus, [PKShippingMethod], [PKPaymentSummaryItem]) -> Void)
```

#### Discussion

Use this method to update the available shipping methods and, if a shipping method has been selected, the current shipping cost.

When this method is called, you create a new array of valid [`PKShippingMethod`](pkshippingmethod.md) objects for the specified address. You also create an array of [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) objects that represent the updated cost. The summary items should include the shipping cost if a valid shipping method has been selected. For more information on updating these values, see the [`PKPaymentRequest`](pkpaymentrequest.md) class’s [`shippingMethods`](pkpaymentrequest/shippingmethods.md) and [`paymentSummaryItems`](pkpaymentrequest/paymentsummaryitems.md) properties.

## Parameters

- `controller`: The payment authorization view controller.
- `address`: An address book record representing the selected shipping method.
- `completion`: This block takes the following parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didselectshippingaddress:completion:))*