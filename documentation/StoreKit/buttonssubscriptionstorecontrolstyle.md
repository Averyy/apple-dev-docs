# ButtonsSubscriptionStoreControlStyle

**Framework**: StoreKit  
**Kind**: struct

A subscription store control style that displays a subscribe button for each subscription plan.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency struct ButtonsSubscriptionStoreControlStyle
```

## Topics

### Getting the button subscription store style
- [static var buttons: ButtonsSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/buttons.md)
  A subscription store control style that displays a subscribe button for each subscription plan.
### Creating the style
- [init()](buttonssubscriptionstorecontrolstyle/init.md)
  Creates a button subscription store control style.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## See Also

- [struct AutomaticSubscriptionStoreControlStyle](automaticsubscriptionstorecontrolstyle.md)
  The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [struct PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [struct CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [struct PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/buttonssubscriptionstorecontrolstyle)*