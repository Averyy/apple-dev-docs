# pagedPicker

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

A subscription store control style that displays subscription plans as a paged picker control, with a single button to subscribe.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency static var pagedPicker: PagedPickerSubscriptionStoreControlStyle { get }
```

Available when `Self` is `PagedPickerSubscriptionStoreControlStyle`.

## See Also

### Getting built-in subscription store control styles
- [static var automatic: AutomaticSubscriptionStoreControlStyle](./automatic.md)
  A subscription store control style that resolves its appearance automatically, based on the current context.
- [static var buttons: ButtonsSubscriptionStoreControlStyle](./buttons.md)
  A subscription store control style that displays a subscribe button for each subscription plan.
- [static var picker: PickerSubscriptionStoreControlStyle](./picker.md)
  A subscription store control style that displays subscription plans as a picker control, with a single button to subscribe.
- [static var prominentPicker: ProminentPickerSubscriptionStoreControlStyle](./prominentpicker.md)
  A subscription store control style that displays subscription plans as a prominent picker control, with a single button to subscribe.
- [static var pagedProminentPicker: PagedProminentPickerSubscriptionStoreControlStyle](./pagedprominentpicker.md)
  A subscription store control style that displays subscription plans as a prominent paged picker control, with a single button to subscribe.
- [static var compactPicker: CompactPickerSubscriptionStoreControlStyle](./compactpicker.md)
  A subscription store control style that displays subscription plans as a compact control, with a single button to subscribe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle/pagedpicker)*