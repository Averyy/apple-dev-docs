# subscriptionGroupIdentifier

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The identifier of the subscription group that the subscription belongs to.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```
string subscriptionGroupIdentifier
```

## Discussion

Auto-renewable subscriptions always belong to a subscription group. You create the subscription group identifiers in App Store Connect before you create and add an auto-renewable subscription. For more information about subscription groups, see [Offer auto-renewable subscriptions](https://help.apple.com/app-store-connect/#/dev75708c031).

## See Also

### Product information
- [type productId](./productid.md)
  The product identifier of the In-App Purchase.
- [type type](./type.md)
  The product type of the In-App Purchase.
- [type quantity](./quantity.md)
  The number of products or seats the customer purchased.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/subscriptiongroupidentifier)*