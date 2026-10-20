# CKError.Code

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

The error codes that CloudKit returns.

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
enum Code
```

```c
enum CKErrorCode : NSInteger;
```

## Topics

### Error Codes
- [CKError.Code.accountTemporarilyUnavailable](./code/accounttemporarilyunavailable.md)
  An error that occurs when the user’s iCloud account is temporarily unavailable.
- [CKError.Code.alreadyShared](./code/alreadyshared.md)
  An error that occurs when CloudKit attempts to share a record with an existing share.
- [CKError.Code.assetFileModified](./code/assetfilemodified.md)
  An error that occurs when the system modifies an asset while saving it.
- [CKError.Code.assetFileNotFound](./code/assetfilenotfound.md)
  An error that occurs when the system can’t find the specified asset.
- [CKError.Code.assetNotAvailable](./code/assetnotavailable.md)
  An error that occurs when the system can’t access the specified asset.
- [CKError.Code.badContainer](./code/badcontainer.md)
  An error that occurs when you use an unknown or unauthorized container.
- [CKError.Code.badDatabase](./code/baddatabase.md)
  An error that occurs when the operation can’t complete for the specified database.
- [CKError.Code.batchRequestFailed](./code/batchrequestfailed.md)
  An error that occurs when the system rejects the entire batch of changes.
- [CKError.Code.changeTokenExpired](./code/changetokenexpired.md)
  An error that occurs when the change token expires.
- [CKError.Code.constraintViolation](./code/constraintviolation.md)
  An error that occurs when the server rejects the request because of a unique constraint violation.
- [CKError.Code.incompatibleVersion](./code/incompatibleversion.md)
  An error that occurs when the current app version is older than the oldest allowed version.
- [CKError.Code.internalError](./code/internalerror.md)
  A nonrecoverable error that CloudKit encounters.
- [CKError.Code.invalidArguments](./code/invalidarguments.md)
  An error that occurs when the request contains invalid information.
- [CKError.Code.limitExceeded](./code/limitexceeded.md)
  An error that occurs when a request’s size exceeds the limit.
- [CKError.Code.managedAccountRestricted](./code/managedaccountrestricted.md)
  An error that occurs when CloudKit rejects a request due to a managed-account restriction.
- [CKError.Code.missingEntitlement](./code/missingentitlement.md)
  An error that occurs when the app is missing a required entitlement.
- [CKError.Code.networkFailure](./code/networkfailure.md)
  An error that occurs when a network is available, but CloudKit is inaccessible.
- [CKError.Code.networkUnavailable](./code/networkunavailable.md)
  An error that occurs when the network is unavailable.
- [CKError.Code.notAuthenticated](./code/notauthenticated.md)
  An error that occurs when CloudKit cannot authenticate the user.
- [CKError.Code.operationCancelled](./code/operationcancelled.md)
  An error that occurs when an operation cancels.
- [CKError.Code.partialFailure](./code/partialfailure.md)
  An error that occurs when an operation completes with partial failures.
- [CKError.Code.participantMayNeedVerification](./code/participantmayneedverification.md)
  An error that occurs when the user isn’t a participant of the share.
- [CKError.Code.permissionFailure](./code/permissionfailure.md)
  An error that occurs when the user doesn’t have permission to save or fetch data.
- [CKError.Code.quotaExceeded](./code/quotaexceeded.md)
  An error that occurs when saving a record exceeds the user’s storage quota.
- [CKError.Code.referenceViolation](./code/referenceviolation.md)
  An error that occurs when CloudKit can’t find the target of a reference.
- [CKError.Code.requestRateLimited](./code/requestratelimited.md)
  An error that occurs when CloudKit rate-limits requests.
- [CKError.Code.serverRecordChanged](./code/serverrecordchanged.md)
  An error that occurs when CloudKit rejects a record because the server’s version is different.
- [CKError.Code.serverRejectedRequest](./code/serverrejectedrequest.md)
  An error that occurs when CloudKit rejects the request.
- [CKError.Code.serverResponseLost](./code/serverresponselost.md)
  An error that occurs when CloudKit is unable to maintain the network connection and provide a response.
- [CKError.Code.serviceUnavailable](./code/serviceunavailable.md)
  An error that occurs when CloudKit is unavailable.
- [CKError.Code.tooManyParticipants](./code/toomanyparticipants.md)
  An error that occurs when a share has too many participants.
- [CKError.Code.unknownItem](./code/unknownitem.md)
  An error that occurs when the specified record doesn’t exist.
- [CKError.Code.userDeletedZone](./code/userdeletedzone.md)
  An error that occurs when the user deletes a record zone using the Settings app.
- [CKError.Code.zoneBusy](./code/zonebusy.md)
  An error that occurs when the server is too busy to handle the record zone operation.
- [CKError.Code.zoneNotFound](./code/zonenotfound.md)
  An error that occurs when the specified record zone doesn’t exist.
- [CKError.Code.resultsTruncated](./code/resultstruncated.md)
  An error that occurs when CloudKit truncates a query’s results.
### Enumeration Cases
- [CKError.Code.participantAlreadyInvited](./code/participantalreadyinvited.md)
  The user is already an invited participant on this share. They must accept the existing share invitation before continuing.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [let CKErrorDomain: String](../ckerrordomain.md)
  The error domain for CloudKit errors.
- [struct CKError](../ckerror.md)
  A type that describes a CloudKit error.
- [let CKErrorRetryAfterKey: String](../ckerrorretryafterkey.md)
  The key to retrieve the number of seconds to wait before you retry a request.
- [let CKErrorUserDidResetEncryptedDataKey: String](../ckerroruserdidresetencrypteddatakey.md)
  The key that determines whether CloudKit deletes a record zone because of a user action.
- [let CKPartialErrorsByItemIDKey: String](../ckpartialerrorsbyitemidkey.md)
  The key to retrieve partial errors.
- [Record Changed Error Keys](../record-changed-error-keys.md)
  Constants that represent conflicting records in a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/code)*