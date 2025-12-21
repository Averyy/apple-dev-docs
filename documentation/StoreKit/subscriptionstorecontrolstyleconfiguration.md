# SubscriptionStoreControlStyleConfiguration

**Framework**: StoreKit  
**Kind**: struct

The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct SubscriptionStoreControlStyleConfiguration
```

#### Overview

When you define a custom subscription store control style by creating a type that conforms to the [`SubscriptionStoreControlStyle`](subscriptionstorecontrolstyle.md) protocol, you implement the [`makeBody(configuration:)`](subscriptionstorecontrolstyle/makebody(configuration:).md) method. That method takes a `SubscriptionStoreControlStyleConfiguration` parameter, which has the information necessary to define the behavior and interactions of a subscription store view’s primary controls.

Decide whether your style supports dividing options into sections.

- If you support sections, use the [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) property to preserve the structure and accessory views you declare using [`SubscriptionOptionSection`](subscriptionoptionsection.md) instances.
- If you don’t support sections, use the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) property to have a flattened array of the [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) values to merchandise.

Provide a control that enables customers to subscribe to each option in either the `options` or `sections` properties.

To hide and sort the subscription options that your view displays, use the initializer of the [`SubscriptionStoreView`](subscriptionstoreview.md). For example, you can initialize the subscription store to contain only the subscription options that upgrade the customer’s current subscription.

Display only the subscription options that appear in either the `options` or `sections` properties. For example, declaring [`SubscriptionOptionGroup`](subscriptionoptiongroup.md) instances can hide certain subscription options from a control. To access information about other subscription options, use the [`allOptions`](subscriptionstorecontrolstyleconfiguration/alloptions.md) property.

In cases where a customer is actively subscribed, use [`autoRenewPreference`](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md) to get the [`Product`](product.md) value of the subscription product that renews at the next billing.

## Topics

### Getting subscription options to merchandise
- [var options: [SubscriptionStoreControlStyleConfiguration.Option]](subscriptionstorecontrolstyleconfiguration/options.md)
  An array of subscription options for the subscription store view to merchandise.
- [var sections: [SubscriptionStoreControlStyleConfiguration.Section]](subscriptionstorecontrolstyleconfiguration/sections.md)
  The subscription options to merchandise by sections.
- [SubscriptionStoreControlStyleConfiguration.Option](subscriptionstorecontrolstyleconfiguration/option.md)
  Properties of an auto-renewable subscription option to merchandise.
- [SubscriptionStoreControlStyleConfiguration.PickerOption](subscriptionstorecontrolstyleconfiguration/pickeroption.md)
  The properties of a picker option to use for selecting a subscription.
- [SubscriptionStoreControlStyleConfiguration.Section](subscriptionstorecontrolstyleconfiguration/section.md)
  The properties of a section of subscription options within a subscription store control.
- [SubscriptionStoreControlStyleConfiguration.Icon](subscriptionstorecontrolstyleconfiguration/icon.md)
  A type-erased icon of a subscription option.
### Getting subscription group properties
- [var groupDisplayName: String](subscriptionstorecontrolstyleconfiguration/groupdisplayname.md)
  The localized display name of the subscription group that the subscription store view merchandises.
- [var autoRenewPreference: Product?](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md)
  The auto-renewable subscripton product that renews at the next billing cycle.
- [var allOptions: [Product]](subscriptionstorecontrolstyleconfiguration/alloptions.md)
  All subscription options in the subscription group.
### Getting subscription description visibility
- [var descriptionVisibility: Visibility](subscriptionstorecontrolstyleconfiguration/descriptionvisibility.md)
  The visibility of product descriptions.

## See Also

- [func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) -> some View](../SwiftUI/View/subscriptionStoreControlStyle(_:).md)
  Sets the control style for subscription store views within a view.
- [func subscriptionStoreControlStyle<S>(S, placement: S.Placement) -> some View](../SwiftUI/View/subscriptionStoreControlStyle(_:placement:).md)
  Sets the control style and control placement for subscription store views within a view.
- [protocol SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)
  A type that specifies the appearance and interaction of controls in the subscription store view instances within the view hierarchy.
- [protocol SubscriptionStoreControlPlacement](subscriptionstorecontrolplacement.md)
  A type that specifies the placement of a subscription control in a subscription store view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration)*