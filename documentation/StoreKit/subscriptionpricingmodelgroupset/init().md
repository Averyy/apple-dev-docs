# init()

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

Creates a pricing model group set with automatic marketing content and default labels for each pricing model.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init() where Label == AutomaticSubscriptionOptionGroupLabel, MarketingContent == AutomaticSubscriptionStoreMarketingContent
```

## See Also

### Creating pricing model group sets
- [init(marketingContent: (SubscriptionInfo.PricingTerms.PricingModel) -> MarketingContent)](./init%28marketingcontent%29.md)
  Creates a pricing model group set with custom marketing content and default labels for each pricing model.
- [init(marketingContent: (SubscriptionInfo.PricingTerms.PricingModel) -> MarketingContent, label: (SubscriptionInfo.PricingTerms.PricingModel) -> Label)](./init%28marketingcontent,label%29.md)
  Creates a pricing model group set with custom marketing content and labels for each pricing model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionpricingmodelgroupset/init())*