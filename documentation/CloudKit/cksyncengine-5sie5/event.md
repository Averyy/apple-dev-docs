# CKSyncEngine.Event

**Framework**: CloudKit  
**Kind**: enum

Describes an event that occurs during a sync operation.

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
enum Event
```

#### Overview

While syncing, [`CKSyncEngine`](cksyncengine-5sie5.md) posts several different types of events. Each event has an associated struct value with details describing the nature of the event.

See the documentation for each event struct for more details about when and why an event is posted.

> ❗ **Important**: You don’t create instances of this type manually. Instead, the sync engine provides them to your app’s delegate during sync operations.

## Topics

### Account changes
- [case accountChange(CKSyncEngine.Event.AccountChange)](cksyncengine-5sie5/event/accountchange(_:).md)
  The user signed in or out of their account.
- [CKSyncEngine.Event.AccountChange](cksyncengine-5sie5/event/accountchange.md)
  The user signed in or out of their account.
### Remote database changes
- [case willFetchChanges(CKSyncEngine.Event.WillFetchChanges)](cksyncengine-5sie5/event/willfetchchanges(_:).md)
  The sync engine is about to fetch changes from the server.
- [CKSyncEngine.Event.WillFetchChanges](cksyncengine-5sie5/event/willfetchchanges.md)
  The sync engine is about to fetch changes from the server.
- [case fetchedDatabaseChanges(CKSyncEngine.Event.FetchedDatabaseChanges)](cksyncengine-5sie5/event/fetcheddatabasechanges(_:).md)
  The sync engine has fetched new database changes from the server.
- [CKSyncEngine.Event.FetchedDatabaseChanges](cksyncengine-5sie5/event/fetcheddatabasechanges.md)
  A type that provides information about fetched database changes.
- [case didFetchChanges(CKSyncEngine.Event.DidFetchChanges)](cksyncengine-5sie5/event/didfetchchanges(_:).md)
  The sync engine finished fetching changes from the server.
- [CKSyncEngine.Event.DidFetchChanges](cksyncengine-5sie5/event/didfetchchanges.md)
  A type that provides information about a finished database fetch.
### Remote record zone changes
- [case willFetchRecordZoneChanges(CKSyncEngine.Event.WillFetchRecordZoneChanges)](cksyncengine-5sie5/event/willfetchrecordzonechanges(_:).md)
  The sync engine is about to fetch record zone changes from the server for a specific zone.
- [CKSyncEngine.Event.WillFetchRecordZoneChanges](cksyncengine-5sie5/event/willfetchrecordzonechanges.md)
  A type that provides information about an imminent fetch of changes in a record zone.
- [case fetchedRecordZoneChanges(CKSyncEngine.Event.FetchedRecordZoneChanges)](cksyncengine-5sie5/event/fetchedrecordzonechanges(_:).md)
  The sync engine fetched new record zone changes from the server.
- [CKSyncEngine.Event.FetchedRecordZoneChanges](cksyncengine-5sie5/event/fetchedrecordzonechanges.md)
  A type that provides information about fetched record zone changes.
- [case didFetchRecordZoneChanges(CKSyncEngine.Event.DidFetchRecordZoneChanges)](cksyncengine-5sie5/event/didfetchrecordzonechanges(_:).md)
  The sync engine has completed fetching record zone changes from the server for a specific zone.
- [CKSyncEngine.Event.DidFetchRecordZoneChanges](cksyncengine-5sie5/event/didfetchrecordzonechanges.md)
  A type that provides information about a finished record zone fetch.
### Pending local changes
- [case willSendChanges(CKSyncEngine.Event.WillSendChanges)](cksyncengine-5sie5/event/willsendchanges(_:).md)
  The sync engine is about to send changes to the server.
- [CKSyncEngine.Event.WillSendChanges](cksyncengine-5sie5/event/willsendchanges.md)
  A type that provides information about an imminent send of local changes.
- [case sentDatabaseChanges(CKSyncEngine.Event.SentDatabaseChanges)](cksyncengine-5sie5/event/sentdatabasechanges(_:).md)
  The sync engine sent a batch of database changes to the server.
- [CKSyncEngine.Event.SentDatabaseChanges](cksyncengine-5sie5/event/sentdatabasechanges.md)
  A type that provides information about a sent batch of database changes.
- [case sentRecordZoneChanges(CKSyncEngine.Event.SentRecordZoneChanges)](cksyncengine-5sie5/event/sentrecordzonechanges(_:).md)
  The sync engine sent a batch of record zone changes to the server.
- [CKSyncEngine.Event.SentRecordZoneChanges](cksyncengine-5sie5/event/sentrecordzonechanges.md)
  The sync engine finished sending a batch of record zone changes to the server.
- [case didSendChanges(CKSyncEngine.Event.DidSendChanges)](cksyncengine-5sie5/event/didsendchanges(_:).md)
  The sync engine finished sending changes to the server.
- [CKSyncEngine.Event.DidSendChanges](cksyncengine-5sie5/event/didsendchanges.md)
  A type that provides information about a finished send operation.
### State updates
- [case stateUpdate(CKSyncEngine.Event.StateUpdate)](cksyncengine-5sie5/event/stateupdate(_:).md)
  The sync engine updated its state.
- [CKSyncEngine.Event.StateUpdate](cksyncengine-5sie5/event/stateupdate.md)
  The sync engine state was updated, and you should persist it locally.
### Debugging the event
- [var description: String](cksyncengine-5sie5/event/description.md)
  A textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/event/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func handleEvent(CKSyncEngine.Event, syncEngine: CKSyncEngine) async](cksyncenginedelegate-1q7g8/handleevent(_:syncengine:).md)
  Tells the delegate to handle the specified sync event.
- [enum CKSyncEngineEventType](cksyncengineeventtype.md)
  Describes an event that occurs during a sync operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event)*