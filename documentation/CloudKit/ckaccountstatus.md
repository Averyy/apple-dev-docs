# CKAccountStatus

**Framework**: CloudKit  
**Kind**: enum

Constants that indicate the availability of the user’s iCloud account.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum CKAccountStatus
```

## Topics

### Account Statuses
- [CKAccountStatus.available](ckaccountstatus/available.md)
  The user’s iCloud account is available.
- [CKAccountStatus.couldNotDetermine](ckaccountstatus/couldnotdetermine.md)
  CloudKit can’t determine the status of the user’s iCloud account.
- [CKAccountStatus.noAccount](ckaccountstatus/noaccount.md)
  The device doesn’t have an iCloud account.
- [CKAccountStatus.restricted](ckaccountstatus/restricted.md)
  The system denies access to the user’s iCloud account.
- [CKAccountStatus.temporarilyUnavailable](ckaccountstatus/temporarilyunavailable.md)
  The user’s iCloud account is temporarily unavailable.
### Initializers
- [init?(rawValue: Int)](ckaccountstatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func accountStatus(completionHandler: (CKAccountStatus, (any Error)?) -> Void)](ckcontainer/accountstatus(completionhandler:).md)
  Determines whether the system can access the user’s iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckaccountstatus)*