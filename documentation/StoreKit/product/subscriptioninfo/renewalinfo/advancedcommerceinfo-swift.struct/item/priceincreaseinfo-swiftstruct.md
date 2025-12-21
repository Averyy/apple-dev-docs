# Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo.Item.PriceIncreaseInfo

**Framework**: StoreKit  
**Kind**: struct

A structure that describes the details of a subscription price increase.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
struct PriceIncreaseInfo
```

## Topics

### Information about a price increase
- [let dependentSKUs: [String]](product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/dependentskus.md)
  An array of one or more SKUs on which the current subscription offer depends.
- [let price: Decimal](product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/price.md)
  The cost of the price increase in the location-specific currency.
- [let status: Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo.Item.PriceIncreaseInfo.Status](product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/status-swift.property.md)
  The status of the price increase.
### Structures
- [Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo.Item.PriceIncreaseInfo.Status](product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/status-swift.struct.md)
  Values that describe the status of a subscription price increase.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct)*