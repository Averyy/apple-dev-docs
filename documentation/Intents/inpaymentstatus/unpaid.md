# INPaymentStatus.unpaid

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The bill is currently unpaid.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case unpaid
```

```c
INPaymentStatusUnpaid
```

## See Also

### Constants
- [INPaymentStatus.unknown](./unknown.md)
  The payment status is unknown.
- [INPaymentStatus.pending](./pending.md)
  The app hasn’t sent the payment yet.
- [INPaymentStatus.completed](./completed.md)
  The app made the payment.
- [INPaymentStatus.canceled](./canceled.md)
  The app canceled the transaction before transferring the funds.
- [INPaymentStatus.failed](./failed.md)
  The transaction failed and the funds were not transferred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentstatus/unpaid)*