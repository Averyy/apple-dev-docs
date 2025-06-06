# includeErrorInReadResult

**Framework**: ProximityReader  
**Kind**: property

A Boolean value that indicates whether the framework returns a result instead of throwing an error when some data is retrievable.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 17.0+

## Declaration

```swift
var includeErrorInReadResult: Bool
```

#### Discussion

The default value  is `false`.

After the framework reads a payment card, when there’s an error, the framework discards  [`PaymentCardReadResult`](paymentcardreadresult.md) and throws an error.

When you set this option to `true`, if an error arises, the framework doesn’t throw an error, instead the [`PaymentCardReadResult`](paymentcardreadresult.md) includes both the [`outcome`](paymentcardreadresult/outcome.md) and the data that the framework can retrieve. You’re responsible for checking the outcome in addition to catching errors the framework throws.

## See Also

- [var returnReadResultImmediately: Bool](paymentcardreader/options-swift.struct/returnreadresultimmediately.md)
  A Boolean value that indicates whether the framework returns a result as soon as possible before closing the system UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/options-swift.struct/includeerrorinreadresult)*