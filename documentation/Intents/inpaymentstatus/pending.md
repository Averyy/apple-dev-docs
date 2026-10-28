# INPaymentStatus.pending

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app hasn’t sent the payment yet.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case pending
```

```c
INPaymentStatusPending
```

## Discussion

Use this constant when you have a record of the transaction details but the funds you haven’t transferred the funds yet.

## See Also

### Constants
- [INPaymentStatus.unknown](./unknown.md)
  The payment status is unknown.
- [INPaymentStatus.completed](./completed.md)
  The app made the payment.
- [INPaymentStatus.canceled](./canceled.md)
  The app canceled the transaction before transferring the funds.
- [INPaymentStatus.failed](./failed.md)
  The transaction failed and the funds were not transferred.
- [INPaymentStatus.unpaid](./unpaid.md)
  The bill is currently unpaid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentstatus/pending)*