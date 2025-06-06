# SubscriptionStorePickerOption

**Framework**: StoreKit  
**Kind**: struct

A subscription option within a subscription picker control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency struct SubscriptionStorePickerOption<Label> where Label : View
```

## Topics

### Creating a subscription picker option
- [init(SubscriptionStoreControlStyleConfiguration.Option)](subscriptionstorepickeroption/init(_:)-4cb3l.md)
- [init(SubscriptionStoreControlStyleConfiguration.PickerOption)](subscriptionstorepickeroption/init(_:)-3iu97.md)
- [init(SubscriptionStoreControlStyleConfiguration.Option, label: (SubscriptionStoreControlStyleConfiguration.PickerOption) -> Label)](subscriptionstorepickeroption/init(_:label:).md)
### Supporting types
- [struct AutomaticSubscriptionStorePickerOptionLabel](automaticsubscriptionstorepickeroptionlabel.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct SubscriptionStoreButton](subscriptionstorebutton.md)
  A button for subscribing to an in-app subscription with a localized label and optional caption.
- [struct SubscriptionStorePicker](subscriptionstorepicker.md)
  A composite control with a picker for selecting a subscription option and a button for confirming the subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorepickeroption)*