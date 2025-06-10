# Transaction.AdvancedCommerceInfo

**Framework**: StoreKit  
**Kind**: struct

Metadata for transactions that use the Advanced Commerce API.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct AdvancedCommerceInfo
```

## Topics

### Structures
- [Transaction.AdvancedCommerceInfo.Item](transaction/advancedcommerceinfo-swift.struct/item.md)
  The developer-defined product that was purchased.
- [Transaction.AdvancedCommerceInfo.Offer](transaction/advancedcommerceinfo-swift.struct/offer.md)
  Information about the offer that was redeemed as part of the purchase.
- [Transaction.AdvancedCommerceInfo.Refund](transaction/advancedcommerceinfo-swift.struct/refund.md)
  Information about refunds that were issued as part of this transaction.
### Instance Properties
- [let description: String?](transaction/advancedcommerceinfo-swift.struct/description.md)
- [let displayName: String?](transaction/advancedcommerceinfo-swift.struct/displayname.md)
- [let estimatedTax: Decimal](transaction/advancedcommerceinfo-swift.struct/estimatedtax.md)
- [let items: [Transaction.AdvancedCommerceInfo.Item]](transaction/advancedcommerceinfo-swift.struct/items.md)
  The items purchased as part of this transaction.
- [let period: SubscriptionPeriod?](transaction/advancedcommerceinfo-swift.struct/period.md)
- [let requestReferenceID: String](transaction/advancedcommerceinfo-swift.struct/requestreferenceid.md)
- [let taxCode: String](transaction/advancedcommerceinfo-swift.struct/taxcode.md)
- [let taxExclusivePrice: Decimal](transaction/advancedcommerceinfo-swift.struct/taxexclusiveprice.md)
- [let taxRate: Decimal](transaction/advancedcommerceinfo-swift.struct/taxrate.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Transaction.OfferType](transaction/offertype-swift.struct.md)
  The types of subscription offers for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct)*