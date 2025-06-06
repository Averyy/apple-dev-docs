# paymentDescription

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A description that you provide of the automatic reload payment and that Apple Pay displays to the user in the payment sheet.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var paymentDescription: String { get set }
```

#### Discussion

Provide a display name for the automatic reload, for example, “Gift Card Reload”.

## See Also

- [var billingAgreement: String?](pkautomaticreloadpaymentrequest/billingagreement.md)
  A localized billing agreement that the payment sheet displays to the user before the user authorizes the payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest/paymentdescription)*