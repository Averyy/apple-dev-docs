# originalTransactionIdentifier

**Framework**: StoreKit Test  
**Kind**: property

The identifier of the original transaction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var originalTransactionIdentifier: Int { get }
```

#### Discussion

For subscription renewals, or if you restore a purchase, the [`originalTransactionIdentifier`](sktesttransaction/originaltransactionidentifier.md) is the original transaction for that subscription or in-app purchase.

## See Also

- [var identifier: Int](sktesttransaction/identifier.md)
  The identifier of the transaction in the testing environment.
- [var productIdentifier: String](sktesttransaction/productidentifier.md)
  An identifier that uniquely represents a product, which you provide in the StoreKit configuration file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekittest/sktesttransaction/originaltransactionidentifier)*