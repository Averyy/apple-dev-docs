# readerIdentifier

**Framework**: ProximityReader  
**Kind**: property

The unique identifier for this card reader.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
var readerIdentifier: String { get async throws }
```

#### Discussion

Include this identifier in support requests or tracing incidents to help track down potential problems. If the identifier isn’t readable, getting this value throws a [`PaymentCardReaderError`](paymentcardreadererror.md).

## See Also

- [let options: PaymentCardReader.Options](paymentcardreader/options-swift.property.md)
  The defined configuration settings when the reader was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreader/readeridentifier)*