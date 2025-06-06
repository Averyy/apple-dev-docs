# CompactPickerSubscriptionStoreControlStyle

**Framework**: StoreKit  
**Kind**: struct

A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency struct CompactPickerSubscriptionStoreControlStyle
```

#### Overview

This style lays out the picker options in a horizontal stack, and it can scroll horizontally if the contents are wider than the container. This style is recommended when you expect your store to display two or three subscription options.

## Topics

### Getting the compact picker control style
- [static var compactPicker: CompactPickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/compactpicker.md)
  A subscription store control style that displays subscription plans as a compact control, with a single button to subscribe.
### Creating the style
- [init()](compactpickersubscriptionstorecontrolstyle/init.md)
  Creates a compact picker subscription store control style.
### Placing the controls
- [CompactPickerSubscriptionStoreControlStyle.Placement](compactpickersubscriptionstorecontrolstyle/placement.md)
  The placement of the compact subscription picker in a subscription store view.

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
- [struct PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/compactpickersubscriptionstorecontrolstyle)*