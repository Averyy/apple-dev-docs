# Transaction.AdvancedCommerceInfo.Refund

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Information about refunds that were issued as part of this transaction.

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
struct Refund
```

## Topics

### Structures
- [Transaction.AdvancedCommerceInfo.Refund.Reason](./refund/reason-swift.struct.md)
  The reason for the refund.
- [Transaction.AdvancedCommerceInfo.Refund.RefundType](./refund/refundtype.md)
  The type of refund.
### Instance Properties
- [let amount: Decimal](./refund/amount.md)
  The amount of the refund.
- [let date: Date](./refund/date.md)
  The date the refund was granted.
- [let reason: Transaction.AdvancedCommerceInfo.Refund.Reason](./refund/reason-swift.property.md)
  The reason for the refund.
- [let type: Transaction.AdvancedCommerceInfo.Refund.RefundType](./refund/type.md)
  The type of the refund.

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
- [Transaction.AdvancedCommerceInfo.Offer](./offer.md)
  Information about the offer that was redeemed as part of the purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund)*