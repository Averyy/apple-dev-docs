# init(paymentDescription:regularBilling:managementURL:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Create a recurring payment object with a description, regular billing information, and a management URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(paymentDescription: String, regularBilling: PKRecurringPaymentSummaryItem, managementURL: URL)
```

#### Discussion

> ❗ **Important**:  You must set the [`recurringPaymentRequest`](pkpaymentrequest/recurringpaymentrequest.md) property on a [`PKPaymentRequest`](pkpaymentrequest.md) object to use this class to request a recurring payment.

 You must set the [`recurringPaymentRequest`](pkpaymentrequest/recurringpaymentrequest.md) property on a [`PKPaymentRequest`](pkpaymentrequest.md) object to use this class to request a recurring payment.

## Parameters

- `paymentDescription`: The description you provide of the recurring payment and that Apple Pay displays to the user in the payment sheet.
- `regularBilling`: The summary item for the recurring payment that includes the payment period and interval.
- `managementURL`: The URL to a web page where the user can update or delete the payment method for the recurring payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest/init(paymentdescription:regularbilling:managementurl:))*