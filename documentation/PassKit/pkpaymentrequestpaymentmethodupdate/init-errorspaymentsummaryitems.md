# init(errors:paymentSummaryItems:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a payment-method update with your specified payment summary items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init(errors: [any Error]?, paymentSummaryItems: [PKPaymentSummaryItem])
```

#### Discussion

Use the `errors` array to specify any errors in the payment method that the user must resolve. For more information on creating user errors, see [`PKPaymentError`](pkpaymenterror.md).

## Parameters

- `errors`: An array of errors in the selected payment-method that the user must resolve.
- `paymentSummaryItems`: An array of summary items that include any changes due to fees or credit card surcharges associated with the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestpaymentmethodupdate/init(errors:paymentsummaryitems:))*