# quantity

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The number of products or seats the customer purchased.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```
int32 quantity
```

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

#### Discussion

For a subscription that a customer buys as a multiseat purchase, this value is the number of seats the purchase covers. For all other in-app purchase types, it’s the number of products the customer bought.

## See Also

### Product information
- [type productId](./productid.md)
  The product identifier of the In-App Purchase.
- [type type](./type.md)
  The product type of the In-App Purchase.
- [type subscriptionGroupIdentifier](./subscriptiongroupidentifier.md)
  The identifier of the subscription group that the subscription belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/quantity)*