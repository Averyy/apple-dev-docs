# billingAgreement

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A localized billing agreement that the payment sheet displays to the user before the user authorizes the payment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var billingAgreement: String? { get set }
```

#### Discussion

The merchant may provide an optional, localized [`billingAgreement`](pkautomaticreloadpaymentrequest/billingagreement.md) string. The maximum length of the [`billingAgreement`](pkautomaticreloadpaymentrequest/billingagreement.md) string is 500 characters.

You may use this string to include information about the reload threshold amount or other reload conditions, for example, or information on how the user can cancel payments. This string isn’t intended to replace any payment terms that you provide outside of the Apple Pay payment sheet.

> ❗ **Important**:  You’re responsible to ensure that your use of this framework, including your billing agreement, is compliant with applicable legal requirements.

 You’re responsible to ensure that your use of this framework, including your billing agreement, is compliant with applicable legal requirements.

The Apple Pay payment sheet displays the text of the [`billingAgreement`](pkautomaticreloadpaymentrequest/billingagreement.md) string; however, long [`billingAgreement`](pkautomaticreloadpaymentrequest/billingagreement.md) strings that don’t fit on the payment sheet screen appear truncated with an ellipsis. Users can select the Billing Details on the payment sheet to read the full text of the [`billingAgreement`](pkautomaticreloadpaymentrequest/billingagreement.md) string, up to the maximum 500 characters.

## See Also

- [var paymentDescription: String](pkautomaticreloadpaymentrequest/paymentdescription.md)
  A description that you provide of the automatic reload payment and that Apple Pay displays to the user in the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest/billingagreement)*