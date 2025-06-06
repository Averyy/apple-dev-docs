# identifier

**Framework**: StoreKit  
**Kind**: property

A string used to uniquely identify a discount offer for a product.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

You set up offers and their identifiers in App Store Connect. If the [`identifier`](skpaymentdiscount/identifier.md) is not valid, an [`SKError.Code.invalidOfferIdentifier`](skerror/code/invalidofferidentifier.md) error can result.

## See Also

- [var keyIdentifier: String](skpaymentdiscount/keyidentifier.md)
  A string that identifies the key used to generate the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/identifier)*