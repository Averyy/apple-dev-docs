# Transaction.RevocationType

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The types of refunds and revocations that apply to transactions.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- tvOS 26.4+
- visionOS 26.4+
- watchOS 26.4+

## Declaration

```swift
struct RevocationType
```

## Topics

### Getting revocation types
- [static let fullRefund: Transaction.RevocationType](./revocationtype-swift.struct/fullrefund.md)
  The transaction was fully refunded.
- [static let proratedRefund: Transaction.RevocationType](./revocationtype-swift.struct/proratedrefund.md)
  The transaction was partially refunded based on consumption.
- [static let familyRevocation: Transaction.RevocationType](./revocationtype-swift.struct/familyrevocation.md)
  The transaction was revoked due to a family sharing revocation.
- [static var assignmentRevocation: Transaction.RevocationType](./revocationtype-swift.struct/assignmentrevocation.md)
  The customer no longer has access through an organization or group.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting revocation status
- [let revocationDate: Date?](./revocationdate.md)
  The date that the App Store refunded or revoked the transaction.
- [let revocationReason: Transaction.RevocationReason?](./revocationreason-swift.property.md)
  The reason that the App Store refunded or revoked the transaction.
- [Transaction.RevocationReason](./revocationreason-swift.struct.md)
  Reasons that describe why the App Store may refund or revoke a transaction.
- [let revocationType: Transaction.RevocationType?](./revocationtype-swift.property.md)
  The type of refund or revocation that applies to the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.struct)*