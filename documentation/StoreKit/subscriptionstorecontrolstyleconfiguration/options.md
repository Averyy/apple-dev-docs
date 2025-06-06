# options

**Framework**: StoreKit  
**Kind**: property

An array of subscription options for the subscription store view to merchandise.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var options: [SubscriptionStoreControlStyleConfiguration.Option] { get }
```

#### Discussion

The [`options`](subscriptionstorecontrolstyleconfiguration/options.md) property is an array that contains the main content of your subscription store control style, including the auto-renewable subscription products. Use the properties of each [`options`](subscriptionstorecontrolstyleconfiguration/options.md) value to declare your control style. Provide a control that enables the customer to subscribe to each option in the array. Call the [`subscribe()`](subscriptionstorecontrolstyleconfiguration/option/subscribe().md) method when the customer activates a control to subscribe.

Display only the subscription options that appear in the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) array. Use the [`allOptions`](subscriptionstorecontrolstyleconfiguration/alloptions.md) property to access information about all the options, for example, to compute comparisons between subscription options.

To hide and sort subscription options, use the initializer of the [`SubscriptionStoreView`](subscriptionstoreview.md). The [`options`](subscriptionstorecontrolstyleconfiguration/options.md) array maintains the sort order, and includes only the options you provide to the subscription store view’s initializer. For example, the following code initializes the subscription store to contain only the subscription options that upgrade the customer’s current subscription:

```swift
SubscriptionStoreView(groupID: "SAMPLE", visibleRelationships: .upgrade)
```

If you configure a subscription store view to show the current auto-renewal preference, the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) array contains the [`autoRenewPreference`](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md) subscription product. There’s no need to specifically display the [`autoRenewPreference`](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md) product in that case.

> **Note**:  A subscription store control style needs only one of the properties, [`options`](subscriptionstorecontrolstyleconfiguration/options.md) or [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md). Use [`options`](subscriptionstorecontrolstyleconfiguration/options.md) if your style doesn’t support sections.

 A subscription store control style needs only one of the properties, [`options`](subscriptionstorecontrolstyleconfiguration/options.md) or [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md). Use [`options`](subscriptionstorecontrolstyleconfiguration/options.md) if your style doesn’t support sections.

If you declare a subscription store view using [`SubscriptionOptionSection`](subscriptionoptionsection.md) instances, this property flattens the section structure and ignores any header or footer views.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/options)*