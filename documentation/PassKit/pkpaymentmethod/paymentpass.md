# paymentPass

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The accompanying payment pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var paymentPass: PKPaymentPass? { get }
```

#### Discussion

If your app has an association with the pass that is funding the payment, this property contains information about that pass; otherwise, it’s `nil`.

Use this property to detect your brand of credit and debit cards. For example, you can provide a discount if the user pays using your store-branded credit card.

> **Note**:  To be able to access the pass, the issuer must add your App ID to the pass when it provisions it. To add your App ID to these passes, contact the bank that issues your cards or the person who manages your cobrand program.

## See Also

- [var secureElementPass: PKSecureElementPass?](pkpaymentmethod/secureelementpass.md)
  The accompanying Secure Element pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentmethod/paymentpass)*