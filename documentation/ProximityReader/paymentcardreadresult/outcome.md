# outcome

**Framework**: ProximityReader  
**Kind**: property

The outcome of the transaction.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 17.0+

## Declaration

```swift
let outcome: PaymentCardReadResult.ReadOutcome
```

#### Discussion

This field is meaningful only if you enable [`includeErrorInReadResult`](paymentcardreader/options-swift.struct/includeerrorinreadresult.md) before you call [`prepare(using:)`](paymentcardreader/prepare(using:).md). If an error occurs while the [`PaymentCardReaderSession`](paymentcardreadersession.md) is open and the framework can retrieve [`paymentCardData`](paymentcardreadresult/paymentcarddata.md), [`PaymentCardReadResult`](paymentcardreadresult.md) includes both the [`PaymentCardReadResult.ReadOutcome`](paymentcardreadresult/readoutcome.md) and the other read data, otherwise the framework throws a [`PaymentCardReaderSession.ReadError`](paymentcardreadersession/readerror.md).

## See Also

- [PaymentCardReadResult.ReadOutcome](paymentcardreadresult/readoutcome.md)
  Values that describe the outcome of a read request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/outcome)*