# deferredPaymentRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A request to set up a deferred payment, such as a hotel booking or a pre-order.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
var deferredPaymentRequest: PKDeferredPaymentRequest? { get set }
```

#### Discussion

> **Note**:  watchOS doesn’t support merchant-specific payment tokens.

 watchOS doesn’t support merchant-specific payment tokens.

This payment request receives a merchant-specific payment token if the payment network supports merchant-specific payment tokens.

> ❗ **Important**:  You can’t use this property simultaneously with multitoken contexts, recurring payment requests, or automatic reload payment requests. Simultaneous use of these properties results in a runtime error and cancels the payment request.

 You can’t use this property simultaneously with multitoken contexts, recurring payment requests, or automatic reload payment requests. Simultaneous use of these properties results in a runtime error and cancels the payment request.

## See Also

- [var recurringPaymentRequest: PKRecurringPaymentRequest?](pkpaymentrequest/recurringpaymentrequest.md)
  An optional request to set up a recurring payment, typically a subscription.
- [class PKRecurringPaymentRequest](pkrecurringpaymentrequest.md)
  A class that represents a request to set up a recurring payment, typically a subscription.
- [var automaticReloadPaymentRequest: PKAutomaticReloadPaymentRequest?](pkpaymentrequest/automaticreloadpaymentrequest.md)
  An optional request to set up an automatic reload payment, such as a store card top-up.
- [class PKAutomaticReloadPaymentRequest](pkautomaticreloadpaymentrequest.md)
  A class that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
- [class PKDeferredPaymentRequest](pkdeferredpaymentrequest.md)
  An object that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/deferredpaymentrequest)*