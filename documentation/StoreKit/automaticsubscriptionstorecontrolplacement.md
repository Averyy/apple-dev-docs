# AutomaticSubscriptionStoreControlPlacement

**Framework**: StoreKit  
**Kind**: struct

A system-defined placement for a subscription store view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct AutomaticSubscriptionStoreControlPlacement
```

#### Overview

You typically don’t use this type directly, except when you implement a custom control style. By default, a custom control style supports all placements. For more information, see the [`SubscriptionStoreControlPlacement`](subscriptionstorecontrolplacement.md) protocol.

## Topics

### Getting automatic placements
- [static var automatic: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/automatic.md)
  A context-appropriate placement that the system determines automatically.
- [static var bottomBar: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/bottombar.md)
  A placement that locates the subscription controls in a bar near the bottom of the main scroll view in a subscription store view.
- [static var buttonsInBottomBar: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/buttonsinbottombar.md)
  A hybrid placement that positions subscription controls within the main scroll view, and places auxiliary buttons in the bottom bar.
- [static var scrollView: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/scrollview.md)
  A placement that locates the subscription controls within the main scroll view of a subscription store view.
- [static var bottom: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/bottom.md)
  A placement that anchors the subscription controls to the bottom edge of the view.
- [static var leading: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/leading.md)
  A placement that anchors the subscription controls to the leading edge of the view.
- [static var trailing: AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement/trailing.md)
  A placement that anchors the subscription controls to the trailing edge of the view.

## Relationships

### Conforms To
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SubscriptionStoreControlPlacement](subscriptionstorecontrolplacement.md)

## See Also

- [struct AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md)
  The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [struct ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md)
  A subscription store control style that displays a subscribe button for each subscription plan.
- [struct PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [struct ProminentPickerSubscriptionStoreControlStyle](prominentpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.
- [struct CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [struct PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [struct PagedProminentPickerSubscriptionStoreControlStyle](pagedprominentpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged prominent picker control, with a single button to subscribe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/automaticsubscriptionstorecontrolplacement)*