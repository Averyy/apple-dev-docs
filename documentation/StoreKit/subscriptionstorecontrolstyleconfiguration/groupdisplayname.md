# groupDisplayName

**Framework**: StoreKit  
**Kind**: property

The localized display name of the subscription group that the subscription store view merchandises.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var groupDisplayName: String { get }
```

#### Discussion

This property is the same as accessing [`groupDisplayName`](product/subscriptioninfo/groupdisplayname.md) on a [`Product.SubscriptionInfo`](product/subscriptioninfo.md) value. Because all options within a subscription store view belong to the same subscription group, using the [`groupDisplayName`](subscriptionstorecontrolstyleconfiguration/groupdisplayname.md) property is more convenient than getting the group display name from an arbitrary subscription option.

## See Also

- [var autoRenewPreference: Product?](subscriptionstorecontrolstyleconfiguration/autorenewpreference.md)
  The auto-renewable subscripton product that renews at the next billing cycle.
- [var allOptions: [Product]](subscriptionstorecontrolstyleconfiguration/alloptions.md)
  All subscription options in the subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyleconfiguration/groupdisplayname)*