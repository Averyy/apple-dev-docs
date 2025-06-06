# recordZoneWithIDWasPurgedBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when CloudKit purges a record zone.

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
var recordZoneWithIDWasPurgedBlock: ((CKRecordZone.ID) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

## See Also

- [var recordZoneWithIDChangedBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidchangedblock.md)
  The closure to execute with a single record zone change.
- [var recordZoneWithIDWasDeletedBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidwasdeletedblock.md)
  The closure to execute when a record zone no longer exists.
- [var recordZoneWithIDWasDeletedDueToUserEncryptedDataResetBlock: ((CKRecordZone.ID) -> Void)?](ckfetchdatabasechangesoperation/recordzonewithidwasdeletedduetouserencrypteddataresetblock.md)
  The closure to execute when a user-invoked account reset deletes a record zone.
- [var changeTokenUpdatedBlock: ((CKServerChangeToken) -> Void)?](ckfetchdatabasechangesoperation/changetokenupdatedblock.md)
  The closure to execute when the change token updates.
- [var fetchDatabaseChangesCompletionBlock: ((CKServerChangeToken?, Bool, (any Error)?) -> Void)?](ckfetchdatabasechangesoperation/fetchdatabasechangescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/recordzonewithidwaspurgedblock)*