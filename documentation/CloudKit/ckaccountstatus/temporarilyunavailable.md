# CKAccountStatus.temporarilyUnavailable

**Framework**: CloudKit  
**Kind**: case

The user’s iCloud account is temporarily unavailable.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case temporarilyUnavailable
```

#### Discussion

You receive this account status when the user’s iCloud account is available, but isn’t ready to support CloudKit operations. Don’t delete any cached data and don’t enqueue any CloudKit operations after receipt of this account status. Instead, use the [`CKAccountChanged`](https://developer.apple.com/documentation/foundation/nsnotification/name/1399172-ckaccountchanged) notification to listen for when the status changes to [`CKAccountStatus.available`](ckaccountstatus/available.md).

## See Also

- [CKAccountStatus.available](ckaccountstatus/available.md)
  The user’s iCloud account is available.
- [CKAccountStatus.couldNotDetermine](ckaccountstatus/couldnotdetermine.md)
  CloudKit can’t determine the status of the user’s iCloud account.
- [CKAccountStatus.noAccount](ckaccountstatus/noaccount.md)
  The device doesn’t have an iCloud account.
- [CKAccountStatus.restricted](ckaccountstatus/restricted.md)
  The system denies access to the user’s iCloud account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckaccountstatus/temporarilyunavailable)*