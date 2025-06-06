# isUpgraded

**Framework**: StoreKit  
**Kind**: property

A Boolean that indicates whether the user upgraded to another subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let isUpgraded: Bool
```

#### Discussion

If [`isUpgraded`](transaction/isupgraded.md) is `true`, the user has upgraded the subscription represented by this transaction to another subscription. This value appears in the transaction only when the value is `true`. To determine the service that the customer is entitled to, look for another transaction that has a subscription with a higher level of service.

## See Also

- [let ownershipType: Transaction.OwnershipType](transaction/ownershiptype-swift.property.md)
  A value that indicates whether the transaction was purchased by the user, or is made available to them through Family Sharing.
- [Transaction.OwnershipType](transaction/ownershiptype-swift.struct.md)
  The types the system uses to describe whether the user purchased the product or it’s available to them through Family Sharing.
- [let purchasedQuantity: Int](transaction/purchasedquantity.md)
  The number of consumable products purchased.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/isupgraded)*