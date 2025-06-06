# SubscriptionStoreControlStyleConfiguration.PickerOption

**Framework**: StoreKit  
**Kind**: struct

The properties of a picker option to use for selecting a subscription.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@dynamicMemberLookup
struct PickerOption
```

#### Overview

You use `SubscriptionStoreControlStyleConfiguration.PickerOption` very similarly to [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md). The key differences are:

- The picker option represents a subscription option within the scope of an element of a picker control, where you can merchandise a standard option using any kind of control.
- Instead of getting an option from a [`SubscriptionStoreControlStyleConfiguration`](subscriptionstorecontrolstyleconfiguration.md), you get a picker option when you create a [`SubscriptionStorePicker`](subscriptionstorepicker.md).
- Instead of providing a [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) method, the picker option provides an [`isSelected`](subscriptionstorecontrolstyleconfiguration/pickeroption/isselected.md) property to get the selection state.

The key difference is a `SubscriptionStoreControlStyleConfiguration.Option` provides a method to subscribe, and a `SubscriptionStoreControlStyleConfiguration.PickerOption` indicates the current selection state within a [`SubscriptionStorePicker`](subscriptionstorepicker.md).

[`SubscriptionStoreControlStyleConfiguration.PickerOption`](subscriptionstorecontrolstyleconfiguration/pickeroption.md) is a dynamic member lookup type, so you don’t need to use [`subscription`](subscriptionstorecontrolstyleconfiguration/pickeroption/subscription.md) directly to access the properties of the `Product` value. Instead, access any properties of `Product` or [`Product.SubscriptionInfo`](product/subscriptioninfo.md) directly on the `PickerOption` value.

## Topics

### Getting properties of the subscription picker option
- [var subscription: Product](subscriptionstorecontrolstyleconfiguration/pickeroption/subscription.md)
  The auto-renewable subscription that the picker option represents.
- [var activeOffer: Product.SubscriptionOffer?](subscriptionstorecontrolstyleconfiguration/pickeroption/activeoffer.md)
- [let isSelected: Bool](subscriptionstorecontrolstyleconfiguration/pickeroption/isselected.md)
  A Boolean value that indicates whether the picker option is in a selected state.
- [var icon: SubscriptionStoreControlStyleConfiguration.Icon?](subscriptionstorecontrolstyleconfiguration/pickeroption/icon.md)
  The subscription option’s icon.
- [var id: Product.ID](subscriptionstorecontrolstyleconfiguration/pickeroption/id.md)
### Dynamic member lookup support
- [subscript<T>(dynamicMember _: KeyPath<Product.SubscriptionInfo, T?>) -> T?](subscriptionstorecontrolstyleconfiguration/pickeroption/subscript(dynamicmember:)-2ahxy.md)
  Facilitates accessing optional subscription properties on a picker option value.
- [subscript<T>(dynamicMember _: KeyPath<Product.SubscriptionInfo, T>) -> T?](subscriptionstorecontrolstyleconfiguration/pickeroption/subscript(dynamicmember:)-4f3i1.md)
  Facilitates accessing subscription properties on a picker option value.
- [subscript<T>(dynamicMember _: KeyPath<Product, T>) -> T](subscriptionstorecontrolstyleconfiguration/pickeroption/subscript(dynamicmember:)-8bsxh.md)
  Facilitates accessing product properties on a picker option value.
### Default Implementations
- [Identifiable Implementations](subscriptionstorecontrolstyleconfiguration/pickeroption/identifiable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [var options: [SubscriptionStoreControlStyleConfiguration.Option]](subscriptionstorecontrolstyleconfiguration/options.md)
  An array of subscription options for the subscription store view to merchandise.
- [var sections: [SubscriptionStoreControlStyleConfiguration.Section]](subscriptionstorecontrolstyleconfiguration/sections.md)
  The subscription options to merchandise by sections.
- [SubscriptionStoreControlStyleConfiguration.Option](subscriptionstorecontrolstyleconfiguration/option.md)
  Properties of an auto-renewable subscription option to merchandise.
- [SubscriptionStoreControlStyleConfiguration.Section](subscriptionstorecontrolstyleconfiguration/section.md)
  The properties of a section of subscription options within a subscription store control.
- [SubscriptionStoreControlStyleConfiguration.Icon](subscriptionstorecontrolstyleconfiguration/icon.md)
  A type-erased icon of a subscription option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/pickeroption)*