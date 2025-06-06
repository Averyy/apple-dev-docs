# init(errors:paymentSummaryItems:shippingMethods:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a payment coupon update with your specified payment summary items, errors, and shipping methods.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(errors: [any Error]?, paymentSummaryItems: [PKPaymentSummaryItem], shippingMethods: [PKShippingMethod])
```

## Parameters

- `errors`: An array of errors for the coupon code that the user must resolve.
- `paymentSummaryItems`: An array of summary items that include any changes due to the coupon.
- `shippingMethods`: An array of shipping methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestcouponcodeupdate/init(errors:paymentsummaryitems:shippingmethods:))*