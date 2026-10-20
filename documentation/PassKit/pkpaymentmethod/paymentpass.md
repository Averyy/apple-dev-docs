# paymentPass

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The accompanying payment pass.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 3.0+ - Deprecated in 27.2

> **Deprecated**: Use [`secureElementPass`](./secureelementpass.md) instead.

## Declaration

```swift
@NSCopying
var paymentPass: PKPaymentPass? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) PKPaymentPass * paymentPass;
```

#### Discussion

If your app has an association with the pass that is funding the payment, this property contains information about that pass; otherwise, it’s `nil`.

Use this property to detect your brand of credit and debit cards. For example, you can provide a discount if the user pays using your store-branded credit card.

> **Note**:  To be able to access the pass, the issuer must add your App ID to the pass when it provisions it. To add your App ID to these passes, contact the bank that issues your cards or the person who manages your cobrand program.

## See Also

### Getting the pass
- [var secureElementPass: PKSecureElementPass?](./secureelementpass.md)
  The accompanying Secure Element pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentmethod/paymentpass)*