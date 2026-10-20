# CKError.Code.managedAccountRestricted

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

An error that occurs when CloudKit rejects a request due to a managed-account restriction.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
case managedAccountRestricted
```

```c
CKErrorManagedAccountRestricted
```

#### Discussion

The system restricts CloudKit access for this account. This is a nonrecoverable error.

## See Also

### Error Codes
- [CKError.Code.accountTemporarilyUnavailable](./accounttemporarilyunavailable.md)
  An error that occurs when the user’s iCloud account is temporarily unavailable.
- [CKError.Code.alreadyShared](./alreadyshared.md)
  An error that occurs when CloudKit attempts to share a record with an existing share.
- [CKError.Code.assetFileModified](./assetfilemodified.md)
  An error that occurs when the system modifies an asset while saving it.
- [CKError.Code.assetFileNotFound](./assetfilenotfound.md)
  An error that occurs when the system can’t find the specified asset.
- [CKError.Code.assetNotAvailable](./assetnotavailable.md)
  An error that occurs when the system can’t access the specified asset.
- [CKError.Code.badContainer](./badcontainer.md)
  An error that occurs when you use an unknown or unauthorized container.
- [CKError.Code.badDatabase](./baddatabase.md)
  An error that occurs when the operation can’t complete for the specified database.
- [CKError.Code.batchRequestFailed](./batchrequestfailed.md)
  An error that occurs when the system rejects the entire batch of changes.
- [CKError.Code.changeTokenExpired](./changetokenexpired.md)
  An error that occurs when the change token expires.
- [CKError.Code.constraintViolation](./constraintviolation.md)
  An error that occurs when the server rejects the request because of a unique constraint violation.
- [CKError.Code.incompatibleVersion](./incompatibleversion.md)
  An error that occurs when the current app version is older than the oldest allowed version.
- [CKError.Code.internalError](./internalerror.md)
  A nonrecoverable error that CloudKit encounters.
- [CKError.Code.invalidArguments](./invalidarguments.md)
  An error that occurs when the request contains invalid information.
- [CKError.Code.limitExceeded](./limitexceeded.md)
  An error that occurs when a request’s size exceeds the limit.
- [CKError.Code.missingEntitlement](./missingentitlement.md)
  An error that occurs when the app is missing a required entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/code/managedaccountrestricted)*