# recordZoneWithIDWasPurgedBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) void (^recordZoneWithIDWasPurgedBlock)(CKRecordZoneID *zoneID);
```

#### Discussion

The closure returns no value and takes the following parameter:

- **`zoneID`**: The purged record zone’s ID.

## See Also

### Processing the Operation’s Results
- [var recordZoneWithIDChangedBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidchangedblock.md)
  The closure to execute with a single record zone change.
- [var recordZoneWithIDWasDeletedBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidwasdeletedblock.md)
  The closure to execute when a record zone no longer exists.
- [var recordZoneWithIDWasDeletedDueToUserEncryptedDataResetBlock: ((CKRecordZone.ID) -> Void)?](./recordzonewithidwasdeletedduetouserencrypteddataresetblock.md)
  The closure to execute when a user-invoked account reset deletes a record zone.
- [var changeTokenUpdatedBlock: ((CKServerChangeToken) -> Void)?](./changetokenupdatedblock.md)
  The closure to execute when the change token updates.
- [var fetchDatabaseChangesCompletionBlock: ((CKServerChangeToken?, Bool, (any Error)?) -> Void)?](./fetchdatabasechangescompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/recordzonewithidwaspurgedblock)*