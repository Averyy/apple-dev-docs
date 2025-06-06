# add(pendingRecordZoneChanges:)

**Framework**: Cloudkit  
**Kind**: method

Adds the specified record zone changes to the state.

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
final func add(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])
```

#### Discussion

Use this method to enable the sync engine to manage your pending record zone changes. For example, when someone makes a change that your app needs to send to the server, use this method to record the change. Then, when creating the change batch for the next send operation, retrieve the pending changes from the [`pendingRecordZoneChanges`](cksyncengine-5sie5/state-swift.class/pendingrecordzonechanges.md) property.

If there are no scheduled sync operations when you invoke this method, the sync engine automatically schedules one to send the changes. After the engine sends those changes, it notifies your app’s sync delegate with an event of type [`CKSyncEngine.Event.SentRecordZoneChanges`](cksyncengine-5sie5/event/sentrecordzonechanges.md).

The sync engine ensures the consistency of any pending changes it’s tracking, deduplicating them as necessary. The engine removes changes from the list as it sends them, but retains any that fail due to a recoverable error, such as a network issue or exceeding the rate limit.

> **Note**:  The order in which you apply record zone changes is important. For example, if you add a save change and then a delete change, the sync engine discards the save and sends only the delete change. The reverse is also true.

## Parameters

- `pendingRecordZoneChanges`: An array of record zone changes.

## See Also

- [func add(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/add(pendingdatabasechanges:).md)
  Adds the specified database changes to the state.
- [func remove(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/remove(pendingdatabasechanges:).md)
  Removes the specified database changes from the state.
- [CKSyncEngine.PendingDatabaseChange](cksyncengine-5sie5/pendingdatabasechange.md)
  Describes an unsent database modification.
- [func remove(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](cksyncengine-5sie5/state-swift.class/remove(pendingrecordzonechanges:).md)
  Removes the specified record zone changes from the state.
- [CKSyncEngine.PendingRecordZoneChange](cksyncengine-5sie5/pendingrecordzonechange.md)
  Describes an unsent record modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/state-swift.class/add(pendingrecordzonechanges:))*