# PaymentCardReadResult.ReadOutcome

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

Values that describe the outcome of a read request.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 17.0+

## Declaration

```swift
enum ReadOutcome
```

## Topics

### Getting the read outcome
- [PaymentCardReadResult.ReadOutcome.success](./readoutcome/success.md)
  The read was successful.
- [PaymentCardReadResult.ReadOutcome.failure](./readoutcome/failure.md)
  The read failed somehow, the card data may not contain all requested tags.
- [PaymentCardReadResult.ReadOutcome.cardDeclined](./readoutcome/carddeclined.md)
  The card declined this transaction.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Checking the read outcome
- [let outcome: PaymentCardReadResult.ReadOutcome](./outcome.md)
  The outcome of the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/readoutcome)*