# pendingDatabaseChanges

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

A list of database changes that the sync engine has yet to send to the iCloud servers.

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
final var pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange] { get }
```

## Discussion

This array contains any pending database changes to send to the iCloud servers. After the sync engine sends those changes, your app’s sync delegate receives an event of type [`CKSyncEngine.Event.SentDatabaseChanges`](../event/sentdatabasechanges.md).

The sync engine keeps this list up-to-date while sending changes to the server. For example, when it successfully saves a zone, it will remove that change from this list. If it fails to send a change due to some retryable error (e.g. a network failure), it will keep that change in this list.

Use the [`add(pendingDatabaseChanges:)`](./add%28pendingdatabasechanges%29.md) and [`remove(pendingDatabaseChanges:)`](./remove%28pendingdatabasechanges%29.md) methods to modify the array’s contents.

## See Also

### Accessing pending changes
- [var hasPendingUntrackedChanges: Bool](./haspendinguntrackedchanges.md)
  A Boolean value that indicates whether there are pending changes that the sync engine is unaware of.
- [var pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange]](./pendingrecordzonechanges.md)
  A list of record zone changes that the sync engine has yet to send to the iCloud servers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/state-swift.class/pendingdatabasechanges)*