# recordZoneWithIDChangedBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute with a single record zone change.

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
var recordZoneWithIDChangedBlock: ((CKRecordZone.ID) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^recordZoneWithIDChangedBlock)(CKRecordZoneID *zoneID);
```

## Discussion

The closure returns no value and takes the following parameter:

- **`zoneID`**: The ID of the  record zone that contains changes.

## See Also

### Processing the Operation’s Results
- [var recordZoneWithIDWasDeletedBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidwasdeletedblock.md)
  The closure to execute when a record zone no longer exists.
- [var recordZoneWithIDWasDeletedDueToUserEncryptedDataResetBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidwasdeletedduetouserencrypteddataresetblock.md)
  The closure to execute when a user-invoked account reset deletes a record zone.
- [var recordZoneWithIDWasPurgedBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidwaspurgedblock.md)
  The closure to execute when CloudKit purges a record zone.
- [var changeTokenUpdatedBlock: ((CKServerChangeToken) -> Void)?](./changetokenupdatedblock.md)
  The closure to execute when the change token updates.
- [var fetchDatabaseChangesCompletionBlock: ((CKServerChangeToken?, Bool, (any Error)?) -> Void)?](./fetchdatabasechangescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/recordzonewithidchangedblock)*