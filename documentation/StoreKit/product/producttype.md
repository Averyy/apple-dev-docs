# Product.ProductType

**Framework**: StoreKit  
**Kind**: struct

The types of Apple In-App Purchases.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
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
  A consumable Apple In-App Purchase.
- [static let nonConsumable: Product.ProductType](product/producttype/nonconsumable.md)
  A non-consumable Apple In-App Purchase.
- [static let nonRenewable: Product.ProductType](product/producttype/nonrenewable.md)
  A non-renewing subscription.
- [static let autoRenewable: Product.ProductType](product/producttype/autorenewable.md)
  An auto-renewable subscription.
### Getting a Localized Description
- [var localizedDescription: String](product/producttype/localizeddescription.md)
### Type Properties
- [static let subscriptionBundle: Product.ProductType](product/producttype/subscriptionbundle.md)
- [static let subscriptionSuite: Product.ProductType](product/producttype/subscriptionsuite.md)

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let id: String](product/id.md)
  The unique product identifier.
- [let type: Product.ProductType](product/type.md)
  The Apple In-App Purchase product type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/producttype)*