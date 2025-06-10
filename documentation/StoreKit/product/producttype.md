# Product.ProductType

**Framework**: StoreKit  
**Kind**: struct

The types of in-app purchases.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct ProductType
```

## Topics

### Getting the Product Type
- [static let consumable: Product.ProductType](product/producttype/consumable.md)
  A consumable in-app purchase.
- [static let nonConsumable: Product.ProductType](product/producttype/nonconsumable.md)
  A non-consumable in-app purchase.
- [static let nonRenewable: Product.ProductType](product/producttype/nonrenewable.md)
  A non-renewing subscription.
- [static let autoRenewable: Product.ProductType](product/producttype/autorenewable.md)
  An auto-renewable subscription.
### Getting a Localized Description
- [var localizedDescription: String](product/producttype/localizeddescription.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let id: String](product/id.md)
  The unique product identifier.
- [let type: Product.ProductType](product/type.md)
  The in-app purchase product type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/producttype)*