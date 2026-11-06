# Transaction.MultiSeatInfo

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The invitation model, price tiers, and revoked seats of a multiseat subscription transaction.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
struct MultiSeatInfo
```

## Topics

### Getting the invitation model
- [let invitationManagement: Transaction.MultiSeatInfo.InvitationManagement](./multiseatinfo-swift.struct/invitationmanagement-swift.property.md)
  The invitation model of the multiseat subscription, either Apple-hosted or developer-hosted invitations.
- [Transaction.MultiSeatInfo.InvitationManagement](./multiseatinfo-swift.struct/invitationmanagement-swift.struct.md)
  Values that indicate whether Apple or you host the invitations for a multiseat subscription.
### Getting the price tiers
- [let priceTiers: [Transaction.MultiSeatInfo.PriceTier]](./multiseatinfo-swift.struct/pricetiers.md)
  The price tiers of the transaction’s seats, with the number of seats bought at each price.
- [Transaction.MultiSeatInfo.PriceTier](./multiseatinfo-swift.struct/pricetier.md)
  A per-seat price and the number of seats that the customer bought at that price.
### Getting revoked seats
- [let revokedSeatQuantity: Int?](./multiseatinfo-swift.struct/revokedseatquantity.md)
  The number of seats from this transaction that the App Store revoked.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting multiseat information
- [let multiSeatInfo: Transaction.MultiSeatInfo?](./multiseatinfo-swift.property.md)
  The seat information for a multiseat subscription transaction.
- [let additionalTransactionReason: Transaction.AdditionalTransactionReason?](./additionaltransactionreason-swift.property.md)
  The reason that more than one transaction represents the subscription period.
- [Transaction.AdditionalTransactionReason](./additionaltransactionreason-swift.struct.md)
  Reasons that more than one transaction represents a single subscription period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/multiseatinfo-swift.struct)*