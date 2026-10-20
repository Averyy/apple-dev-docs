# ButtonsSubscriptionStoreControlStyle

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A subscription store control style that displays a subscribe button for each subscription plan.

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
@MainActor
@preconcurrency struct ButtonsSubscriptionStoreControlStyle
```

## Topics

### Getting the button subscription store style
- [static var buttons: ButtonsSubscriptionStoreControlStyle](./subscriptionstorecontrolstyle/buttons.md)
  A subscription store control style that displays a subscribe button for each subscription plan.
### Creating the style
- [init()](./buttonssubscriptionstorecontrolstyle/init%28%29.md)
  Creates a button subscription store control style.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SubscriptionStoreControlStyle](./subscriptionstorecontrolstyle.md)

## See Also

### Placement types
- [struct AutomaticSubscriptionStoreControlStyle](./automaticsubscriptionstorecontrolstyle.md)
  The default in-app subscription store control style that resolves its appearance based on the view’s context.
- [struct PickerSubscriptionStoreControlStyle](./pickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [struct CompactPickerSubscriptionStoreControlStyle](./compactpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a compact picker control, with a single button to subscribe.
- [struct PagedPickerSubscriptionStoreControlStyle](./pagedpickersubscriptionstorecontrolstyle.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/buttonssubscriptionstorecontrolstyle)*