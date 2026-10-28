# removePendingDatabaseChanges:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Removes the specified database changes from the state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
- (void) removePendingDatabaseChanges:(NSArray<CKSyncEnginePendingDatabaseChange *> *) changes;
```

## Discussion

Use this method when you no longer want the sync engine to send certain pending changes.

## Parameters

- `changes`: An array of database changes.

## See Also

### Modifying pending changes
- [- addPendingDatabaseChanges:](./addpendingdatabasechanges_.md)
  Adds the specified database changes to the state.
- [CKSyncEnginePendingZoneDelete](../cksyncenginependingzonedelete.md)
  An object that describes an unsent record zone deletion.
- [CKSyncEnginePendingZoneSave](../cksyncenginependingzonesave.md)
  An object that describes an unsent record zone modification.
- [CKSyncEnginePendingDatabaseChange](../cksyncenginependingdatabasechange.md)
  An object that describes an unsent database modification.
- [- addPendingRecordZoneChanges:](./addpendingrecordzonechanges_.md)
  Adds the specified record zone changes to the state.
- [- removePendingRecordZoneChanges:](./removependingrecordzonechanges_.md)
  Removes the specified record zone changes from the state.
- [CKSyncEnginePendingRecordZoneChange](../cksyncenginependingrecordzonechange.md)
  An object that describes an unsent record modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginestate/removependingdatabasechanges:)*