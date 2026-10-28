# INPaymentStatus.unknown

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The payment status is unknown.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case unknown
```

```c
INPaymentStatusUnknown
```

## Discussion

Use this constant when the financial transaction has not yet occurred and you are unable to determine its state.

## See Also

### Constants
- [INPaymentStatus.pending](./pending.md)
  The app hasn’t sent the payment yet.
- [INPaymentStatus.completed](./completed.md)
  The app made the payment.
- [INPaymentStatus.canceled](./canceled.md)
  The app canceled the transaction before transferring the funds.
- [INPaymentStatus.failed](./failed.md)
  The transaction failed and the funds were not transferred.
- [INPaymentStatus.unpaid](./unpaid.md)
  The bill is currently unpaid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentstatus/unknown)*