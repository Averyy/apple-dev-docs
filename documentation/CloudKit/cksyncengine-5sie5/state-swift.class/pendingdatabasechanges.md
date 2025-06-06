# pendingDatabaseChanges

**Framework**: CloudKit  
**Kind**: property

The database changes that the sync engine has yet to send to the iCloud servers.

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
final var pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange] { get }
```

#### Discussion

This array contains any pending database changes to send to the iCloud servers in a subsequent send operation (scheduled or manual). After the sync engine sends those changes, your app’s sync delegate receives an event of type [`CKSyncEngine.Event.SentDatabaseChanges`](cksyncengine-5sie5/event/sentdatabasechanges.md).

Use the [`add(pendingDatabaseChanges:)`](cksyncengine-5sie5/state-swift.class/add(pendingdatabasechanges:).md) and [`remove(pendingDatabaseChanges:)`](cksyncengine-5sie5/state-swift.class/remove(pendingdatabasechanges:).md) methods to modify the array’s contents.

## See Also

- [var hasPendingUntrackedChanges: Bool](cksyncengine-5sie5/state-swift.class/haspendinguntrackedchanges.md)
  A Boolean value that indicates whether there are pending changes that the sync engine is unaware of.
- [var pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange]](cksyncengine-5sie5/state-swift.class/pendingrecordzonechanges.md)
  The record zone changes that the sync engine has yet to send to the iCloud servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/state-swift.class/pendingdatabasechanges)*