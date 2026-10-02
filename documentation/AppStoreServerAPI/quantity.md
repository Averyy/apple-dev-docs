# quantity

**Framework**: App Store Server API  
**Kind**: typealias

The number of products or seats the customer purchased.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
int32 quantity
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

For a subscription that a customer buys as a multiseat purchase, this value is the number of seats the purchase covers. For all other in-app purchase types, it’s the number of products the customer bought.

## See Also

- [type productId](productid.md)
  The unique identifier of the product.
- [type type](type.md)
  The type of In-App Purchase products you can offer in your app.
- [type subscriptionGroupIdentifier](subscriptiongroupidentifier.md)
  The identifier of the subscription group that the subscription belongs to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/quantity)*