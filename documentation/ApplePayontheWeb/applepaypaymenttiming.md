# ApplePayPaymentTiming

**Framework**: Apple Pay on the Web  
**Kind**: enum

A type that indicates the time a payment occurs in a transaction.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
enum ApplePayPaymentTiming
```

## Mentions

- [Apple Pay on the Web Version 14 Release Notes](apple-pay-on-the-web-version-14-release-notes.md)

#### Overview

The following are the payment timing values:

- **`"immediate"`**: A value that specifies that the payment occurs when the transaction is complete.
- **`"recurring"`**: A value that specifies that the payment occurs on a regular basis.
- **`"deferred"`**: A value that specifies that the payment occurs in the future.
- **`"automaticReload"`**: A value that specifies that the payment occurs automatically when the account falls below the [`automaticReloadPaymentThresholdAmount`](applepaylineitem/automaticreloadpaymentthresholdamount.md) amount.

## Topics

### Enumeration Cases
- [automaticReload](applepaypaymenttiming/automaticreload.md)
- [deferred](applepaypaymenttiming/deferred.md)
- [immediate](applepaypaymenttiming/immediate.md)
- [recurring](applepaypaymenttiming/recurring.md)

## See Also

- [paymentTiming](applepaylineitem/paymenttiming.md)
  The time that the payment occurs as part of a successful transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymenttiming)*