# multiTokenContexts

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An array of payment token contexts to request multiple payment tokens with one payment token per context.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var multiTokenContexts: [PKPaymentTokenContext] { get set }
```

#### Discussion

Use multitoken contexts to indicate payments for multiple merchants. This property is an array of [`PKPaymentTokenContext`](pkpaymenttokencontext.md) objects. The sum of all payment token contexts must be less than or equal to the grand total of the enclosing payment request listed as the last payment summary item, [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md). Otherwise, the request results in a runtime error and cancels the payment request.

> ❗ **Important**:  You can’t use this property with [`recurringPaymentRequest`](pkpaymentrequest/recurringpaymentrequest.md) or [`automaticReloadPaymentRequest`](pkpaymentrequest/automaticreloadpaymentrequest.md) properties. Simultaneous use of these properties results in a runtime error and cancels the payment request.

 You can’t use this property with [`recurringPaymentRequest`](pkpaymentrequest/recurringpaymentrequest.md) or [`automaticReloadPaymentRequest`](pkpaymentrequest/automaticreloadpaymentrequest.md) properties. Simultaneous use of these properties results in a runtime error and cancels the payment request.

## See Also

- [class PKPaymentTokenContext](pkpaymenttokencontext.md)
  A class that defines the context for a single payment token in a payment request for multimerchant payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/multitokencontexts)*