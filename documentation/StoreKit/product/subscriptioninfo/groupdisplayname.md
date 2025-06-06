# groupDisplayName

**Framework**: StoreKit  
**Kind**: property

The localized name of the subscription group, suitable for display.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
@backDeployed(before: iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0)
var groupDisplayName: String { get }
```

#### Discussion

You provide a group display name in App Store Connect when you set up a subscription group. For more information, see [`Offer auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev75708c031).

The [`SubscriptionStoreView`](subscriptionstoreview.md) uses this value as part of the automatic marketing content if you don’t provide a marketing content view.

> **Note**:  When you create a new product in App Store Connect or in a StoreKit configuration file, you can test it before you add a product localization. The [`groupDisplayName`](product/subscriptioninfo/groupdisplayname.md) value is an empty string until you add a localization. For more information on localizations, see [`Add localizations`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions#add-localizations).

 When you create a new product in App Store Connect or in a StoreKit configuration file, you can test it before you add a product localization. The [`groupDisplayName`](product/subscriptioninfo/groupdisplayname.md) value is an empty string until you add a localization. For more information on localizations, see [`Add localizations`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/offer-auto-renewable-subscriptions#add-localizations).

## See Also

- [let subscriptionGroupID: String](product/subscriptioninfo/subscriptiongroupid.md)
  The subscription group identifier for this subscription.
- [var groupLevel: Int](product/subscriptioninfo/grouplevel.md)
  The rank of the subscription relative to other subscriptions in the same subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/groupdisplayname)*