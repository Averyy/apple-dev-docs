# subscriptionStoreButtonLabel(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func subscriptionStoreButtonLabel(_ label: SubscriptionStoreButtonLabel) -> some StoreContent
```

## See Also

### Configuring store content
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some StoreContent](./subscriptionstoreoptiongroupstyle%28_%29.md)
- [func storeButton(Visibility, for: StoreButtonKind...) -> some StoreContent](./storebutton%28_,for%29.md)
- [func subscriptionStoreControlStyle<S>(S, placement: S.Placement) -> some StoreContent](./subscriptionstorecontrolstyle%28_,placement%29.md)
- [func productDescription(Visibility) -> some StoreContent](./productdescription%28_%29.md)
- [func preferredSubscriptionPricingTerms((Product, SubscriptionInfo) -> SubscriptionInfo.PricingTerms?) -> some StoreContent](./preferredsubscriptionpricingterms%28_%29.md)
  Sets the pricing terms that the store uses to merchandise the subscription options within this store content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storecontent/subscriptionstorebuttonlabel(_:))*