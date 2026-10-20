# alreadyShared

**Framework**: CloudKit  
**Kind**: property  
**Role**: Type Property

An error that occurs when CloudKit attempts to share a record with an existing share.

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
static var alreadyShared: CKError.Code { get }
```

#### Discussion

A record can exist in only a single share at a time. This error means that one of the following conditions exists:

- The record already has an existing share.
- The record has a parent, and its parent has a share.
- The record is a parent, and one of its children has a share.

## See Also

### Getting Error Codes
- [static var accountTemporarilyUnavailable: CKError.Code](./accounttemporarilyunavailable.md)
  An error that occurs when the user’s iCloud account is temporarily unavailable.
- [static var assetFileModified: CKError.Code](./assetfilemodified.md)
  An error that occurs when the system modifies an asset while saving it.
- [static var assetFileNotFound: CKError.Code](./assetfilenotfound.md)
  An error that occurs when the system can’t find the specified asset.
- [static var assetNotAvailable: CKError.Code](./assetnotavailable.md)
  An error that occurs when the system can’t access the specified asset.
- [static var badContainer: CKError.Code](./badcontainer.md)
  An error that occurs when you use an unknown or unauthorized container.
- [static var badDatabase: CKError.Code](./baddatabase.md)
  An error that occurs when the operation can’t complete for the specified database.
- [static var batchRequestFailed: CKError.Code](./batchrequestfailed.md)
  An error that occurs when the system rejects the entire batch of changes.
- [static var changeTokenExpired: CKError.Code](./changetokenexpired.md)
  An error that occurs when the change token expires.
- [static var constraintViolation: CKError.Code](./constraintviolation.md)
  An error that occurs when the server rejects the request because of a unique constraint violation.
- [static var incompatibleVersion: CKError.Code](./incompatibleversion.md)
  An error that occurs when the current app version is older than the oldest allowed version.
- [static var internalError: CKError.Code](./internalerror.md)
  A nonrecoverable error that CloudKit encounters.
- [static var invalidArguments: CKError.Code](./invalidarguments.md)
  An error that occurs when the request contains invalid information.
- [static var limitExceeded: CKError.Code](./limitexceeded.md)
  An error that occurs when a request’s size exceeds the limit.
- [static var managedAccountRestricted: CKError.Code](./managedaccountrestricted.md)
  An error that occurs when CloudKit rejects a request due to a managed-account restriction.
- [static var missingEntitlement: CKError.Code](./missingentitlement.md)
  An error that occurs when the app is missing a required entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/alreadyshared)*