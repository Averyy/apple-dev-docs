# changeTokenUpdatedBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when the change token updates.

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
var changeTokenUpdatedBlock: ((CKServerChangeToken) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^changeTokenUpdatedBlock)(CKServerChangeToken *serverChangeToken);
```

## Discussion

The closure executes periodically, and provides a new change token so that you don’t need to refetch previously fetched record zone changes in a subsequent operation.

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
- [var fetchDatabaseChangesCompletionBlock: ((CKServerChangeToken?, Bool, (any Error)?) -> Void)?](./fetchdatabasechangescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/changetokenupdatedblock)*