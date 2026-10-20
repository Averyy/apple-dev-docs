# PaymentCardReadResult.ReadOutcome.success

**Framework**: ProximityReader  
**Kind**: case  
**Role**: Case

The read was successful.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 17.0+

## Declaration

```swift
case success
```

## See Also

### Getting the read outcome
- [PaymentCardReadResult.ReadOutcome.failure](./failure.md)
  The read failed somehow, the card data may not contain all requested tags.
- [PaymentCardReadResult.ReadOutcome.cardDeclined](./carddeclined.md)
  The card declined this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/readoutcome/success)*