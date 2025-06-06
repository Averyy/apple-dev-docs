# returnReadResultImmediately

**Framework**: ProximityReader  
**Kind**: property

A Boolean value that indicates whether the framework returns a result as soon as possible before closing the system UI.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 17.0+

## Declaration

```swift
var returnReadResultImmediately: Bool
```

#### Discussion

The default value  is `false`.

After the framework reads a payment card, by default, the UI shows an animation before closing then returning the result. When you set this option to `true`, the framework returns [`PaymentCardReadResult`](paymentcardreadresult.md)  immediately without waiting for the system UI to close.

## See Also

- [var includeErrorInReadResult: Bool](paymentcardreader/options-swift.struct/includeerrorinreadresult.md)
  A Boolean value that indicates whether the framework returns a result instead of throwing an error when some data is retrievable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/options-swift.struct/returnreadresultimmediately)*