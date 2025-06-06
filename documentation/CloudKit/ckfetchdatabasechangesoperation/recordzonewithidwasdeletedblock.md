# recordZoneWithIDWasDeletedBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when a record zone no longer exists.

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
var recordZoneWithIDWasDeletedBlock: ((CKRecordZone.ID) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

## See Also

- [var recordZoneWithIDChangedBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidchangedblock.md)
  The closure to execute with a single record zone change.
- [var recordZoneWithIDWasDeletedDueToUserEncryptedDataResetBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidwasdeletedduetouserencrypteddataresetblock.md)
  The closure to execute when a user-invoked account reset deletes a record zone.
- [var recordZoneWithIDWasPurgedBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidwaspurgedblock.md)
  The closure to execute when CloudKit purges a record zone.
- [var changeTokenUpdatedBlock: ((CKServerChangeToken) -> Void)?](ckfetchdatabasechangesoperation/changetokenupdatedblock.md)
  The closure to execute when the change token updates.
- [var fetchDatabaseChangesCompletionBlock: ((CKServerChangeToken?, Bool, (any Error)?) -> Void)?](ckfetchdatabasechangesoperation/fetchdatabasechangescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/recordzonewithidwasdeletedblock)*