# init(marketingContent:label:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

Creates a pricing model group set with custom marketing content and labels for each pricing model.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder marketingContent: @escaping (SubscriptionInfo.PricingTerms.PricingModel) -> MarketingContent, @ViewBuilder label: @escaping (SubscriptionInfo.PricingTerms.PricingModel) -> Label)
```

## Parameters

- `marketingContent`: A view builder that provides marketing content for each pricing model.
- `label`: A view builder that provides a label for each pricing model.

## See Also

### Creating pricing model group sets
- [init()](./init%28%29.md)
  Creates a pricing model group set with automatic marketing content and default labels for each pricing model.
- [init(marketingContent: (SubscriptionInfo.PricingTerms.PricingModel) -> MarketingContent)](./init%28marketingcontent%29.md)
  Creates a pricing model group set with custom marketing content and default labels for each pricing model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionpricingmodelgroupset/init(marketingcontent:label:))*