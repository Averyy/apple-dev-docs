# CKError

**Framework**: CloudKit  
**Kind**: struct

A type that describes a CloudKit error.

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
struct CKError
```

## Mentions

- [Designing and Creating a CloudKit Database](designing-and-creating-a-cloudkit-database.md)

#### Overview

CloudKit provides operations that faciliate moving data between your app and iCloud. There are also convenience methods in [`CKContainer`](ckcontainer.md) and [`CKDatabase`](ckdatabase.md) that provide similar functionality. If an operation or method fails to complete its task, CloudKit provides detailed error information that you can use to recover. A failure might be due to network or server conditions, or because of conflicts between local and remote data. For a list of possible reasons, see [`CKError.Code`](ckerror/code.md).

If you receive an error, cast it to an instance of `CKError` to access additional information that CloudKit provides. For example, if the error code is [`requestRateLimited`](ckerror/requestratelimited.md), you can use the [`retryAfterSeconds`](ckerror/retryafterseconds.md) property to determine how long you must wait before you retry the operation or method.

Batch operations, such as [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md), can complete with a [`partialFailure`](ckerror/partialfailure.md) error. This means only a subset of the operation’s changes succeed. Use the [`partialErrorsByItemID`](ckerror/partialerrorsbyitemid.md) property to access a dictionary that maps items that CloudKit can’t process to errors that describe those failures. You can then handle each error independently.

If you attempt to save a record and the server’s version of that record is newer, CloudKit returns a [`serverRecordChanged`](ckerror/serverrecordchanged.md) error. Use the [`ancestorRecord`](ckerror/ancestorrecord.md), [`clientRecord`](ckerror/clientrecord.md), and [`serverRecord`](ckerror/serverrecord.md) properties to resolve the conflict. Make sure you merge any changes into `serverRecord` because that version contains the most recent change tag.

## Topics

### Getting Error Codes
- [static var accountTemporarilyUnavailable: CKError.Code](ckerror/accounttemporarilyunavailable.md)
  An error that occurs when the user’s iCloud account is temporarily unavailable.
- [static var alreadyShared: CKError.Code](ckerror/alreadyshared.md)
  An error that occurs when CloudKit attempts to share a record with an existing share.
- [static var assetFileModified: CKError.Code](ckerror/assetfilemodified.md)
  An error that occurs when the system modifies an asset while saving it.
- [static var assetFileNotFound: CKError.Code](ckerror/assetfilenotfound.md)
  An error that occurs when the system can’t find the specified asset.
- [static var assetNotAvailable: CKError.Code](ckerror/assetnotavailable.md)
  An error that occurs when the system can’t access the specified asset.
- [static var badContainer: CKError.Code](ckerror/badcontainer.md)
  An error that occurs when you use an unknown or unauthorized container.
- [static var badDatabase: CKError.Code](ckerror/baddatabase.md)
  An error that occurs when the operation can’t complete for the specified database.
- [static var batchRequestFailed: CKError.Code](ckerror/batchrequestfailed.md)
  An error that occurs when the system rejects the entire batch of changes.
- [static var changeTokenExpired: CKError.Code](ckerror/changetokenexpired.md)
  An error that occurs when the change token expires.
- [static var constraintViolation: CKError.Code](ckerror/constraintviolation.md)
  An error that occurs when the server rejects the request because of a unique constraint violation.
- [static var incompatibleVersion: CKError.Code](ckerror/incompatibleversion.md)
  An error that occurs when the current app version is older than the oldest allowed version.
- [static var internalError: CKError.Code](ckerror/internalerror.md)
  A nonrecoverable error that CloudKit encounters.
- [static var invalidArguments: CKError.Code](ckerror/invalidarguments.md)
  An error that occurs when the request contains invalid information.
- [static var limitExceeded: CKError.Code](ckerror/limitexceeded.md)
  An error that occurs when a request’s size exceeds the limit.
- [static var managedAccountRestricted: CKError.Code](ckerror/managedaccountrestricted.md)
  An error that occurs when CloudKit rejects a request due to a managed-account restriction.
- [static var missingEntitlement: CKError.Code](ckerror/missingentitlement.md)
  An error that occurs when the app is missing a required entitlement.
- [static var networkFailure: CKError.Code](ckerror/networkfailure.md)
  An error that occurs when a network is available, but CloudKit is inaccessible.
- [static var networkUnavailable: CKError.Code](ckerror/networkunavailable.md)
  An error that occurs when the network is unavailable.
- [static var notAuthenticated: CKError.Code](ckerror/notauthenticated.md)
  An error that occurs when the user is unauthenticated.
- [static var operationCancelled: CKError.Code](ckerror/operationcancelled.md)
  An error that occurs when an operation cancels.
- [static var partialFailure: CKError.Code](ckerror/partialfailure.md)
  An error that occurs when an operation completes with partial failures.
- [static var participantMayNeedVerification: CKError.Code](ckerror/participantmayneedverification.md)
  An error that occurs when the user isn’t a participant of the share.
- [static var permissionFailure: CKError.Code](ckerror/permissionfailure.md)
  An error that occurs when the user doesn’t have permission to save or fetch data.
- [static var quotaExceeded: CKError.Code](ckerror/quotaexceeded.md)
  An error that occurs when saving a record exceeds the user’s storage quota.
- [static var referenceViolation: CKError.Code](ckerror/referenceviolation.md)
  An error that occurs when CloudKit can’t find the target of a reference.
- [static var requestRateLimited: CKError.Code](ckerror/requestratelimited.md)
  An error that occurs when CloudKit rate-limits requests.
- [static var serverRecordChanged: CKError.Code](ckerror/serverrecordchanged.md)
  An error that occurs when CloudKit rejects a record because the server’s version is different.
- [static var serverRejectedRequest: CKError.Code](ckerror/serverrejectedrequest.md)
  An error that occurs when CloudKit rejects the request.
- [static var serverResponseLost: CKError.Code](ckerror/serverresponselost.md)
  An error that occurs when CloudKit is unable to maintain the network connection and provide a response.
- [static var serviceUnavailable: CKError.Code](ckerror/serviceunavailable.md)
  An error that occurs when CloudKit is unavailable.
- [static var tooManyParticipants: CKError.Code](ckerror/toomanyparticipants.md)
  An error that occurs when a share has too many participants.
- [static var unknownItem: CKError.Code](ckerror/unknownitem.md)
  An error that occurs when the specified record doesn’t exist.
- [static var userDeletedZone: CKError.Code](ckerror/userdeletedzone.md)
  An error that occurs when the user deletes a record zone using the Settings app.
- [static var zoneBusy: CKError.Code](ckerror/zonebusy.md)
  An error that occurs when the server is too busy to handle the record zone operation.
- [static var zoneNotFound: CKError.Code](ckerror/zonenotfound.md)
  An error that occurs when the specified record zone doesn’t exist.
- [static var resultsTruncated: CKError.Code](ckerror/resultstruncated.md)
  An error that occurs when CloudKit truncates a query’s results.
- [CKError.Code](ckerror/code.md)
  The error codes that CloudKit returns.
### Getting Partial Errors
- [var partialErrorsByItemID: [AnyHashable : any Error]?](ckerror/partialerrorsbyitemid.md)
  The dictionary that contains errors that relate to individual record operations.
### Getting Conflicted Records
- [var ancestorRecord: CKRecord?](ckerror/ancestorrecord.md)
  The original version of the record.
- [var clientRecord: CKRecord?](ckerror/clientrecord.md)
  The local version of the record that includes any changes.
- [var serverRecord: CKRecord?](ckerror/serverrecord.md)
  The server’s version of the record.
### Getting Retry Information
- [var retryAfterSeconds: Double?](ckerror/retryafterseconds.md)
  The number of seconds to wait before you retry the request.
### Type Properties
- [static var errorDomain: String](ckerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let CKErrorDomain: String](ckerrordomain.md)
  The error domain for CloudKit errors.
- [CKError.Code](ckerror/code.md)
  The error codes that CloudKit returns.
- [let CKErrorRetryAfterKey: String](ckerrorretryafterkey.md)
  The key to retrieve the number of seconds to wait before you retry a request.
- [let CKErrorUserDidResetEncryptedDataKey: String](ckerroruserdidresetencrypteddatakey.md)
  The key that determines whether CloudKit deletes a record zone because of a user action.
- [let CKPartialErrorsByItemIDKey: String](ckpartialerrorsbyitemidkey.md)
  The key to retrieve partial errors.
- [Record Changed Error Keys](record-changed-error-keys.md)
  Constants that represent conflicting records in a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror)*