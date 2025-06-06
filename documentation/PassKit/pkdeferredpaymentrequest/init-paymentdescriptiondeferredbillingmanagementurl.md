# init(paymentDescription:deferredBilling:managementURL:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: init

Creates a deferred payment request with the payment description, deferred billing summary, and management URL you provide.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
init(paymentDescription: String, deferredBilling: PKDeferredPaymentSummaryItem, managementURL: URL)
```

## Parameters

- `paymentDescription`: A description of the deferred payment, for example “Hotel stay, 2 nights.”
- `deferredBilling`: Details about the deferred payment, for example “Pay $2.99 on October 9, 2023.”
- `managementURL`: A URL that links to a page on your web site where the user can manage the payment method for the deferred payment, including deleting it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest/init(paymentdescription:deferredbilling:managementurl:))*