# serverResponseLost

**Framework**: CloudKit  
**Kind**: property

An error that occurs when CloudKit is unable to maintain the network connection and provide a response.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var serverResponseLost: CKError.Code { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckerror/serverresponselost)*