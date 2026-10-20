# CKError.Code.batchRequestFailed

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

An error that occurs when the system rejects the entire batch of changes.

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
case batchRequestFailed
```

```c
CKErrorBatchRequestFailed
```

#### Discussion

This error occurs when an operation attempts to save multiple items in a custom zone, but one of those items encounters an error. Because custom zones are atomic, the entire batch fails. The items that cause the problem have their own errors, and all other items in the batch have a [`CKError.Code.batchRequestFailed`](./batchrequestfailed.md) error to indicate that the system can’t save them.

This error indicates that the system can’t process the associated item due to an error in another item in the operation. Check the other per-item errors under [`CKPartialErrorsByItemIDKey`](../../ckpartialerrorsbyitemidkey.md) for any that aren’t [`CKError.Code.batchRequestFailed`](./batchrequestfailed.md) errors. Handle those errors, and then retry all items in the operation.

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
- [CKError.Code.managedAccountRestricted](./managedaccountrestricted.md)
  An error that occurs when CloudKit rejects a request due to a managed-account restriction.
- [CKError.Code.missingEntitlement](./missingentitlement.md)
  An error that occurs when the app is missing a required entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/code/batchrequestfailed)*