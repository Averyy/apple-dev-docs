# SubscriptionStoreControlStyle.Configuration

**Framework**: StoreKit  
**Kind**: typealias  
**Role**: Type Alias

The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
typealias Configuration = SubscriptionStoreControlStyleConfiguration
```

## See Also

### Creating custom subscription store control styles
- [func makeBody(configuration: Self.Configuration) -> Self.Body](./makebody%28configuration%29.md)
  Creates a view that represents the body of a subscription store control.
- [SubscriptionStoreControlStyle.SubscribeButton](./subscribebutton.md)
  A button for subscribing to an in-app subscription.
- [SubscriptionStoreControlStyle.SubscriptionPicker](./subscriptionpicker.md)
  A composite control for selecting a subscription option and confirming the subscription.
- [SubscriptionStoreControlStyle.SubscriptionPickerOption](./subscriptionpickeroption.md)
  A subscription option within a subscription picker control.
- [struct SubscriptionStoreControlPlacementKey](../subscriptionstorecontrolplacementkey.md)
  A placement for a subscription store control in a store view.
- [associatedtype Placement : SubscriptionStoreControlPlacement = AutomaticSubscriptionStoreControlPlacement](./placement.md)
  The placement of subscription controls in a subscription store.
- [associatedtype Body : View](./body.md)
  A view that represents the body of a subscription store control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle/configuration)*