# subscriptionGroupID

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The subscription group identifier for this subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let subscriptionGroupID: String
```

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create the subscription group identifiers in App Store Connect before you create and add an auto-renewable subscription. For more information about subscription groups, see [Offer auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev75708c031).

## See Also

### Identifying the subscription group
- [var groupDisplayName: String](./groupdisplayname.md)
  The localized name of the subscription group, suitable for display.
- [var groupLevel: Int](./grouplevel.md)
  The rank of the subscription relative to other subscriptions in the same subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/subscriptiongroupid)*