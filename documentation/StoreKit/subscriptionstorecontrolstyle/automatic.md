# automatic

**Framework**: StoreKit  
**Kind**: property

A subscription store control style that resolves its appearance automatically, based on the current context.

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
@preconcurrency static var automatic: AutomaticSubscriptionStoreControlStyle { get }
```

#### Discussion

You can also use [`subscriptionStoreControlStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/subscriptionStoreControlStyle(_:)) with [`automatic`](subscriptionstorecontrolstyle/automatic.md) as the parameter to construct this style.

## See Also

- [static var buttons: ButtonsSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/buttons.md)
  A subscription store control style that displays a subscribe button for each subscription plan.
- [static var picker: PickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/picker.md)
  A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [static var prominentPicker: ProminentPickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/prominentpicker.md)
  A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.
- [static var pagedPicker: PagedPickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/pagedpicker.md)
  A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.
- [static var pagedProminentPicker: PagedProminentPickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/pagedprominentpicker.md)
  A subscription store control style that displays subscription plans as a prominent paged picker control, with a single button to subscribe.
- [static var compactPicker: CompactPickerSubscriptionStoreControlStyle](subscriptionstorecontrolstyle/compactpicker.md)
  A subscription store control style that displays subscription plans as a compact control, with a single button to subscribe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle/automatic)*