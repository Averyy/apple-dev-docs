# allOptions

**Framework**: StoreKit  
**Kind**: property

All subscription options in the subscription group.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var allOptions: [Product] { get }
```

#### Discussion

The [`allOptions`](subscriptionstorecontrolstyleconfiguration/alloptions.md) property is an array that contains all the subscription options in a subscription group. Use the [`allOptions`](subscriptionstorecontrolstyleconfiguration/alloptions.md) property to access the subscription options that the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) and [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) properties may not contain.

For example, use the [`allOptions`](subscriptionstorecontrolstyleconfiguration/alloptions.md) property if your control style displays comparisons between available subscription options. A [`SubscriptionPeriodGroupSet`](subscriptionperiodgroupset.md) can compare the value of a yearly renewing subscription to a monthly subscription. Because each instance of your control style displays only subscriptions with matching renewal periods, you can’t compute such a comparison using the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) property. The [`allOptions`](subscriptionstorecontrolstyleconfiguration/alloptions.md) value is always a superset of the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) property.

> **Note**:  Don’t use the [`allOptions`](subscriptionstorecontrolstyleconfiguration/alloptions.md) property to determine the subscription options your control style view displays. Instead, only display the subscription options that the [`options`](subscriptionstorecontrolstyleconfiguration/options.md) or [`sections`](subscriptionstorecontrolstyleconfiguration/sections.md) properties contain.

It’s possible for a subscription store control to display only a subset of the options available within a subscription group. For example, if you use a store content builder to declare the content of a [`SubscriptionStoreView`](subscriptionstoreview.md), the store may create multiple instances of your control with different configuration values. These instances may each display a different subset of the subscripton options.

## See Also

- [var groupDisplayName: String](subscriptionstorecontrolstyleconfiguration/groupdisplayname.md)
  The localized display name of the subscription group that the subscription store view merchandises.
- [var autoRenewPreference: Product?](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md)
  The auto-renewable subscripton product that renews at the next billing cycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/alloptions)*