# CKAccountStatus.restricted

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

The system denies access to the user’s iCloud account.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case restricted
```

```c
CKAccountStatusRestricted
```

#### Discussion

Your app can’t access the user’s iCloud account due to restrictions that Parental Controls or Mobile Device Management impose.

## See Also

### Account Statuses
- [CKAccountStatus.available](./available.md)
  The user’s iCloud account is available.
- [CKAccountStatus.couldNotDetermine](./couldnotdetermine.md)
  CloudKit can’t determine the status of the user’s iCloud account.
- [CKAccountStatus.noAccount](./noaccount.md)
  The device doesn’t have an iCloud account.
- [CKAccountStatus.temporarilyUnavailable](./temporarilyunavailable.md)
  The user’s iCloud account is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckaccountstatus/restricted)*