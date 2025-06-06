# CKAccountStatus.restricted

**Framework**: CloudKit  
**Kind**: case

The system denies access to the user’s iCloud account.

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
case restricted
```

#### Discussion

Your app can’t access the user’s iCloud account due to restrictions that Parental Controls or Mobile Device Management impose.

## See Also

- [CKAccountStatus.available](ckaccountstatus/available.md)
  The user’s iCloud account is available.
- [CKAccountStatus.couldNotDetermine](ckaccountstatus/couldnotdetermine.md)
  CloudKit can’t determine the status of the user’s iCloud account.
- [CKAccountStatus.noAccount](ckaccountstatus/noaccount.md)
  The device doesn’t have an iCloud account.
- [CKAccountStatus.temporarilyUnavailable](ckaccountstatus/temporarilyunavailable.md)
  The user’s iCloud account is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckaccountstatus/restricted)*