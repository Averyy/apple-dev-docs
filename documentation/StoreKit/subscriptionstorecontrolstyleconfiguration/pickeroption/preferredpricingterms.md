# preferredPricingTerms

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The preferred pricing terms for this subscription option.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
var preferredPricingTerms: SubscriptionInfo.PricingTerms? { get }
```

## Discussion

This property reflects the pricing terms from the [`preferredSubscriptionPricingTerms(_:)`](../../../SwiftUI/view/preferredsubscriptionpricingterms%28_%29.md) view modifier on an ancestor view, or from the [`preferredSubscriptionPricingTerms(_:)`](../../storecontent/preferredsubscriptionpricingterms%28_%29.md) modifier on the enclosing store content. The value is `nil` when you don’t specify preferred pricing terms. It’s the subscription’s default pricing terms when the modifier’s closure returns `nil`, or when the pricing terms you specify don’t exist for the subscription.

Use this property in your custom [`SubscriptionStoreControlStyle`](../../subscriptionstorecontrolstyle.md) to display pricing information that matches the pricing terms the store uses. For example, when the [`pricingModel`](../../product/subscriptioninfo/pricingterms-swift.struct/pricingmodel-swift.property.md) is seat-based, display its [`priceTiers`](../../product/subscriptioninfo/pricingterms-swift.struct/seatbasedpricing/pricetiers.md).

## See Also

### Getting properties of the subscription picker option
- [var subscription: Product](./subscription.md)
  The auto-renewable subscription that the picker option represents.
- [var activeOffer: Product.SubscriptionOffer?](./activeoffer.md)
- [let isSelected: Bool](./isselected.md)
  A Boolean value that indicates whether the picker option is in a selected state.
- [var icon: SubscriptionStoreControlStyleConfiguration.Icon?](./icon.md)
  The subscription option’s icon.
- [var id: Product.ID](./id.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption/preferredpricingterms)*