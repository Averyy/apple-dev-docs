# Placement

**Framework**: StoreKit  
**Kind**: associatedtype  
**Required**: Yes

The placement of subscription controls in a subscription store.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
associatedtype Placement : SubscriptionStoreControlPlacement = AutomaticSubscriptionStoreControlPlacement
```

## See Also

- [func makeBody(configuration: Self.Configuration) -> Self.Body](subscriptionstorecontrolstyle/makebody(configuration:).md)
  Creates a view that represents the body of a subscription store control.
- [SubscriptionStoreControlStyle.Configuration](subscriptionstorecontrolstyle/configuration.md)
  The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.
- [SubscriptionStoreControlStyle.SubscribeButton](subscriptionstorecontrolstyle/subscribebutton.md)
  A button for subscribing to an in-app subscription.
- [SubscriptionStoreControlStyle.SubscriptionPicker](subscriptionstorecontrolstyle/subscriptionpicker.md)
  A composite control for selecting a subscription option and confirming the subscription.
- [SubscriptionStoreControlStyle.SubscriptionPickerOption](subscriptionstorecontrolstyle/subscriptionpickeroption.md)
  A subscription option within a subscription picker control.
- [struct SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey.md)
  A placement for a subscription store control in a store view.
- [associatedtype Body : View](subscriptionstorecontrolstyle/body.md)
  A view that represents the body of a subscription store control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle/placement)*