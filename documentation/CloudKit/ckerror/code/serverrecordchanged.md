# CKError.Code.serverRecordChanged

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

An error that occurs when CloudKit rejects a record because the server’s version is different.

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
case serverRecordChanged
```

```c
CKErrorServerRecordChanged
```

#### Discussion

This error indicates that the server’s version of the record is newer than the local version the client’s trying to save. Your app needs to handle this error, resolve any conflicts in the record, and attempt another save of the record, if necessary.

CloudKit provides your app with three copies of the record in this error’s `userInfo` dictionary to assist with comparing and merging the changes:

- [`CKRecordChangedErrorClientRecordKey`](../../ckrecordchangederrorclientrecordkey.md): The local record that the client’s trying to save.
- [`CKRecordChangedErrorServerRecordKey`](../../ckrecordchangederrorserverrecordkey.md): The record that exists on the server.
- [`CKRecordChangedErrorAncestorRecordKey`](../../ckrecordchangederrorancestorrecordkey.md): The original version of the record.

When a conflict occurs, your app needs to merge all changes into the record for the [`CKRecordChangedErrorServerRecordKey`](../../ckrecordchangederrorserverrecordkey.md) key and attempt a new save using that record. Merging into either of the other two copies of the record results in another conflict error because those records have the old record change tag.

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
- [CKError.Code.managedAccountRestricted](./managedaccountrestricted.md)
  An error that occurs when CloudKit rejects a request due to a managed-account restriction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/code/serverrecordchanged)*