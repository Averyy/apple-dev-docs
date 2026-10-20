# CKSyncEngine.Event.DidSendChanges

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A type that provides information about a finished send operation.

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
struct DidSendChanges
```

## Topics

### Accessing the context
- [let context: CKSyncEngine.SendChangesContext](./didsendchanges/context.md)
  The context of the finished send request.
### Debugging the event
- [var description: String](./didsendchanges/description.md)
  A textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./didsendchanges/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Escapable](../../../Swift/escapable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Pending local changes
- [case willSendChanges(CKSyncEngine.Event.WillSendChanges)](./willsendchanges%28_%29.md)
  The sync engine is about to send changes to the server.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/didsendchanges)*