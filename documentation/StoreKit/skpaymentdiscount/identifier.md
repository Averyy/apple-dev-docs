# identifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A string used to uniquely identify a discount offer for a product.

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
var identifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

#### Discussion

You set up offers and their identifiers in App Store Connect. If the [`identifier`](./identifier.md) is not valid, an [`SKError.Code.invalidOfferIdentifier`](../skerror/code/invalidofferidentifier.md) error can result.

## See Also

### Identifying the Discount
- [var keyIdentifier: String](./keyidentifier.md)
  A string that identifies the key used to generate the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skpaymentdiscount/identifier)*