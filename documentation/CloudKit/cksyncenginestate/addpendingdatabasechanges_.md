# addPendingDatabaseChanges:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Adds the specified database changes to the state.

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
- (void) addPendingDatabaseChanges:(NSArray<CKSyncEnginePendingDatabaseChange *> *) changes;
```

#### Discussion

Use this method to enable the sync engine to manage your pending database changes. For example, when someone makes a change that your app needs to send to the server, use this method to record the change. If there are no scheduled sync operations when you invoke this method, the sync engine automatically schedules one to send the changes. After the engine sends those changes, it notifies your app’s sync delegate with an event of type [`CKSyncEngineSentDatabaseChangesEvent`](../cksyncenginesentdatabasechangesevent.md).

The sync engine maintains a consistent collection of tracked pending changes, deduplicating them as necessary. The engine removes changes from the list as it sends them, but retains any that fail due to a recoverable error, such as a network issue, or exceeding the rate limit.

> **Note**: The order in which you apply database changes is important.
>
> For example:
>
> - If you add a `CKSyncEnginePendingDatabaseChange` with type `CKSyncEnginePendingDatabaseChangeTypeSaveZone` for zoneA then another with type `CKSyncEnginePendingDatabaseChangeTypeDeleteZone`, the sync engine discards the save and sends only the delete change.
> - If you add a `CKSyncEnginePendingDatabaseChange` with type `CKSyncEnginePendingDatabaseChangeTypeDeleteZone` for zoneA then another with type `CKSyncEnginePendingDatabaseChangeTypeSaveZone`, the sync engine discards the delete and sends only the save change.

## Parameters

- `changes`: An array of database changes.

## See Also

### Modifying pending changes
- [- removePendingDatabaseChanges:](./removependingdatabasechanges_.md)
  Removes the specified database changes from the state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginestate/addpendingdatabasechanges:)*