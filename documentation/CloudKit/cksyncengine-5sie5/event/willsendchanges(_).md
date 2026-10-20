# CKSyncEngine.Event.willSendChanges(_:)

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

The sync engine is about to send changes to the server.

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
case willSendChanges(CKSyncEngine.Event.WillSendChanges)
```

#### Discussion

A send operation may send all local changes, only changes to a specific set of records, or only those in a specific record zone. Use this case’s associated value to determine the scope for the current operation. For more information, see [`CKSyncEngine.SendChangesContext`](../sendchangescontext.md).

## See Also

### Pending local changes
- [CKSyncEngine.Event.WillSendChanges](./willsendchanges.md)
  A type that provides information about an imminent send of local changes.
- [case sentDatabaseChanges(CKSyncEngine.Event.SentDatabaseChanges)](./sentdatabasechanges%28_%29.md)
  The sync engine sent a batch of database changes to the server.
- [CKSyncEngine.Event.SentDatabaseChanges](./sentdatabasechanges.md)
  A type that provides information about a sent batch of database changes.
- [case sentRecordZoneChanges(CKSyncEngine.Event.SentRecordZoneChanges)](./sentrecordzonechanges%28_%29.md)
  The sync engine sent a batch of record zone changes to the server.
- [CKSyncEngine.Event.SentRecordZoneChanges](./sentrecordzonechanges.md)
  The sync engine finished sending a batch of record zone changes to the server.
- [case didSendChanges(CKSyncEngine.Event.DidSendChanges)](./didsendchanges%28_%29.md)
  The sync engine finished sending changes to the server.
- [CKSyncEngine.Event.DidSendChanges](./didsendchanges.md)
  A type that provides information about a finished send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/willsendchanges(_:))*