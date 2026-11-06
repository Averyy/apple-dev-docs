# SubscriptionPricingModelGroupSet

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A set of subscription option groups, where each group represents subscriptions merchandised with a common pricing model.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency struct SubscriptionPricingModelGroupSet<Label, MarketingContent> where Label : View, MarketingContent : View
```

## Mentions

- [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md)

## Overview

Use this type to present the same subscription plans side by side, grouped by pricing model. A product appears in more than one group when it offers more than one pricing model, for example, when it has both single-price and seat-based pricing terms for multiseat purchases.

The label and marketing content closures receive a [`Product.SubscriptionInfo.PricingTerms.PricingModel`](./product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.enum.md) value that identifies each group. Use its case, [`Product.SubscriptionInfo.PricingTerms.PricingModel.singlePrice(_:)`](./product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.enum/singleprice%28_%29.md) or [`Product.SubscriptionInfo.PricingTerms.PricingModel.seatBased(_:)`](./product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.enum/seatbased%28_%29.md), to decide what each group shows. Don’t read the case’s associated value: it describes the pricing of one product in the group, not the group as a whole.

For more information, see [Supporting multiseat purchases in your app](./supporting-multiseat-purchases-in-your-app.md).

## Topics

### Creating pricing model group sets
- [init()](./subscriptionpricingmodelgroupset/init%28%29.md)
  Creates a pricing model group set with automatic marketing content and default labels for each pricing model.
- [init(marketingContent: (SubscriptionInfo.PricingTerms.PricingModel) -> MarketingContent)](./subscriptionpricingmodelgroupset/init%28marketingcontent%29.md)
  Creates a pricing model group set with custom marketing content and default labels for each pricing model.
- [init(marketingContent: (SubscriptionInfo.PricingTerms.PricingModel) -> MarketingContent, label: (SubscriptionInfo.PricingTerms.PricingModel) -> Label)](./subscriptionpricingmodelgroupset/init%28marketingcontent,label%29.md)
  Creates a pricing model group set with custom marketing content and labels for each pricing model.
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
- [struct SubscriptionBillingPlanTypeGroupSet](./subscriptionbillingplantypegroupset.md)
  A set of subscription option groups, where each group represents subscriptions merchandised with a common billing plan type.
- [struct SubscriptionOptionSection](./subscriptionoptionsection.md)
- [protocol StoreContent](./storecontent.md)
  A type that represents the content of a store.
- [struct StoreContentBuilder](./storecontentbuilder.md)
  A result builder that creates store content from closures that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionpricingmodelgroupset)*