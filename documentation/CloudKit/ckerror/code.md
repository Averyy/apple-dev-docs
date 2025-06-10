# CKError.Code

**Framework**: CloudKit  
**Kind**: enum

The error codes that CloudKit returns.

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
enum Code
```

## Topics

### Error Codes
- [CKError.Code.accountTemporarilyUnavailable](ckerror/code/accounttemporarilyunavailable.md)
  An error that occurs when the user’s iCloud account is temporarily unavailable.
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
- [CKError.Code.networkFailure](ckerror/code/networkfailure.md)
  An error that occurs when a network is available, but CloudKit is inaccessible.
- [CKError.Code.networkUnavailable](ckerror/code/networkunavailable.md)
  An error that occurs when the network is unavailable.
- [CKError.Code.notAuthenticated](ckerror/code/notauthenticated.md)
  An error that occurs when the user is unauthenticated.
- [CKError.Code.operationCancelled](ckerror/code/operationcancelled.md)
  An error that occurs when an operation cancels.
- [CKError.Code.partialFailure](ckerror/code/partialfailure.md)
  An error that occurs when an operation completes with partial failures.
- [CKError.Code.participantMayNeedVerification](ckerror/code/participantmayneedverification.md)
  An error that occurs when the user isn’t a participant of the share.
- [CKError.Code.permissionFailure](ckerror/code/permissionfailure.md)
  An error that occurs when the user doesn’t have permission to save or fetch data.
- [CKError.Code.quotaExceeded](ckerror/code/quotaexceeded.md)
  An error that occurs when saving a record exceeds the user’s storage quota.
- [CKError.Code.referenceViolation](ckerror/code/referenceviolation.md)
  An error that occurs when CloudKit can’t find the target of a reference.
- [CKError.Code.requestRateLimited](ckerror/code/requestratelimited.md)
  An error that occurs when CloudKit rate-limits requests.
- [CKError.Code.serverRecordChanged](ckerror/code/serverrecordchanged.md)
  An error that occurs when CloudKit rejects a record because the server’s version is different.
- [CKError.Code.serverRejectedRequest](ckerror/code/serverrejectedrequest.md)
  An error that occurs when CloudKit rejects the request.
- [CKError.Code.serverResponseLost](ckerror/code/serverresponselost.md)
  An error that occurs when CloudKit is unable to maintain the network connection and provide a response.
- [CKError.Code.serviceUnavailable](ckerror/code/serviceunavailable.md)
  An error that occurs when CloudKit is unavailable.
- [CKError.Code.tooManyParticipants](ckerror/code/toomanyparticipants.md)
  An error that occurs when a share has too many participants.
- [CKError.Code.unknownItem](ckerror/code/unknownitem.md)
  An error that occurs when the specified record doesn’t exist.
- [CKError.Code.userDeletedZone](ckerror/code/userdeletedzone.md)
  An error that occurs when the user deletes a record zone using the Settings app.
- [CKError.Code.zoneBusy](ckerror/code/zonebusy.md)
  An error that occurs when the server is too busy to handle the record zone operation.
- [CKError.Code.zoneNotFound](ckerror/code/zonenotfound.md)
  An error that occurs when the specified record zone doesn’t exist.
- [CKError.Code.resultsTruncated](ckerror/code/resultstruncated.md)
  An error that occurs when CloudKit truncates a query’s results.
### Enumeration Cases
- [CKError.Code.participantAlreadyInvited](ckerror/code/participantalreadyinvited.md)
  The user is already an invited participant on this share. They must accept the existing share invitation before continuing.
### Initializers
- [init?(rawValue: Int)](ckerror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let CKErrorDomain: String](ckerrordomain.md)
  The error domain for CloudKit errors.
- [struct CKError](ckerror.md)
  A type that describes a CloudKit error.
- [let CKErrorRetryAfterKey: String](ckerrorretryafterkey.md)
  The key to retrieve the number of seconds to wait before you retry a request.
- [let CKErrorUserDidResetEncryptedDataKey: String](ckerroruserdidresetencrypteddatakey.md)
  The key that determines whether CloudKit deletes a record zone because of a user action.
- [let CKPartialErrorsByItemIDKey: String](ckpartialerrorsbyitemidkey.md)
  The key to retrieve partial errors.
- [Record Changed Error Keys](record-changed-error-keys.md)
  Constants that represent conflicting records in a save operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/code)*