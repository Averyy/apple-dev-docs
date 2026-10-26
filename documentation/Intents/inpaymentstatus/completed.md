# INPaymentStatus.completed

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app made the payment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case completed
```

```c
INPaymentStatusCompleted
```

#### Discussion

Use this constant when the funds have been successfully transferred to the payee’s account.

## See Also

### Constants
- [INPaymentStatus.unknown](./unknown.md)
  The payment status is unknown.
- [INPaymentStatus.pending](./pending.md)
  The app hasn’t sent the payment yet.
- [INPaymentStatus.canceled](./canceled.md)
  The app canceled the transaction before transferring the funds.
- [INPaymentStatus.failed](./failed.md)
  The transaction failed and the funds were not transferred.
- [INPaymentStatus.unpaid](./unpaid.md)
  The bill is currently unpaid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentstatus/completed)*