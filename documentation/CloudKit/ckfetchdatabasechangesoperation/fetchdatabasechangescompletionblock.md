# fetchDatabaseChangesCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when the operation finishes.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.12+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: Use fetchDatabaseChangesResultBlock instead

## Declaration

```swift
var fetchDatabaseChangesCompletionBlock: ((CKServerChangeToken?, Bool, (any Error)?) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^fetchDatabaseChangesCompletionBlock)(CKServerChangeToken *serverChangeToken, BOOL moreComing, NSError *operationError);
```

#### Discussion

The closure returns no value and takes the following parameters:

- The change token to store and use in subsequent instances of [`CKFetchDatabaseChangesOperation`](../ckfetchdatabasechangesoperation.md).
- A Boolean value that indicates whether this is the final database change. If [`fetchAllChanges`](./fetchallchanges.md) is [`false`](../../Swift/false.md), it’s the app’s responsibility to create additional instances of [`CKFetchDatabaseChangesOperation`](../ckfetchdatabasechangesoperation.md) to fetch further changes.
- An error object that contains information about a problem, or `nil` if CloudKit successfully retrieves the database changes.

> **Note**: The change token and error parameters are mutually exclusive — that is, the closure provides one of them but not both.

Your app is responsible for saving the change token at the end of the operation and providing it to future uses of [`CKFetchDatabaseChangesOperation`](../ckfetchdatabasechangesoperation.md). If the server returns a [`CKError.Code.changeTokenExpired`](../ckerror/code/changetokenexpired.md) error, the [`previousServerChangeToken`](./previousserverchangetoken.md) value is stale and your app needs to clear its local cache and refetch the database changes, starting with a `nil` change token.

## See Also

### Processing the Operation’s Results
- [var recordZoneWithIDChangedBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidchangedblock.md)
  The closure to execute with a single record zone change.
- [var recordZoneWithIDWasDeletedBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidwasdeletedblock.md)
  The closure to execute when a record zone no longer exists.
- [var recordZoneWithIDWasDeletedDueToUserEncryptedDataResetBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidwasdeletedduetouserencrypteddataresetblock.md)
  The closure to execute when a user-invoked account reset deletes a record zone.
- [var recordZoneWithIDWasPurgedBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidwaspurgedblock.md)
  The closure to execute when CloudKit purges a record zone.
- [var changeTokenUpdatedBlock: ((CKServerChangeToken) -> Void)?](./changetokenupdatedblock.md)
  The closure to execute when the change token updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/fetchdatabasechangescompletionblock)*