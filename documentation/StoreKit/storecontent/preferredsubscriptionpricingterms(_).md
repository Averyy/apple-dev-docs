# preferredSubscriptionPricingTerms(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

Sets the pricing terms that the store uses to merchandise the subscription options within this store content.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
nonisolated
func preferredSubscriptionPricingTerms(_ pricingTerms: @escaping (Product, SubscriptionInfo) -> SubscriptionInfo.PricingTerms?) -> some StoreContent
```

## Mentions

- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)

## Discussion

Use this modifier on a [`SubscriptionOptionGroup`](../subscriptionoptiongroup.md) or other store content to choose the pricing terms for the subscription options within that content. Different groups in one subscription store view can then show the same products with different pricing terms, for example, a group that shows seat-based pricing terms for multiseat purchases.

Unlike the [`preferredSubscriptionPricingTerms(_:)`](../../SwiftUI/view/preferredsubscriptionpricingterms%28_%29.md) view modifier, which applies to every subscription store in the view, this modifier applies only to the store content you apply it to. The pricing terms you set override pricing terms that you set in ancestor views. If the pricing terms you return don’t exist for a subscription, the store uses the subscription’s default pricing terms.

To read the pricing terms in a custom control style, use [`preferredPricingTerms`](../subscriptionstorecontrolstyleconfiguration/option/preferredpricingterms.md).

## Parameters

- `pricingTerms`: A closure that the system calls before it draws each subscription product. The closure receives the product and its subscription information. Return the pricing terms to use for that subscription option, or `nil` to use the subscription’s default pricing terms.

## See Also

### Choosing pricing terms
- [func preferredSubscriptionPricingTerms((Product, SubscriptionInfo) -> SubscriptionInfo.PricingTerms?) -> some View
](../../SwiftUI/view/preferredsubscriptionpricingterms%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storecontent/preferredsubscriptionpricingterms(_:))*