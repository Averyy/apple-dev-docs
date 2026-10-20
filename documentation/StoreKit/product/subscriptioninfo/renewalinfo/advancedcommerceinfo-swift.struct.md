# Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Renewal information for subscriptions that use the Advanced Commerce API.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct AdvancedCommerceInfo
```

## Topics

### Structures
- [Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo.Item](./advancedcommerceinfo-swift.struct/item.md)
  The developer-defined product that was purchased.
### Instance Properties
- [let consistencyToken: String](./advancedcommerceinfo-swift.struct/consistencytoken.md)
- [let description: String](./advancedcommerceinfo-swift.struct/description.md)
- [let displayName: String](./advancedcommerceinfo-swift.struct/displayname.md)
- [let items: [Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo.Item]](./advancedcommerceinfo-swift.struct/items.md)
  The items included in this subscription.
- [let period: SubscriptionPeriod](./advancedcommerceinfo-swift.struct/period.md)
- [let requestReferenceID: String](./advancedcommerceinfo-swift.struct/requestreferenceid.md)
- [let taxCode: String](./advancedcommerceinfo-swift.struct/taxcode.md)

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Getting renewal information for Advanced Commerce API
- [let advancedCommerceInfo: Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo?](./advancedcommerceinfo-swift.property.md)
  Renewal information for a subscription that uses the Advanced Commerce API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct)*