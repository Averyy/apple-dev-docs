# isUpgraded

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the user upgraded to another subscription.

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
let isUpgraded: Bool
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../managing-the-life-cycle-of-multiseat-subscriptions.md)
- [Supporting monthly subscriptions with a 12-month commitment](../supporting-monthly-subscriptions-with-a-12-month-commitment.md)

## Discussion

If [`isUpgraded`](./isupgraded.md) is `true`, the user has upgraded the subscription represented by this transaction to another subscription. This value appears in the transaction only when the value is `true`. To determine the service that the customer is entitled to, look for another transaction that has a subscription with a higher level of service.

## See Also

### Getting purchase details
- [let ownershipType: Transaction.OwnershipType](./ownershiptype-swift.property.md)
  A value that indicates whether the customer purchased the product or has access to it through Family Sharing, an organization, or a group.
- [Transaction.OwnershipType](./ownershiptype-swift.struct.md)
  Values that indicate whether the customer purchased the product or has access to it through Family Sharing, an organization, or a group.
- [let purchasedQuantity: Int](./purchasedquantity.md)
  The number of purchased seats or consumable products.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/isupgraded)*