# sections

**Framework**: StoreKit  
**Kind**: property

The subscription options to merchandise by sections.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var sections: [SubscriptionStoreControlStyleConfiguration.Section] { get }
```

#### Discussion

The [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) property represents the main content of your subscription store control style, including the auto-renewable subscription products.

Each [`SubscriptionStoreControlStyleConfiguration.Section`](subscriptionstorecontrolstyleconfiguration/section.md) element contains an array of [`SubscriptionStoreControlStyleConfiguration.Option`](subscriptionstorecontrolstyleconfiguration/option.md) values named [`options`](subscriptionstorecontrolstyleconfiguration/section/options.md). Use this structure to modify the appearance of a control depending on the section it belongs to.

The elements of [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) represent [`SubscriptionOptionSection`](subscriptionoptionsection.md) instances. A minimal store has one implicit section, with the [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) property containing a single element. The single element’s [`header`](subscriptionstorecontrolstyleconfiguration/section/header-swift.property.md) and [`footer`](subscriptionstorecontrolstyleconfiguration/section/footer-swift.property.md) properties are both `nil`, and its [`options`](subscriptionstorecontrolstyleconfiguration/section/options.md) property is identical to the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) property on [`SubscriptionStoreControlStyleConfiguration`](subscriptionstorecontrolstyleconfiguration.md).

> **Note**:  Typically, a style needs only one of the properties: [`options`](subscriptionstorecontrolstyleconfiguration/options.md) or [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md). Use the [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) property if your style supports sections.

 Typically, a style needs only one of the properties: [`options`](subscriptionstorecontrolstyleconfiguration/options.md) or [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md). Use the [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) property if your style supports sections.

Use the initializer of the [`SubscriptionStoreView`](subscriptionstoreview.md) to determine the contents of the [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) array.

Display only the subscription options that appear in the [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) array. Use the [`allOptions`](subscriptionstorecontrolstyleconfiguration/alloptions.md) property to access information about all the options, for example, to compute comparisons between subscription options. The view your style creates needs to provide a control that enables the customer to subscribe to each option in the array.

If you configure a subscription store view to show the current auto-renewal preference, the [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) array contains the [`autoRenewPreference`](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md) subscription product. There’s no need to specifically display the [`autoRenewPreference`](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md) product in that case.

## See Also

- [var options: [SubscriptionStoreControlStyleConfiguration.Option]](subscriptionstorecontrolstyleconfiguration/options.md)
  An array of subscription options for the subscription store view to merchandise.
- [SubscriptionStoreControlStyleConfiguration.Option](subscriptionstorecontrolstyleconfiguration/option.md)
  Properties of an auto-renewable subscription option to merchandise.
- [SubscriptionStoreControlStyleConfiguration.PickerOption](subscriptionstorecontrolstyleconfiguration/pickeroption.md)
  The properties of a picker option to use for selecting a subscription.
- [SubscriptionStoreControlStyleConfiguration.Section](subscriptionstorecontrolstyleconfiguration/section.md)
  The properties of a section of subscription options within a subscription store control.
- [SubscriptionStoreControlStyleConfiguration.Icon](subscriptionstorecontrolstyleconfiguration/icon.md)
  A type-erased icon of a subscription option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/sections)*