# CKSyncEngineEvent

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An event that occurs during a sync operation.

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
@interface CKSyncEngineEvent : NSObject
```

## Overview

All sync operation events descend from this base class, and as such you don’t create instances of it directly. Instead, the sync engine dispatches them to your app’s delegate, periodically, throughout a sync operation.

See the documentation for each event class for more details about when and why an event is posted.

Use the [`type`](./cksyncengineevent/type.md) property to determine the event’s proper type, and then use the corresponding convenience property to retrieve a reference to the event that’s downcast to the appropriate subclass. For example, when CloudKit vends an event with [`type`](./cksyncengineevent/type.md) set to [`CKSyncEngineEventType.stateUpdate`](./cksyncengineeventtype/stateupdate.md), use the [`stateUpdateEvent`](./cksyncengineevent/stateupdateevent.md) property to get the downcast reference.

> ❗ **Important**: It is a fatal error to access a non-corresponding convenience property.

## Topics

### Determining the type
- [type](./cksyncengineevent/type.md)
  The type of event.
- [enum CKSyncEngineEventType](./cksyncengineeventtype.md)
  Describes an event that occurs during a sync operation.
### Accessing account changes
- [accountChangeEvent](./cksyncengineevent/accountchangeevent.md)
  The event downcast to the subclass that represents a change to the device’s iCloud account.
- [CKSyncEngineAccountChangeEvent](./cksyncengineaccountchangeevent.md)
  The user signed in or out of their account.
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
- [CKSyncEngineDidFetchRecordZoneChangesEvent](./cksyncenginedidfetchrecordzonechangesevent.md)
  An object that provides information about a finished record zone fetch.
- [didFetchChangesEvent](./cksyncengineevent/didfetchchangesevent.md)
  The event downcast to the subclass that represents a completed database fetch.
- [CKSyncEngineDidFetchChangesEvent](./cksyncenginedidfetchchangesevent.md)
  The sync engine finished fetching changes from the server.
### Accessing send events
- [willSendChangesEvent](./cksyncengineevent/willsendchangesevent.md)
  The event downcast to the subclass that represents an imminent send operation.
- [CKSyncEngineWillSendChangesEvent](./cksyncenginewillsendchangesevent.md)
  An object that provides information about an imminent send of local changes.
- [sentDatabaseChangesEvent](./cksyncengineevent/sentdatabasechangesevent.md)
  The event downcast to the subclass that represents a sent batch of database changes.
- [CKSyncEngineSentDatabaseChangesEvent](./cksyncenginesentdatabasechangesevent.md)
  An object that provides information about a sent batch of database changes.
- [sentRecordZoneChangesEvent](./cksyncengineevent/sentrecordzonechangesevent.md)
  The event downcast to the subclass that represents a sent batch of record zone changes.
- [CKSyncEngineSentRecordZoneChangesEvent](./cksyncenginesentrecordzonechangesevent.md)
  The sync engine finished sending a batch of record zone changes to the server.
- [didSendChangesEvent](./cksyncengineevent/didsendchangesevent.md)
  The event downcast to the subclass that represents a completed send operation.
- [CKSyncEngineDidSendChangesEvent](./cksyncenginedidsendchangesevent.md)
  An object that provides information about a finished send operation.
### Accessing state updates
- [stateUpdateEvent](./cksyncengineevent/stateupdateevent.md)
  The event downcast to the subclass that represents an update to the sync engine’s state.
- [CKSyncEngineStateUpdateEvent](./cksyncenginestateupdateevent.md)
  The sync engine state was updated, and you should persist it locally.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CKSyncEngineAccountChangeEvent](./cksyncengineaccountchangeevent.md)
- [CKSyncEngineDidFetchChangesEvent](./cksyncenginedidfetchchangesevent.md)
- [CKSyncEngineDidFetchRecordZoneChangesEvent](./cksyncenginedidfetchrecordzonechangesevent.md)
- [CKSyncEngineDidSendChangesEvent](./cksyncenginedidsendchangesevent.md)
- [CKSyncEngineFetchedDatabaseChangesEvent](./cksyncenginefetcheddatabasechangesevent.md)
- [CKSyncEngineFetchedRecordZoneChangesEvent](./cksyncenginefetchedrecordzonechangesevent.md)
- [CKSyncEngineSentDatabaseChangesEvent](./cksyncenginesentdatabasechangesevent.md)
- [CKSyncEngineSentRecordZoneChangesEvent](./cksyncenginesentrecordzonechangesevent.md)
- [CKSyncEngineStateUpdateEvent](./cksyncenginestateupdateevent.md)
- [CKSyncEngineWillFetchChangesEvent](./cksyncenginewillfetchchangesevent.md)
- [CKSyncEngineWillFetchRecordZoneChangesEvent](./cksyncenginewillfetchrecordzonechangesevent.md)
- [CKSyncEngineWillSendChangesEvent](./cksyncenginewillsendchangesevent.md)

## See Also

### Handling sync events
- [- syncEngine:handleEvent:](./cksyncenginedelegate-3c38p/syncengine_handleevent_.md)
  Tells the delegate to handle the specified sync event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineevent)*