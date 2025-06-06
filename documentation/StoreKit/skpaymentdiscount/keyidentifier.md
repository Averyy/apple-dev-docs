# keyIdentifier

**Framework**: StoreKit  
**Kind**: property

A string that identifies the key used to generate the signature.

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
var keyIdentifier: String { get }
```

#### Discussion

You generate and download keys from App Store Connect. See the “KEY ID” column in App Store Connect to use as the [`keyIdentifier`](skpaymentdiscount/keyidentifier.md).

## See Also

- [var identifier: String](skpaymentdiscount/identifier.md)
  A string used to uniquely identify a discount offer for a product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/keyidentifier)*