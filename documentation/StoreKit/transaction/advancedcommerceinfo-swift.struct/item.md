# Transaction.AdvancedCommerceInfo.Item

**Framework**: StoreKit  
**Kind**: struct

The developer-defined product that was purchased.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct Item
```

## Topics

### Structures
- [Transaction.AdvancedCommerceInfo.Item.Details](transaction/advancedcommerceinfo-swift.struct/item/details-swift.struct.md)
  The item details.
### Instance Properties
- [let details: Transaction.AdvancedCommerceInfo.Item.Details](transaction/advancedcommerceinfo-swift.struct/item/details-swift.property.md)
  The item’s details.
- [let refunds: [Transaction.AdvancedCommerceInfo.Refund]?](transaction/advancedcommerceinfo-swift.struct/item/refunds.md)
  The list of refunds that were issued as part of this transaction.
- [let revocationDate: Date?](transaction/advancedcommerceinfo-swift.struct/item/revocationdate.md)
  The date access to this item was revoked.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Transaction.AdvancedCommerceInfo.Offer](transaction/advancedcommerceinfo-swift.struct/offer.md)
  Information about the offer that was redeemed as part of the purchase.
- [Transaction.AdvancedCommerceInfo.Refund](transaction/advancedcommerceinfo-swift.struct/refund.md)
  Information about refunds that were issued as part of this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/item)*