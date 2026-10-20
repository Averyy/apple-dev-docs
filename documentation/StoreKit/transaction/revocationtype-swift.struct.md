# Transaction.RevocationType

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

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

### Type Properties
- [static var assignmentRevocation: Transaction.RevocationType](./revocationtype-swift.struct/assignmentrevocation.md)
  The transaction was revoked by the organization administrator.
- [static let familyRevocation: Transaction.RevocationType](./revocationtype-swift.struct/familyrevocation.md)
  The transaction was revoked due to a family sharing revocation.
- [static let fullRefund: Transaction.RevocationType](./revocationtype-swift.struct/fullrefund.md)
  The transaction was fully refunded.
- [static let proratedRefund: Transaction.RevocationType](./revocationtype-swift.struct/proratedrefund.md)
  The transaction was partially refunded based on consumption.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.struct)*