# CKSyncEngine.State

**Framework**: CloudKit  
**Kind**: class

An object that manages the sync engine’s state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
final class State
```

#### Overview

To reliably and consistently sync your app’s data, a sync engine keeps a record of several important pieces of data, such as server changes tokens (for databases and record zones), subscription identifiers, the most recent [`userRecordID`](ckuseridentity/userrecordid.md), and so on. This class automatically manages that state on behalf of your app, but there are certain elements you can modify. For example, you control the list of pending changes to send to the iCloud servers and manipulate that list using the [`add(pendingDatabaseChanges:)`](cksyncengine-5sie5/state-swift.class/add(pendingdatabasechanges:).md) and [`add(pendingRecordZoneChanges:)`](cksyncengine-5sie5/state-swift.class/add(pendingrecordzonechanges:).md) methods. If there aren’t any scheduled sync operations when you invoke these methods, the engine automatically schedules one.

An engine’s state changes periodically and, when it does, the sync engine dispatches a [`CKSyncEngine.Event.stateUpdate(_:)`](cksyncengine-5sie5/event/stateupdate(_:).md) event to your delegate. The event contains an instance of [`CKSyncEngine.State.Serialization`](cksyncengine-5sie5/state-swift.class/serialization.md) and, on receipt of such an event, it’s your responsibility to persist the serialized state to disk so that it’s available across app launches. On the next initialization of the sync engine, you provide the most recently persisted state as part of the engine’s configuration. For more information, see [`init(database:stateSerialization:delegate:)`](cksyncengine-5sie5/configuration/init(database:stateserialization:delegate:).md).

## Topics

### Accessing pending changes
- [var hasPendingUntrackedChanges: Bool](cksyncengine-5sie5/state-swift.class/haspendinguntrackedchanges.md)
  A Boolean value that indicates whether there are pending changes that the sync engine is unaware of.
- [var pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange]](cksyncengine-5sie5/state-swift.class/pendingdatabasechanges.md)
  The database changes that the sync engine has yet to send to the iCloud servers.
- [var pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange]](cksyncengine-5sie5/state-swift.class/pendingrecordzonechanges.md)
  The record zone changes that the sync engine has yet to send to the iCloud servers.
### Manipulating pending changes
- [func add(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/add(pendingdatabasechanges:).md)
  Adds the specified database changes to the state.
- [func remove(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/remove(pendingdatabasechanges:).md)
  Removes the specified database changes from the state.
- [CKSyncEngine.PendingDatabaseChange](cksyncengine-5sie5/pendingdatabasechange.md)
  Describes an unsent database modification.
- [func add(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](cksyncengine-5sie5/state-swift.class/add(pendingrecordzonechanges:).md)
  Adds the specified record zone changes to the state.
- [func remove(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](cksyncengine-5sie5/state-swift.class/remove(pendingrecordzonechanges:).md)
  Removes the specified record zone changes from the state.
- [CKSyncEngine.PendingRecordZoneChange](cksyncengine-5sie5/pendingrecordzonechange.md)
  Describes an unsent record modification.
### Serializing state
- [CKSyncEngine.State.Serialization](cksyncengine-5sie5/state-swift.class/serialization.md)
  A type that contains the serialized representation of a sync engine’s state.
### Instance Properties
- [var zoneIDsWithUnfetchedServerChanges: [CKRecordZone.ID]](cksyncengine-5sie5/state-swift.class/zoneidswithunfetchedserverchanges.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var database: CKDatabase](cksyncengine-5sie5/database.md)
  The associated database.
- [var state: CKSyncEngine.State](cksyncengine-5sie5/state-swift.property.md)
  The sync engine’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/state-swift.class)*