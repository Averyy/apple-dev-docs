# PickerSubscriptionStoreControlStyle

**Framework**: StoreKit  
**Kind**: struct

A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct PickerSubscriptionStoreControlStyle
```

## Topics

### Getting the picker control style
- [static var picker: PickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/picker.md)
  A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
### Placing the controls
- [associatedtype Placement : SubscriptionStoreControlPlacement = AutomaticSubscriptionStoreControlPlacement](subscriptionstorecontrolstyle/placement.md)
  The placement of subscription controls in a subscription store.
### Creating the style
- [init()](pickersubscriptionstorecontrolstyle/init.md)
  Creates a picker subscription store control style.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## See Also

- [struct AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md)
  The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [struct ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md)
  A subscription store control style that displays a subscribe button for each subscription plan.
- [struct CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [struct PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/pickersubscriptionstorecontrolstyle)*