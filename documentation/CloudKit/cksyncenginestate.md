# CKSyncEngineState

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that manages the sync engine’s state.

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
@interface CKSyncEngineState : NSObject
```

## Overview

To reliably and consistently sync your app’s data, a sync engine keeps a record of several important pieces of data, such as server changes tokens (for databases and record zones), subscription identifiers, the most recent [`userRecordID`](./ckuseridentity/userrecordid.md), and so on. This class automatically manages that state on behalf of your app, but there are certain elements you can modify. For example, you control the list of pending changes to send to the iCloud servers and manipulate that list using the [`addPendingDatabaseChanges:`](./cksyncenginestate/addpendingdatabasechanges_.md) and [`addPendingRecordZoneChanges:`](./cksyncenginestate/addpendingrecordzonechanges_.md) methods. If there aren’t any scheduled sync operations when you invoke these methods, the engine automatically schedules one.

An engine’s state changes periodically and, when it does, the sync engine dispatches an event of type  [`CKSyncEngineStateUpdateEvent`](./cksyncenginestateupdateevent.md) to your delegate. The event contains an instance of [`CKSyncEngineStateSerialization`](./cksyncenginestateserialization.md) and, on receipt of such an event, it’s your responsibility to persist the serialized state to disk so that it’s available across app launches. On the next initialization of the sync engine, you provide the most recently persisted state as part of the engine’s configuration. For more information, see [`initWithDatabase:stateSerialization:delegate:`](./cksyncengineconfiguration/initwithdatabase_stateserialization_delegate_.md).

## Topics

### Accessing pending changes
- [hasPendingUntrackedChanges](./cksyncenginestate/haspendinguntrackedchanges.md)
  A Boolean value that indicates whether there are pending changes that the sync engine is unaware of.
- [pendingDatabaseChanges](./cksyncenginestate/pendingdatabasechanges.md)
  A list of database changes that the sync engine has yet to send to the iCloud servers.
- [pendingRecordZoneChanges](./cksyncenginestate/pendingrecordzonechanges.md)
  A list of record zone changes that the sync engine has yet to send to the iCloud servers.
### Modifying pending changes
- [- addPendingDatabaseChanges:](./cksyncenginestate/addpendingdatabasechanges_.md)
  Adds the specified database changes to the state.
- [- removePendingDatabaseChanges:](./cksyncenginestate/removependingdatabasechanges_.md)
  Removes the specified database changes from the state.
- [CKSyncEnginePendingZoneDelete](./cksyncenginependingzonedelete.md)
  An object that describes an unsent record zone deletion.
- [CKSyncEnginePendingZoneSave](./cksyncenginependingzonesave.md)
  An object that describes an unsent record zone modification.
- [CKSyncEnginePendingDatabaseChange](./cksyncenginependingdatabasechange.md)
  An object that describes an unsent database modification.
- [- addPendingRecordZoneChanges:](./cksyncenginestate/addpendingrecordzonechanges_.md)
  Adds the specified record zone changes to the state.
- [- removePendingRecordZoneChanges:](./cksyncenginestate/removependingrecordzonechanges_.md)
  Removes the specified record zone changes from the state.
- [CKSyncEnginePendingRecordZoneChange](./cksyncenginependingrecordzonechange.md)
  An object that describes an unsent record modification.
### Instance Properties
- [zoneIDsWithUnfetchedServerChanges](./cksyncenginestate/zoneidswithunfetchedserverchanges.md)
  The identifiers of zones with changes on the server that have not yet been fetched.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Accessing the engine’s attributes
- [database](./cksyncengine-4b4w9/database.md)
  The associated database.
- [state](./cksyncengine-4b4w9/state.md)
  A collection of state properties used to efficiently manage sync engine operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginestate)*