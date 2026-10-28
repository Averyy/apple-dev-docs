# CKSyncEngineWillFetchRecordZoneChangesEvent

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

The sync engine finished fetching record zone changes from the server for a specific zone.

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
@interface CKSyncEngineWillFetchRecordZoneChangesEvent : CKSyncEngineEvent
```

## Overview

This might be a good signal to perform any post-processing tasks on a per-zone basis if necessary.

You should receive one [`CKSyncEngineDidFetchRecordZoneChangesEvent`](./cksyncenginedidfetchrecordzonechangesevent.md) for each `CKSyncEngineWillFetchRecordZoneChangesEvent`.

## Topics

### Identifying the record zone
- [zoneID](./cksyncenginewillfetchrecordzonechangesevent/zoneid.md)
  The associated record zone’s unique identifier.

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
- [CKSyncEngineDidFetchRecordZoneChangesEvent](./cksyncenginedidfetchrecordzonechangesevent.md)
  An object that provides information about a finished record zone fetch.
- [didFetchChangesEvent](./cksyncengineevent/didfetchchangesevent.md)
  The event downcast to the subclass that represents a completed database fetch.
- [CKSyncEngineDidFetchChangesEvent](./cksyncenginedidfetchchangesevent.md)
  The sync engine finished fetching changes from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginewillfetchrecordzonechangesevent)*