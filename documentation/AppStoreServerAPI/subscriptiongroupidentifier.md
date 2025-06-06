# subscriptionGroupIdentifier

**Framework**: App Store Server API  
**Kind**: typealias

The identifier of the subscription group that the subscription belongs to.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
string subscriptionGroupIdentifier
```

#### Discussion

Auto-renewable subscriptions always belong to a subscription group. You create the subscription group identifiers in App Store Connect before you create and add an auto-renewable subscription. For more information about subscription groups, see [`Offer auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev75708c031).

## See Also

- [type productId](productid.md)
  The unique identifier of the product, which you create in App Store Connect.
- [type type](type.md)
  The type of In-App Purchase products you can offer in your app.
- [type quantity](quantity.md)
  The number of purchased consumable products.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/subscriptiongroupidentifier)*