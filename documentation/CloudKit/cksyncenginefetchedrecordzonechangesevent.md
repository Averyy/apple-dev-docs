# CKSyncEngineFetchedRecordZoneChangesEvent

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that provides information about fetched record zone changes.

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
@interface CKSyncEngineFetchedRecordZoneChangesEvent : CKSyncEngineEvent
```

## Overview

> **Note**: Although CloudKit doesn’t guarantee the order of fetched database changes, the typical order for both deletions and modifications is oldest to newest.

## Topics

### Accessing changes
- [deletions](./cksyncenginefetchedrecordzonechangesevent/deletions.md)
  The fetched record deletions.
- [CKSyncEngineFetchedRecordDeletion](./cksyncenginefetchedrecorddeletion.md)
  An object that describes the deletion of an individual record.
- [modifications](./cksyncenginefetchedrecordzonechangesevent/modifications.md)
  The fetched record modifications.

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
- [didFetchRecordZoneChangesEvent](./cksyncengineevent/didfetchrecordzonechangesevent.md)
  The event downcast to the subclass that represents a completed record zone fetch.
- [CKSyncEngineDidFetchRecordZoneChangesEvent](./cksyncenginedidfetchrecordzonechangesevent.md)
  An object that provides information about a finished record zone fetch.
- [didFetchChangesEvent](./cksyncengineevent/didfetchchangesevent.md)
  The event downcast to the subclass that represents a completed database fetch.
- [CKSyncEngineDidFetchChangesEvent](./cksyncenginedidfetchchangesevent.md)
  The sync engine finished fetching changes from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginefetchedrecordzonechangesevent)*