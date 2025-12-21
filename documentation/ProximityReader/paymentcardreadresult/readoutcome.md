# PaymentCardReadResult.ReadOutcome

**Framework**: ProximityReader  
**Kind**: enum

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
- [PaymentCardReadResult.ReadOutcome.success](paymentcardreadresult/readoutcome/success.md)
  The read was successful.
- [PaymentCardReadResult.ReadOutcome.failure](paymentcardreadresult/readoutcome/failure.md)
  The read failed somehow, the card data may not contain all requested tags.
- [PaymentCardReadResult.ReadOutcome.cardDeclined](paymentcardreadresult/readoutcome/carddeclined.md)
  The card declined this transaction.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let outcome: PaymentCardReadResult.ReadOutcome](paymentcardreadresult/outcome.md)
  The outcome of the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/readoutcome)*