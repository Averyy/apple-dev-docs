# PagedProminentPickerSubscriptionStoreControlStyle

**Framework**: StoreKit  
**Kind**: struct

A subscription store control style that displays subscription plans as a paged prominent picker control, with a single button to subscribe.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency struct PagedProminentPickerSubscriptionStoreControlStyle
```

## Topics

### Getting the paged prominent picker control style
- [static var pagedProminentPicker: PagedProminentPickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/pagedprominentpicker.md)
  A subscription store control style that displays subscription plans as a prominent paged picker control, with a single button to subscribe.
### Creating the style
- [init()](pagedprominentpickersubscriptionstorecontrolstyle/init.md)
  Creates the paged prominent picker control style.
### Placing the controls
- [PagedProminentPickerSubscriptionStoreControlStyle.Placement](pagedprominentpickersubscriptionstorecontrolstyle/placement.md)

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
- [struct ProminentPickerSubscriptionStoreControlStyle](prominentpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.
- [struct CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [struct PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [struct AutomaticSubscriptionStoreControlPlacement](automaticsubscriptionstorecontrolplacement.md)
  A system-defined placement for a subscription store view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/pagedprominentpickersubscriptionstorecontrolstyle)*