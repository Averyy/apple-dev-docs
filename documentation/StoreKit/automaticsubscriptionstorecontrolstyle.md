# AutomaticSubscriptionStoreControlStyle

**Framework**: StoreKit  
**Kind**: struct

The default in-app subscription store control style that resolves its appearance based on the view’s context.

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
@preconcurrency struct AutomaticSubscriptionStoreControlStyle
```

## Topics

### Getting the automatic subscription store control style
- [static var automatic: AutomaticSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/automatic.md)
  A subscription store control style that resolves its appearance automatically, based on the current context.
### Creating the style
- [init()](automaticsubscriptionstorecontrolstyle/init.md)
  Creates an automatic subscription store control style.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)

## See Also

- [struct ButtonsSubscriptionStoreControlStyle](buttonssubscriptionstorecontrolstyle.md)
  A subscription store control style that displays a subscribe button for each subscription plan.
- [struct PickerSubscriptionStoreControlStyle](pickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [struct CompactPickerSubscriptionStoreControlStyle](compactpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [struct PagedPickerSubscriptionStoreControlStyle](pagedpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/automaticsubscriptionstorecontrolstyle)*