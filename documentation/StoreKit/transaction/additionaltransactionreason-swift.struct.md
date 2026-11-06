# Transaction.AdditionalTransactionReason

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Reasons that more than one transaction represents a single subscription period.

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
struct AdditionalTransactionReason
```

## Topics

### Identifying the reason
- [static let seatAddition: Transaction.AdditionalTransactionReason](./additionaltransactionreason-swift.struct/seataddition.md)
  A reason that indicates the group purchaser added seats to a multiseat subscription partway through the period.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting multiseat information
- [let multiSeatInfo: Transaction.MultiSeatInfo?](./multiseatinfo-swift.property.md)
  The seat information for a multiseat subscription transaction.
- [Transaction.MultiSeatInfo](./multiseatinfo-swift.struct.md)
  The invitation model, price tiers, and revoked seats of a multiseat subscription transaction.
- [let additionalTransactionReason: Transaction.AdditionalTransactionReason?](./additionaltransactionreason-swift.property.md)
  The reason that more than one transaction represents the subscription period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/additionaltransactionreason-swift.struct)*