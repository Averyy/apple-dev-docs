# Product.ProductType

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

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
- [static let consumable: Product.ProductType](./producttype/consumable.md)
  A consumable Apple In-App Purchase.
- [static let nonConsumable: Product.ProductType](./producttype/nonconsumable.md)
  A non-consumable Apple In-App Purchase.
- [static let nonRenewable: Product.ProductType](./producttype/nonrenewable.md)
  A non-renewing subscription.
- [static let autoRenewable: Product.ProductType](./producttype/autorenewable.md)
  An auto-renewable subscription.
### Getting a Localized Description
- [var localizedDescription: String](./producttype/localizeddescription.md)
### Type Properties
- [static let subscriptionBundle: Product.ProductType](./producttype/subscriptionbundle.md)
- [static let subscriptionSuite: Product.ProductType](./producttype/subscriptionsuite.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting product identifiers and type
- [let id: String](./id.md)
  The unique product identifier.
- [let type: Product.ProductType](./type.md)
  The Apple In-App Purchase product type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/producttype)*