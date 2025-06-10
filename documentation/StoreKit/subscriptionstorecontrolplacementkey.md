# SubscriptionStoreControlPlacementKey

**Framework**: StoreKit  
**Kind**: struct

A placement for a subscription store control in a store view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct SubscriptionStoreControlPlacementKey
```

#### Overview

This type represents all available control placements. You typically don’t interact with this type directly. Use it if you create a custom control style that conforms to the [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md) protocol to restrict the supported placements for your style. By default, a custom control style supports all placements. For more information, see [`SubscriptionStoreControlPlacement`](subscriptionstorecontrolplacement.md).

## Topics

### Placing subscription store controls
- [static var bottom: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/bottom.md)
  A placement that anchors the subscription controls to the bottom edge of the view.
- [static var leading: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/leading.md)
  A placement that anchors the subscription controls to the leading edge of the view.
- [static var scrollView: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/scrollview.md)
  A placement that locates the subscription controls within the main scroll view of a subscription store view.
- [static var trailing: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/trailing.md)
  A placement that anchors the subscription controls to the trailing edge of the view.
- [static var bottomBar: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/bottombar.md)
  A placement that locates the subscription controls in a bar near the bottom of the main scroll view in a subscription store view.
- [static var buttonsInBottomBar: SubscriptionStoreControlPlacementKey](subscriptionstorecontrolplacementkey/buttonsinbottombar.md)
  A hybrid placement that positions subscription controls within the main scroll view, and places auxiliary buttons in the bottom bar.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [associatedtype Placement : SubscriptionStoreControlPlacement = AutomaticSubscriptionStoreControlPlacement](subscriptionstorecontrolstyle/placement.md)
  The placement of subscription controls in a subscription store.
- [associatedtype Body : View](subscriptionstorecontrolstyle/body.md)
  A view that represents the body of a subscription store control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolplacementkey)*