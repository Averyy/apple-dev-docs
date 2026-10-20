# CKSyncEngine.Event.sentDatabaseChanges(_:)

**Framework**: CloudKit  
**Kind**: case  
**Role**: Case

The sync engine sent a batch of database changes to the server.

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
case sentDatabaseChanges(CKSyncEngine.Event.SentDatabaseChanges)
```

## See Also

### Pending local changes
- [case willSendChanges(CKSyncEngine.Event.WillSendChanges)](./willsendchanges%28_%29.md)
  The sync engine is about to send changes to the server.
- [CKSyncEngine.Event.WillSendChanges](./willsendchanges.md)
  A type that provides information about an imminent send of local changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/sentdatabasechanges(_:))*