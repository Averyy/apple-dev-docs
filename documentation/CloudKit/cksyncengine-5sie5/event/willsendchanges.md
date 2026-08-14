# CKSyncEngine.Event.WillSendChanges

**Framework**: CloudKit  
**Kind**: struct

A type that provides information about an imminent send of local changes.

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
struct WillSendChanges
```

## Topics

### Accessing the context
- [let context: CKSyncEngine.SendChangesContext](cksyncengine-5sie5/event/willsendchanges/context.md)
  The context of the imminent send request.
### Debugging the event
- [var description: String](cksyncengine-5sie5/event/willsendchanges/description.md)
  A textual description of the event that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/event/willsendchanges/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case willSendChanges(CKSyncEngine.Event.WillSendChanges)](cksyncengine-5sie5/event/willsendchanges(_:).md)
  The sync engine is about to send changes to the server.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/event/willsendchanges)*