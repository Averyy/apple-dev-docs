# fullRefund

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

The transaction was fully refunded.

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
static let fullRefund: Transaction.RevocationType
```

## See Also

### Getting revocation types
- [static let proratedRefund: Transaction.RevocationType](./proratedrefund.md)
  The transaction was partially refunded based on consumption.
- [static let familyRevocation: Transaction.RevocationType](./familyrevocation.md)
  The transaction was revoked due to a family sharing revocation.
- [static var assignmentRevocation: Transaction.RevocationType](./assignmentrevocation.md)
  The customer no longer has access through an organization or group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.struct/fullrefund)*