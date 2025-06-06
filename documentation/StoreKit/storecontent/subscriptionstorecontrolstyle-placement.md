# subscriptionStoreControlStyle(_:placement:)

**Framework**: StoreKit  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
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

- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some StoreContent](storecontent/subscriptionstoreoptiongroupstyle(_:).md)
- [func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some StoreContent](storecontent/subscriptionstorebuttonlabel(_:).md)
- [func storeButton(Visibility, for: StoreButtonKind...) -> some StoreContent](storecontent/storebutton(_:for:).md)
- [func productDescription(Visibility) -> some StoreContent](storecontent/productdescription(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storecontent/subscriptionstorecontrolstyle(_:placement:))*