# Transaction.AdvancedCommerceInfo.Offer

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Information about the offer that was redeemed as part of the purchase.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct Offer
```

## Topics

### Structures
- [Transaction.AdvancedCommerceInfo.Offer.Reason](./offer/reason-swift.struct.md)
  The reasons why subscription offers are applied to the purchase of auto-renewable subscriptions.
### Instance Properties
- [let period: SubscriptionPeriod](./offer/period.md)
  The duration of the offer.
- [let periodCount: Int](./offer/periodcount.md)
  The number of periods the system applies the offer.
- [let price: Decimal](./offer/price.md)
  The discounted price under the offer.
- [let reason: Transaction.AdvancedCommerceInfo.Offer.Reason](./offer/reason-swift.property.md)
  The reason the offer was applied.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Structures
- [Transaction.AdvancedCommerceInfo.Item](./item.md)
  The developer-defined product that was purchased.
- [Transaction.AdvancedCommerceInfo.Refund](./refund.md)
  Information about refunds that were issued as part of this transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/offer)*