# CKSyncEngineDidSendChangesEvent

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that provides information about a finished send operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface CKSyncEngineDidSendChangesEvent : CKSyncEngineEvent
```

## Topics

### Accessing the context
- [context](./cksyncenginedidsendchangesevent/context.md)
  The context of the finished send request.

## Relationships

### Inherits From
- [CKSyncEngineEvent](./cksyncengineevent.md)

## See Also

### Accessing send events
- [willSendChangesEvent](./cksyncengineevent/willsendchangesevent.md)
  The event downcast to the subclass that represents an imminent send operation.
- [CKSyncEngineWillSendChangesEvent](./cksyncenginewillsendchangesevent.md)
  An object that provides information about an imminent send of local changes.
- [sentDatabaseChangesEvent](./cksyncengineevent/sentdatabasechangesevent.md)
  The event downcast to the subclass that represents a sent batch of database changes.
- [CKSyncEngineSentDatabaseChangesEvent](./cksyncenginesentdatabasechangesevent.md)
  An object that provides information about a sent batch of database changes.
- [sentRecordZoneChangesEvent](./cksyncengineevent/sentrecordzonechangesevent.md)
  The event downcast to the subclass that represents a sent batch of record zone changes.
- [CKSyncEngineSentRecordZoneChangesEvent](./cksyncenginesentrecordzonechangesevent.md)
  The sync engine finished sending a batch of record zone changes to the server.
- [didSendChangesEvent](./cksyncengineevent/didsendchangesevent.md)
  The event downcast to the subclass that represents a completed send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginedidsendchangesevent)*