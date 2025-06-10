# SubscriptionStoreControlStyleConfiguration.Option

**Framework**: StoreKit  
**Kind**: struct

Properties of an auto-renewable subscription option to merchandise.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@dynamicMemberLookup
struct Option
```

#### Overview

You use `SubscriptionStoreControlStyleConfiguration.Option` very similarly to [`Product`](product.md) values, with some important differences:

- The `offer` property indicates the offer that applies to the purchase. Display the terms of the `offer`, and ignore offer properties on [`Product.SubscriptionInfo`](product/subscriptioninfo.md), such as [`introductoryOffer`](product/subscriptioninfo/introductoryoffer.md).
- If the `offer` is `nil`, no offer applies to the purchase.
- Call the [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) method when a customer activates a control to subscribe to a subscription option, instead of methods on [`Product`](product.md), such as [`purchase(confirmIn:options:)`](product/purchase(confirmin:options:)-6dj6y.md).
- Access the decorative icon using the [`icon`](subscriptionstorecontrolstyleconfiguration/option/icon.md) property.

`SubscriptionStoreControlStyleConfiguration.Option` is a dynamic member lookup type, so you don’t need to use [`subscription`](subscriptionstorecontrolstyleconfiguration/option/subscription.md) directly to access the properties of the `Product` value. Instead, access the properties of `Product` or [`Product.SubscriptionInfo`](product/subscriptioninfo.md) directly on the `Option` value. In the example below, the [`displayName`](product/displayname.md) property is available on `Option` to use as the button label:

```swift
struct DisplayNameButtonsControlStyle: SubscriptionStoreControlStyle {

    func makeBody(configuration: Configuration) -> some View {
        ForEach(configuration.options) { option in
            Button(option.displayName, action: option.subscribe)
        }
    }
}
```

## Topics

### Getting the subscription product and offer
- [var subscription: Product](subscriptionstorecontrolstyleconfiguration/option/subscription.md)
  The auto-renewable subscription to merchandise.
- [var id: Product.ID](subscriptionstorecontrolstyleconfiguration/option/id.md)
  The product ID of the auto-renewable subscription.
- [var activeOffer: Product.SubscriptionOffer?](subscriptionstorecontrolstyleconfiguration/option/activeoffer.md)
  The subscription offer the customer is eligible for, and that applies to the subscription option.
### Getting the icon
- [var icon: SubscriptionStoreControlStyleConfiguration.Icon?](subscriptionstorecontrolstyleconfiguration/option/icon.md)
  The subscription option’s icon.
### Purchasing a subscription option
- [func subscribe()](subscriptionstorecontrolstyleconfiguration/option/subscribe.md)
  Initiates a purchase when a customer activates a control to subscribe to the option.
### Looking up dynamic members
- [subscript<T>(dynamicMember _: KeyPath<Product.SubscriptionInfo, T?>) -> T?](subscriptionstorecontrolstyleconfiguration/option/subscript(dynamicmember:)-8sl2m.md)
  Facilitates accessing optional subscription properties on an option value.
- [subscript<T>(dynamicMember _: KeyPath<Product.SubscriptionInfo, T>) -> T?](subscriptionstorecontrolstyleconfiguration/option/subscript(dynamicmember:)-wjww.md)
  Facilitates accessing subscription properties on an option value.
- [subscript<T>(dynamicMember _: KeyPath<Product, T>) -> T](subscriptionstorecontrolstyleconfiguration/option/subscript(dynamicmember:)-9g2sm.md)
  Facilitates accessing product properties on an option value.
### Default Implementations
- [Identifiable Implementations](subscriptionstorecontrolstyleconfiguration/option/identifiable-implementations.md)

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
- [SubscriptionStoreControlStyleConfiguration.PickerOption](subscriptionstorecontrolstyleconfiguration/pickeroption.md)
  The properties of a picker option to use for selecting a subscription.
- [SubscriptionStoreControlStyleConfiguration.Section](subscriptionstorecontrolstyleconfiguration/section.md)
  The properties of a section of subscription options within a subscription store control.
- [SubscriptionStoreControlStyleConfiguration.Icon](subscriptionstorecontrolstyleconfiguration/icon.md)
  A type-erased icon of a subscription option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/option)*