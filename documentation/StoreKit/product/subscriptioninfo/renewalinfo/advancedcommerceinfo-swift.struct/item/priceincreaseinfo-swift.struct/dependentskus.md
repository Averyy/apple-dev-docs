# dependentSKUs

**Framework**: StoreKit  
**Kind**: property

An array of one or more SKUs on which the current subscription offer depends.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- macOS 26.2+
- tvOS 26.2+
- visionOS 26.2+
- watchOS 26.2+

## Declaration

```swift
let dependentSKUs: [String]
```

#### Discussion

You can provide a list of SKUs and create a contingency scenario in which a person’s refusal to agree to a price increase results in the App Store canceling other, bundled services (the ). If the price increase requires a personʼs consent, and they don’t consent but instead cancel the subscription in the Manage Subscriptions view, the App Store cancels the dependent SKUs.

> ❗ **Important**: You can’t create chains of dependent SKUs; for example, if SKU A has a dependent SKU B, B can’t have its own dependent SKU, C. However, B can have its own price increase.

## See Also

- [let price: Decimal](product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/price.md)
  The cost of the price increase in the location-specific currency.
- [let status: Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo.Item.PriceIncreaseInfo.Status](product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/status-swift.property.md)
  The status of the price increase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct/item/priceincreaseinfo-swift.struct/dependentskus)*