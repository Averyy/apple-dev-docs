# purchasedQuantity

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The number of purchased seats or consumable products.

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
let purchasedQuantity: Int
```

## Mentions

- [Managing the life cycle of multiseat subscriptions](../managing-the-life-cycle-of-multiseat-subscriptions.md)
- [Supporting multiseat purchases in your app](../supporting-multiseat-purchases-in-your-app.md)
- [Testing multiseat subscriptions](../testing-multiseat-subscriptions.md)

## Discussion

For a multiseat subscription, the value is the number of seats that the transaction covers. When the group purchaser adds seats partway through a period, the transaction for the addition covers only the added seats; for more information, see [`additionalTransactionReason`](./additionaltransactionreason-swift.property.md). With Apple-hosted invitations, a group member’s transaction has the same value as the group purchaser’s.

## See Also

### Getting purchase details
- [let isUpgraded: Bool](./isupgraded.md)
  A Boolean that indicates whether the user upgraded to another subscription.
- [let ownershipType: Transaction.OwnershipType](./ownershiptype-swift.property.md)
  A value that indicates whether the customer purchased the product or has access to it through Family Sharing, an organization, or a group.
- [Transaction.OwnershipType](./ownershiptype-swift.struct.md)
  Values that indicate whether the customer purchased the product or has access to it through Family Sharing, an organization, or a group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/purchasedquantity)*