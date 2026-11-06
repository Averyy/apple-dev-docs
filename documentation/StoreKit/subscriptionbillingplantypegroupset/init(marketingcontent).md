# init(marketingContent:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

Creates a billing plan type group set with custom marketing content and default labels for each billing plan type.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder marketingContent: @escaping (SubscriptionInfo.BillingPlanType) -> MarketingContent) where Label == AutomaticSubscriptionOptionGroupLabel
```

## Parameters

- `marketingContent`: A view builder that provides marketing content for each billing plan type.

## See Also

### Creating billing plan type group sets
- [init()](./init%28%29.md)
  Creates a billing plan type group set with automatic marketing content and default labels for each billing plan type.
- [init(marketingContent: (SubscriptionInfo.BillingPlanType) -> MarketingContent, label: (SubscriptionInfo.BillingPlanType) -> Label)](./init%28marketingcontent,label%29.md)
  Creates a billing plan type group set with custom marketing content and labels for each billing plan type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionbillingplantypegroupset/init(marketingcontent:))*