# SubscriptionStoreControlStyleConfiguration.Section

**Framework**: StoreKit  
**Kind**: struct

The properties of a section of subscription options within a subscription store control.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct Section
```

#### Overview

Each value represents an instance of [`SubscriptionOptionSection`](subscriptionoptionsection.md) when the system creates a [`SubscriptionStoreView`](subscriptionstoreview.md).

Even if a subscription store instance doesn’t declare sections using [`SubscriptionOptionSection`](subscriptionoptionsection.md), the instance always has at least one implicit section that contains the options within the group. Implicit sections have `nil` for the [`header`](subscriptionstorecontrolstyleconfiguration/section/header-swift.property.md) and [`footer`](subscriptionstorecontrolstyleconfiguration/section/footer-swift.property.md) accessory views.

## Topics

### Getting a section’s content
- [var options: [SubscriptionStoreControlStyleConfiguration.Option]](subscriptionstorecontrolstyleconfiguration/section/options.md)
  The subscription options to merchandise within a section.
### Getting accessory views
- [var header: SubscriptionStoreControlStyleConfiguration.Section.Header?](subscriptionstorecontrolstyleconfiguration/section/header-swift.property.md)
  A decorative header view for a section that displays before the options.
- [var footer: SubscriptionStoreControlStyleConfiguration.Section.Footer?](subscriptionstorecontrolstyleconfiguration/section/footer-swift.property.md)
  A decorative footer view for a section that displays after the options.
- [SubscriptionStoreControlStyleConfiguration.Section.Header](subscriptionstorecontrolstyleconfiguration/section/header-swift.struct.md)
  A type-erased header of a section of subscription options.
- [SubscriptionStoreControlStyleConfiguration.Section.Footer](subscriptionstorecontrolstyleconfiguration/section/footer-swift.struct.md)
  A type-erased footer of a section of subscription options.
### Identifying a section
- [SubscriptionStoreControlStyleConfiguration.Section.ID](subscriptionstorecontrolstyleconfiguration/section/id.md)
  The stable identity of a section of subscription options.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [var options: [SubscriptionStoreControlStyleConfiguration.Option]](subscriptionstorecontrolstyleconfiguration/options.md)
  An array of subscription options for the subscription store view to merchandise.
- [var sections: [SubscriptionStoreControlStyleConfiguration.Section]](subscriptionstorecontrolstyleconfiguration/sections.md)
  The subscription options to merchandise by sections.
- [SubscriptionStoreControlStyleConfiguration.Option](subscriptionstorecontrolstyleconfiguration/option.md)
  Properties of an auto-renewable subscription option to merchandise.
- [SubscriptionStoreControlStyleConfiguration.PickerOption](subscriptionstorecontrolstyleconfiguration/pickeroption.md)
  The properties of a picker option to use for selecting a subscription.
- [SubscriptionStoreControlStyleConfiguration.Icon](subscriptionstorecontrolstyleconfiguration/icon.md)
  A type-erased icon of a subscription option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/section)*