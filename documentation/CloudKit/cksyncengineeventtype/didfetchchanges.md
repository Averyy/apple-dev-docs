# CKSyncEngineEventType.didFetchChanges

**Framework**: CloudKit  
**Kind**: case

An event that indicates the database fetch is done.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
case didFetchChanges
```

## See Also

- [CKSyncEngineEventType.stateUpdate](cksyncengineeventtype/stateupdate.md)
  An event indicating an update to the sync engine’s state.
- [CKSyncEngineEventType.accountChange](cksyncengineeventtype/accountchange.md)
  An event indicating a change to the device’s iCloud account.
- [CKSyncEngineEventType.fetchedDatabaseChanges](cksyncengineeventtype/fetcheddatabasechanges.md)
  An event indicating there are fetched database changes to process.
- [CKSyncEngineEventType.fetchedRecordZoneChanges](cksyncengineeventtype/fetchedrecordzonechanges.md)
  An event indicating there are fetched record zone changes to process.
- [CKSyncEngineEventType.sentDatabaseChanges](cksyncengineeventtype/sentdatabasechanges.md)
  An event indicating a sent batch of database changes.
- [CKSyncEngineEventType.sentRecordZoneChanges](cksyncengineeventtype/sentrecordzonechanges.md)
  An event indicating a sent batch of record zone changes.
- [CKSyncEngineEventType.willFetchChanges](cksyncengineeventtype/willfetchchanges.md)
  An event indicating an imminent database fetch.
- [CKSyncEngineEventType.willFetchRecordZoneChanges](cksyncengineeventtype/willfetchrecordzonechanges.md)
  An event indicating an imminent fetch of changes in a record zone.
- [CKSyncEngineEventType.didFetchRecordZoneChanges](cksyncengineeventtype/didfetchrecordzonechanges.md)
  An event that indicates the record zone fetch is done.
- [CKSyncEngineEventType.willSendChanges](cksyncengineeventtype/willsendchanges.md)
  An event indicating an imminent send of local changes.
- [CKSyncEngineEventType.didSendChanges](cksyncengineeventtype/didsendchanges.md)
  An event that indicates a finished send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineeventtype/didfetchchanges)*