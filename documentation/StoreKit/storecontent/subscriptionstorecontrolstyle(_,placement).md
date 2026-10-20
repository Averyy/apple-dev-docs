# subscriptionStoreControlStyle(_:placement:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func subscriptionStoreControlStyle<S>(_ style: S, placement: S.Placement = .automatic) -> some StoreContent where S : SubscriptionStoreControlStyle
```

## See Also

### Configuring store content
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some StoreContent](./subscriptionstoreoptiongroupstyle%28_%29.md)
- [func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some StoreContent](./subscriptionstorebuttonlabel%28_%29.md)
- [func storeButton(Visibility, for: StoreButtonKind...) -> some StoreContent](./storebutton%28_,for%29.md)
- [func productDescription(Visibility) -> some StoreContent](./productdescription%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storecontent/subscriptionstorecontrolstyle(_:placement:))*