# Transaction.RevocationReason

**Framework**: StoreKit  
**Kind**: struct

Reasons that describe why the App Store may refund a transaction or revoke it from Family Sharing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct RevocationReason
```

## Topics

### Revocation reasons
- [static let developerIssue: Transaction.RevocationReason](transaction/revocationreason-swift.struct/developerissue.md)
  The value that indicates a customer canceled the transaction due to an actual or perceived issue within your app.
- [static let other: Transaction.RevocationReason](transaction/revocationreason-swift.struct/other.md)
  The value that indicates a customer canceled the transaction for other reasons.
### Getting a localized description
- [var localizedDescription: String](transaction/revocationreason-swift.struct/localizeddescription.md)
  The localized text that describes the revocation reason.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let revocationDate: Date?](transaction/revocationdate.md)
  The date that the App Store refunded the transaction or revoked it from Family Sharing.
- [let revocationReason: Transaction.RevocationReason?](transaction/revocationreason-swift.property.md)
  The reason that the App Store refunded the transaction or revoked it from Family Sharing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/revocationreason-swift.struct)*