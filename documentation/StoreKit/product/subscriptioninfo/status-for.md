# status(for:)

**Framework**: StoreKit  
**Kind**: method

Gets the subscription status for a subscription group identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func status(for groupID: String) async throws -> [Product.SubscriptionInfo.Status]
```

#### Return Value

An array of [`Product.SubscriptionInfo.Status`](product/subscriptioninfo/status-swift.struct.md). This array is empty if the customer has never subscribed to a product in this subscription group.

#### Discussion

To get the subscription group identifier of a subscription, see [`subscriptionGroupID`](product/subscriptioninfo/subscriptiongroupid.md) in [`Product.SubscriptionInfo`](product/subscriptioninfo.md), or [`subscriptionGroupID`](transaction/subscriptiongroupid.md) in [`Transaction`](transaction.md). You originally create subscription group identifiers when you set up in-app purchases in App Store Connect. For more information, see [`Offer auto-renewable subscriptions`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev75708c031).

Users can only buy one auto-renewable subscription within a group at a time. However, the returned array may contain multiple status values if your subscription supports Family Sharing, and the person has access to other subscriptions in the group through Family Sharing. For more information about Family Sharing, see [`Enable Family Sharing for your subscriptions`](https://developer.apple.comhttps://developer.apple.com/news/?id=ksfkdwpr).

## Parameters

- `groupID`: The subscription group identifier of the subscription to get status for.

## See Also

- [var status: [Product.SubscriptionInfo.Status]](product/subscriptioninfo/status-swift.property.md)
  An array that contains status information for a subscription group, including renewal and transaction information.
- [static func status(transactionID: UInt64) async throws -> SubscriptionStatus?](product/subscriptioninfo/status(transactionid:).md)
  Gets the subscription status for a transaction ID.
- [Product.SubscriptionInfo.Status](product/subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/status(for:))*