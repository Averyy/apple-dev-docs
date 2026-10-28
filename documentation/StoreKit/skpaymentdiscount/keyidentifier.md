# keyIdentifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string that identifies the key used to generate the signature.

**Availability**:
- iOS 12.2+ - Deprecated in 18.0
- iPadOS 12.2+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.14.4+ - Deprecated in 15.0
- tvOS 12.2+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 6.2+ - Deprecated in 11.0

> **Deprecated**: Create a Product.PurchaseOption.promotionalOffer to use in Product.purchase(confirmIn:options:).

## Declaration

```swift
var keyIdentifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * keyIdentifier;
```

## Discussion

You generate and download keys from App Store Connect. See the “KEY ID” column in App Store Connect to use as the [`keyIdentifier`](./keyidentifier.md).

## See Also

### Identifying the Discount
- [var identifier: String](./identifier.md)
  A string used to uniquely identify a discount offer for a product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/keyidentifier)*