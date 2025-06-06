# fetchDatabaseChangesCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when the operation finishes.

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
var fetchDatabaseChangesCompletionBlock: ((CKServerChangeToken?, Bool, (any Error)?) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- The change token to store and use in subsequent instances of [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md).
- A Boolen value that indicates whether this is the final database change. If [`fetchAllChanges`](ckfetchdatabasechangesoperation/fetchallchanges.md) is [`false`](https://developer.apple.com/documentation/swift/false), it’s the app’s responsibility to create additional instances of [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md) to fetch further changes.
- An error object that contains information about a problem, or `nil` if CloudKit successfully retrieves the database changes.

> **Note**:  The change token and error parameters are mutally exclusive — that is, the closure provides one of them but not both.

 The change token and error parameters are mutally exclusive — that is, the closure provides one of them but not both.

Your app is responsible for saving the change token at the end of the operation and providing it to future uses of [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md). If the server returns a [`CKError.Code.changeTokenExpired`](ckerror/code/changetokenexpired.md) error, the [`previousServerChangeToken`](ckfetchdatabasechangesoperation/previousserverchangetoken.md) value is stale and your app needs to clear its local cache and refetch the database changes, starting with a `nil` change token.

## See Also

- [var recordZoneWithIDChangedBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidchangedblock.md)
  The closure to execute with a single record zone change.
- [var recordZoneWithIDWasDeletedBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidwasdeletedblock.md)
  The closure to execute when a record zone no longer exists.
- [var recordZoneWithIDWasDeletedDueToUserEncryptedDataResetBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidwasdeletedduetouserencrypteddataresetblock.md)
  The closure to execute when a user-invoked account reset deletes a record zone.
- [var recordZoneWithIDWasPurgedBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidwaspurgedblock.md)
  The closure to execute when CloudKit purges a record zone.
- [var changeTokenUpdatedBlock: ((CKServerChangeToken) -> Void)?](ckfetchdatabasechangesoperation/changetokenupdatedblock.md)
  The closure to execute when the change token updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/fetchdatabasechangescompletionblock)*