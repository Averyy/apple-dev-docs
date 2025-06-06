# PagedPickerSubscriptionStoreControlStyle

**Framework**: StoreKit  
**Kind**: struct

A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency struct PagedPickerSubscriptionStoreControlStyle
```

## Topics

### Getting the paged picker control style
- [static var pagedPicker: PagedPickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/pagedpicker.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
### Creating the style
- [init()](pagedpickersubscriptionstorecontrolstyle/init.md)
  Creates a paged picker control style.
### Placing the controls
- [PagedPickerSubscriptionStoreControlStyle.Placement](pagedpickersubscriptionstorecontrolstyle/placement.md)
  The placement of paged subscription picker in a subscription store view.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/pagedpickersubscriptionstorecontrolstyle)*