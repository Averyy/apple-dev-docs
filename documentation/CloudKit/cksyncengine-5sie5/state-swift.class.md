# CKSyncEngine.State

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
- visionOS
- watchOS 10.0+

## Declaration

```swift
final class State
```

#### Overview

To reliably and consistently sync your app’s data, a sync engine keeps a record of several important pieces of data, such as server changes tokens (for databases and record zones), subscription identifiers, the most recent [`userRecordID`](../ckuseridentity/userrecordid.md), and so on. This class automatically manages that state on behalf of your app, but there are certain elements you can modify. For example, you control the list of pending changes to send to the iCloud servers and manipulate that list using the [`add(pendingDatabaseChanges:)`](./state-swift.class/add%28pendingdatabasechanges%29.md) and [`add(pendingRecordZoneChanges:)`](./state-swift.class/add%28pendingrecordzonechanges%29.md) methods. If there aren’t any scheduled sync operations when you invoke these methods, the engine automatically schedules one.

An engine’s state changes periodically and, when it does, the sync engine dispatches a [`CKSyncEngine.Event.stateUpdate(_:)`](./event/stateupdate%28_%29.md) event to your delegate. The event contains an instance of [`CKSyncEngine.State.Serialization`](./state-swift.class/serialization.md) and, on receipt of such an event, it’s your responsibility to persist the serialized state to disk so that it’s available across app launches. On the next initialization of the sync engine, you provide the most recently persisted state as part of the engine’s configuration. For more information, see [`init(database:stateSerialization:delegate:)`](./configuration/init%28database,stateserialization,delegate%29.md).

## Topics

### Accessing pending changes
- [var hasPendingUntrackedChanges: Bool](./state-swift.class/haspendinguntrackedchanges.md)
  A Boolean value that indicates whether there are pending changes that the sync engine is unaware of.
- [var pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange]](./state-swift.class/pendingdatabasechanges.md)
  A list of database changes that the sync engine has yet to send to the iCloud servers.
- [var pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange]](./state-swift.class/pendingrecordzonechanges.md)
  A list of record zone changes that the sync engine has yet to send to the iCloud servers.
### Manipulating pending changes
- [func add(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](./state-swift.class/add%28pendingdatabasechanges%29.md)
  Adds the specified database changes to the state.
- [func remove(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](./state-swift.class/remove%28pendingdatabasechanges%29.md)
  Removes the specified database changes from the state.
- [CKSyncEngine.PendingDatabaseChange](./pendingdatabasechange.md)
  Describes an unsent database modification.
- [func add(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](./state-swift.class/add%28pendingrecordzonechanges%29.md)
  Adds the specified record zone changes to the state.
- [func remove(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](./state-swift.class/remove%28pendingrecordzonechanges%29.md)
  Removes the specified record zone changes from the state.
- [CKSyncEngine.PendingRecordZoneChange](./pendingrecordzonechange.md)
  Describes an unsent record modification.
### Serializing state
- [CKSyncEngine.State.Serialization](./state-swift.class/serialization.md)
  A type that contains the serialized representation of a sync engine’s state.
### Instance Properties
- [var zoneIDsWithUnfetchedServerChanges: [CKRecordZone.ID]](./state-swift.class/zoneidswithunfetchedserverchanges.md)
  The identifiers of zones with changes on the server that have not yet been fetched.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the engine’s attributes
- [var database: CKDatabase](./database.md)
  The associated database.
- [var state: CKSyncEngine.State](./state-swift.property.md)
  A collection of state properties used to efficiently manage sync engine operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/state-swift.class)*