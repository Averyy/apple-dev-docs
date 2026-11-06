# SubscriptionBillingPlanTypeGroupSet

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A set of subscription option groups, where each group represents subscriptions merchandised with a common billing plan type.

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
@preconcurrency struct SubscriptionBillingPlanTypeGroupSet<Label, MarketingContent> where Label : View, MarketingContent : View
```

## Overview

Use this type to present the same subscription plans side by side, grouped by billing plan type. A product appears in more than one group when it offers more than one billing plan type, for example, when it has pricing terms for both [`monthly`](./product/subscriptioninfo/billingplantype/monthly.md) and [`upFront`](./product/subscriptioninfo/billingplantype/upfront.md). For more information about billing plans, see [Managing the life cycle of monthly subscriptions with a 12-month commitment](./managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment.md).

## Topics

### Creating billing plan type group sets
- [init()](./subscriptionbillingplantypegroupset/init%28%29.md)
  Creates a billing plan type group set with automatic marketing content and default labels for each billing plan type.
- [init(marketingContent: (SubscriptionInfo.BillingPlanType) -> MarketingContent)](./subscriptionbillingplantypegroupset/init%28marketingcontent%29.md)
  Creates a billing plan type group set with custom marketing content and default labels for each billing plan type.
- [init(marketingContent: (SubscriptionInfo.BillingPlanType) -> MarketingContent, label: (SubscriptionInfo.BillingPlanType) -> Label)](./subscriptionbillingplantypegroupset/init%28marketingcontent,label%29.md)
  Creates a billing plan type group set with custom marketing content and labels for each billing plan type.
### Creating the group style
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some View
](../SwiftUI/view/subscriptionstoreoptiongroupstyle%28_%29.md)
  Sets the style subscription store views within this view use to display groups of subscription options.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [StoreContent](./storecontent.md)

## See Also

### Declaring the structure of a subscription store
- [struct SubscriptionOptionGroup](./subscriptionoptiongroup.md)
  A group of subscription options that includes optional views for labels and marketing content.
- [struct SubscriptionOptionGroupSet](./subscriptionoptiongroupset.md)
  A set of groups of subscription options that include optional views for labels and marketing content.
- [struct SubscriptionPeriodGroupSet](./subscriptionperiodgroupset.md)
- [struct SubscriptionPricingModelGroupSet](./subscriptionpricingmodelgroupset.md)
  A set of subscription option groups, where each group represents subscriptions merchandised with a common pricing model.
- [struct SubscriptionOptionSection](./subscriptionoptionsection.md)
- [protocol StoreContent](./storecontent.md)
  A type that represents the content of a store.
- [struct StoreContentBuilder](./storecontentbuilder.md)
  A result builder that creates store content from closures that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionbillingplantypegroupset)*