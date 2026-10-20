# Product.SubscriptionInfo.BundledSubscription

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Properties and functionality specific to auto-renewable subscriptions included in a subscription bundle.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct BundledSubscription
```

## Topics

### Instance Properties
- [let description: String](./bundledsubscription/description.md)
  A localized description of the product.
- [let displayName: String](./bundledsubscription/displayname.md)
  A localized display name of the product.
- [let displayPrice: String](./bundledsubscription/displayprice.md)
  A localized string representation of `price`.
- [let id: Product.ID](./bundledsubscription/id.md)
  The unique product identifier.
- [let isFamilyShareable: Bool](./bundledsubscription/isfamilyshareable.md)
  Whether the product is available for family sharing.
- [let price: Decimal](./bundledsubscription/price.md)
  The price of the product in local currency.
- [let subscriptionGroupDisplayName: String](./bundledsubscription/subscriptiongroupdisplayname.md)
  A localized display name of the subscription’s group.
- [let subscriptionGroupID: String](./bundledsubscription/subscriptiongroupid.md)
  The group identifier for this subscription.
- [let subscriptionGroupLevel: Int](./bundledsubscription/subscriptiongrouplevel.md)
  The level of this subscription relative to other subscriptions in the same group.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/bundledsubscription)*