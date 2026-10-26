# CKSyncEngineDidFetchRecordZoneChangesEvent

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that provides information about a finished record zone fetch.

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
@interface CKSyncEngineDidFetchRecordZoneChangesEvent : CKSyncEngineEvent
```

## Topics

### Identifying the record zone
- [zoneID](./cksyncenginedidfetchrecordzonechangesevent/zoneid.md)
  The associated record zone’s unique identifier.
### Handling errors
- [error](./cksyncenginedidfetchrecordzonechangesevent/error.md)
  An error that describes the cause of a failed fetch operation.

## Relationships

### Inherits From
- [CKSyncEngineEvent](./cksyncengineevent.md)

## See Also

### Accessing fetch events
- [willFetchChangesEvent](./cksyncengineevent/willfetchchangesevent.md)
  The event downcast to the subclass that represents an imminent database fetch.
- [CKSyncEngineWillFetchChangesEvent](./cksyncenginewillfetchchangesevent.md)
  The sync engine is about to fetch changes from the server.
- [willFetchRecordZoneChangesEvent](./cksyncengineevent/willfetchrecordzonechangesevent.md)
  The event downcast to the subclass that represents an imminent fetch of record zone changes.
- [CKSyncEngineWillFetchRecordZoneChangesEvent](./cksyncenginewillfetchrecordzonechangesevent.md)
  The sync engine finished fetching record zone changes from the server for a specific zone.
- [fetchedDatabaseChangesEvent](./cksyncengineevent/fetcheddatabasechangesevent.md)
  The event downcast to the subclass that represents a set of fetched database changes to process.
- [CKSyncEngineFetchedDatabaseChangesEvent](./cksyncenginefetcheddatabasechangesevent.md)
  An object that provides information about fetched database changes.
- [fetchedRecordZoneChangesEvent](./cksyncengineevent/fetchedrecordzonechangesevent.md)
  The event downcast to the subclass that represents a set of fetched record zone changes to process.
- [CKSyncEngineFetchedRecordZoneChangesEvent](./cksyncenginefetchedrecordzonechangesevent.md)
  An object that provides information about fetched record zone changes.
- [didFetchRecordZoneChangesEvent](./cksyncengineevent/didfetchrecordzonechangesevent.md)
  The event downcast to the subclass that represents a completed record zone fetch.
- [didFetchChangesEvent](./cksyncengineevent/didfetchchangesevent.md)
  The event downcast to the subclass that represents a completed database fetch.
- [CKSyncEngineDidFetchChangesEvent](./cksyncenginedidfetchchangesevent.md)
  The sync engine finished fetching changes from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginedidfetchrecordzonechangesevent)*