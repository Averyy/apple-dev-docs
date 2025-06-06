# StoreContent

**Framework**: StoreKit  
**Kind**: protocol

A type that represents the content of a store.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol StoreContent
```

## Topics

### Implementing store content
- [var body: Self.Body](storecontent/body-swift.property.md)
- [associatedtype Body : StoreContent](storecontent/body-swift.associatedtype.md)
### Configuring store content
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some StoreContent](storecontent/subscriptionstoreoptiongroupstyle(_:).md)
- [func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some StoreContent](storecontent/subscriptionstorebuttonlabel(_:).md)
- [func storeButton(Visibility, for: StoreButtonKind...) -> some StoreContent](storecontent/storebutton(_:for:).md)
- [func subscriptionStoreControlStyle<S>(S, placement: S.Placement) -> some StoreContent](storecontent/subscriptionstorecontrolstyle(_:placement:).md)
- [func productDescription(Visibility) -> some StoreContent](storecontent/productdescription(_:).md)
### Configuring backgrounds
- [func subscriptionStoreControlBackground(SubscriptionStoreControlBackground) -> some StoreContent](storecontent/subscriptionstorecontrolbackground(_:)-10hv8.md)
- [func subscriptionStoreControlBackground(some ShapeStyle) -> some StoreContent](storecontent/subscriptionstorecontrolbackground(_:)-3xzai.md)
- [func subscriptionStorePickerItemBackground(some ShapeStyle) -> some StoreContent](storecontent/subscriptionstorepickeritembackground(_:).md)
- [func subscriptionStorePickerItemBackground(some ShapeStyle, in: some Shape) -> some StoreContent](storecontent/subscriptionstorepickeritembackground(_:in:).md)
### Supporting types
- [struct IdentifiedStoreContent](identifiedstorecontent.md)
  The type of SwiftUI view that StoreKit transforms store content into.

## Relationships

### Conforming Types
- [SubscriptionOptionGroup](subscriptionoptiongroup.md)
- [SubscriptionOptionGroupSet](subscriptionoptiongroupset.md)
- [SubscriptionOptionSection](subscriptionoptionsection.md)
- [SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [TupleStoreContent](tuplestorecontent.md)

## See Also

- [struct SubscriptionOptionGroup](subscriptionoptiongroup.md)
  A group of subscription options that includes optional views for labels and marketing content.
- [struct SubscriptionOptionGroupSet](subscriptionoptiongroupset.md)
  A set of groups of subscription options that include optional views for labels and marketing content.
- [struct SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [struct SubscriptionOptionSection](subscriptionoptionsection.md)
- [struct StoreContentBuilder](storecontentbuilder.md)
  A result builder that creates store content from closures that you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storecontent)*