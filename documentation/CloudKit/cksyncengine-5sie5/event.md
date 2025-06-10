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

> ❗ **Important**:  You don’t create instances of this type manually. Instead, the sync engine provides them to your app’s delegate during sync operations.

## Topics

### Account changes
- [case accountChange(CKSyncEngine.Event.AccountChange)](cksyncengine-5sie5/event/accountchange(_:).md)
  An event indicating a change to the device’s iCloud account.
- [CKSyncEngine.Event.AccountChange](cksyncengine-5sie5/event/accountchange.md)
  A type that provides information about a change to the device’s iCloud account.
### Remote database changes
- [case willFetchChanges(CKSyncEngine.Event.WillFetchChanges)](cksyncengine-5sie5/event/willfetchchanges(_:).md)
  An event indicating an imminent database fetch.
- [CKSyncEngine.Event.WillFetchChanges](cksyncengine-5sie5/event/willfetchchanges.md)
  A type that provides information about an imminent database fetch.
- [case fetchedDatabaseChanges(CKSyncEngine.Event.FetchedDatabaseChanges)](cksyncengine-5sie5/event/fetcheddatabasechanges(_:).md)
  An event indicating there are fetched database changes to process.
- [CKSyncEngine.Event.FetchedDatabaseChanges](cksyncengine-5sie5/event/fetcheddatabasechanges.md)
  A type that provides information about fetched database changes.
- [case didFetchChanges(CKSyncEngine.Event.DidFetchChanges)](cksyncengine-5sie5/event/didfetchchanges(_:).md)
  An event that indicates the database fetch is done.
- [CKSyncEngine.Event.DidFetchChanges](cksyncengine-5sie5/event/didfetchchanges.md)
  A type that provides information about a finished database fetch.
### Remote record zone changes
- [case willFetchRecordZoneChanges(CKSyncEngine.Event.WillFetchRecordZoneChanges)](cksyncengine-5sie5/event/willfetchrecordzonechanges(_:).md)
  An event indicating an imminent fetch of changes in a record zone.
- [CKSyncEngine.Event.WillFetchRecordZoneChanges](cksyncengine-5sie5/event/willfetchrecordzonechanges.md)
  A type that provides information about an imminent fetch of changes in a record zone.
- [case fetchedRecordZoneChanges(CKSyncEngine.Event.FetchedRecordZoneChanges)](cksyncengine-5sie5/event/fetchedrecordzonechanges(_:).md)
  An event indicating there are fetched record zone changes to process.
- [CKSyncEngine.Event.FetchedRecordZoneChanges](cksyncengine-5sie5/event/fetchedrecordzonechanges.md)
  A type that provides information about fetched record zone changes.
- [case didFetchRecordZoneChanges(CKSyncEngine.Event.DidFetchRecordZoneChanges)](cksyncengine-5sie5/event/didfetchrecordzonechanges(_:).md)
  An event that indicates the record zone fetch is done.
- [CKSyncEngine.Event.DidFetchRecordZoneChanges](cksyncengine-5sie5/event/didfetchrecordzonechanges.md)
  A type that provides information about a finished record zone fetch.
### Pending local changes
- [case willSendChanges(CKSyncEngine.Event.WillSendChanges)](cksyncengine-5sie5/event/willsendchanges(_:).md)
  An event indicating an imminent send of local changes.
- [CKSyncEngine.Event.WillSendChanges](cksyncengine-5sie5/event/willsendchanges.md)
  A type that provides information about an imminent send of local changes.
- [case sentDatabaseChanges(CKSyncEngine.Event.SentDatabaseChanges)](cksyncengine-5sie5/event/sentdatabasechanges(_:).md)
  An event indicating a sent batch of database changes.
- [CKSyncEngine.Event.SentDatabaseChanges](cksyncengine-5sie5/event/sentdatabasechanges.md)
  A type that provides information about a sent batch of database changes.
- [case sentRecordZoneChanges(CKSyncEngine.Event.SentRecordZoneChanges)](cksyncengine-5sie5/event/sentrecordzonechanges(_:).md)
  An event indicating a sent batch of record zone changes.
- [CKSyncEngine.Event.SentRecordZoneChanges](cksyncengine-5sie5/event/sentrecordzonechanges.md)
  A type that provides information about a sent batch of record zone changes.
- [case didSendChanges(CKSyncEngine.Event.DidSendChanges)](cksyncengine-5sie5/event/didsendchanges(_:).md)
  An event that indicates a finished send operation.
- [CKSyncEngine.Event.DidSendChanges](cksyncengine-5sie5/event/didsendchanges.md)
  A type that provides information about a finished send operation.
### State updates
- [case stateUpdate(CKSyncEngine.Event.StateUpdate)](cksyncengine-5sie5/event/stateupdate(_:).md)
  An event indicating an update to the sync engine’s state.
- [CKSyncEngine.Event.StateUpdate](cksyncengine-5sie5/event/stateupdate.md)
  A type that provides information about an update to the sync engine’s state.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func handleEvent(CKSyncEngine.Event, syncEngine: CKSyncEngine) async](cksyncenginedelegate-1q7g8/handleevent(_:syncengine:).md)
  Tells the delegate to handle the specified sync event.
- [enum CKSyncEngineEventType](cksyncengineeventtype.md)
  Describes an event that occurs during a sync operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event)*