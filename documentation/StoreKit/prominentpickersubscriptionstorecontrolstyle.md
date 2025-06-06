# ProminentPickerSubscriptionStoreControlStyle

**Framework**: StoreKit  
**Kind**: struct

A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Declaration

```swift
@MainActor
@preconcurrency struct ProminentPickerSubscriptionStoreControlStyle
```

## Topics

### Getting the prominent picker control style
- [static var pagedProminentPicker: PagedProminentPickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/pagedprominentpicker.md)
  A subscription store control style that displays subscription plans as a prominent paged picker control, with a single button to subscribe.
### Creating the style
- [init()](prominentpickersubscriptionstorecontrolstyle/init.md)
  Creates a prominent picker subscription store control style.
### Placing the controls
- [associatedtype Placement : SubscriptionStoreControlPlacement = AutomaticSubscriptionStoreControlPlacement](subscriptionstorecontrolstyle/placement.md)
  The placement of subscription controls in a subscription store.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## See Also

- [struct AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md)
  The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [struct ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md)
  A subscription store control style that displays a subscribe button for each subscription plan.
- [struct PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [struct CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [struct PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [struct PagedProminentPickerSubscriptionStoreControlStyle](pagedprominentpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged prominent picker control, with a single button to subscribe.
- [struct AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement.md)
  A system-defined placement for a subscription store view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/prominentpickersubscriptionstorecontrolstyle)*