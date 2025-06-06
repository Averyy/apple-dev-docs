# CKError.Code.accountTemporarilyUnavailable

**Framework**: CloudKit  
**Kind**: case

An error that occurs when the user’s iCloud account is temporarily unavailable.

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
case accountTemporarilyUnavailable
```

#### Discussion

You receive this error when the user’s iCloud account is available, but isn’t ready to support CloudKit operations. Don’t delete any cached data and don’t enqueue any additional CloudKit operations.

Checking the account status after the operation fails, assuming there are no other changes to the account’s status, returns [`CKAccountStatus.temporarilyUnavailable`](ckaccountstatus/temporarilyunavailable.md). Use the [`CKAccountChanged`](https://developer.apple.com/documentation/foundation/nsnotification/name/1399172-ckaccountchanged) notification to listen for future account status changes, and retry the operation after the status becomes [`CKAccountStatus.available`](ckaccountstatus/available.md).

## See Also

- [CKError.Code.alreadyShared](ckerror/code/alreadyshared.md)
  An error that occurs when CloudKit attempts to share a record with an existing share.
- [CKError.Code.assetFileModified](ckerror/code/assetfilemodified.md)
  An error that occurs when the system modifies an asset while saving it.
- [CKError.Code.assetFileNotFound](ckerror/code/assetfilenotfound.md)
  An error that occurs when the system can’t find the specified asset.
- [CKError.Code.assetNotAvailable](ckerror/code/assetnotavailable.md)
  An error that occurs when the system can’t access the specified asset.
- [CKError.Code.badContainer](ckerror/code/badcontainer.md)
  An error that occurs when you use an unknown or unauthorized container.
- [CKError.Code.badDatabase](ckerror/code/baddatabase.md)
  An error that occurs when the operation can’t complete for the specified database.
- [CKError.Code.batchRequestFailed](ckerror/code/batchrequestfailed.md)
  An error that occurs when the system rejects the entire batch of changes.
- [CKError.Code.changeTokenExpired](ckerror/code/changetokenexpired.md)
  An error that occurs when the change token expires.
- [CKError.Code.constraintViolation](ckerror/code/constraintviolation.md)
  An error that occurs when the server rejects the request because of a unique constraint violation.
- [CKError.Code.incompatibleVersion](ckerror/code/incompatibleversion.md)
  An error that occurs when the current app version is older than the oldest allowed version.
- [CKError.Code.internalError](ckerror/code/internalerror.md)
  A nonrecoverable error that CloudKit encounters.
- [CKError.Code.invalidArguments](ckerror/code/invalidarguments.md)
  An error that occurs when the request contains invalid information.
- [CKError.Code.limitExceeded](ckerror/code/limitexceeded.md)
  An error that occurs when a request’s size exceeds the limit.
- [CKError.Code.managedAccountRestricted](ckerror/code/managedaccountrestricted.md)
  An error that occurs when CloudKit rejects a request due to a managed-account restriction.
- [CKError.Code.missingEntitlement](ckerror/code/missingentitlement.md)
  An error that occurs when the app is missing a required entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/code/accounttemporarilyunavailable)*