# CKSyncEngineEventType

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Describes an event that occurs during a sync operation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum CKSyncEngineEventType
```

```c
enum CKSyncEngineEventType : NSInteger;
```

## Topics

### Event types
- [CKSyncEngineEventType.stateUpdate](./cksyncengineeventtype/stateupdate.md)
  The sync engine updated its state.
- [CKSyncEngineEventType.accountChange](./cksyncengineeventtype/accountchange.md)
  The user signed in or out of their account.
- [CKSyncEngineEventType.fetchedDatabaseChanges](./cksyncengineeventtype/fetcheddatabasechanges.md)
  The sync engine has fetched new database changes from the server.
- [CKSyncEngineEventType.fetchedRecordZoneChanges](./cksyncengineeventtype/fetchedrecordzonechanges.md)
  The sync engine fetched new record zone changes from the server.
- [CKSyncEngineEventType.sentDatabaseChanges](./cksyncengineeventtype/sentdatabasechanges.md)
  The sync engine sent a batch of database changes to the server.
- [CKSyncEngineEventType.sentRecordZoneChanges](./cksyncengineeventtype/sentrecordzonechanges.md)
  The sync engine sent a batch of record zone changes to the server.
- [CKSyncEngineEventType.willFetchChanges](./cksyncengineeventtype/willfetchchanges.md)
  The sync engine is about to fetch changes from the server.
- [CKSyncEngineEventType.willFetchRecordZoneChanges](./cksyncengineeventtype/willfetchrecordzonechanges.md)
  The sync engine is about to fetch record zone changes from the server for a specific zone.
- [CKSyncEngineEventType.didFetchRecordZoneChanges](./cksyncengineeventtype/didfetchrecordzonechanges.md)
  The sync engine has completed fetching record zone changes from the server for a specific zone.
- [CKSyncEngineEventType.didFetchChanges](./cksyncengineeventtype/didfetchchanges.md)
  The sync engine finished fetching changes from the server.
- [CKSyncEngineEventType.willSendChanges](./cksyncengineeventtype/willsendchanges.md)
  The sync engine is about to send changes to the server.
- [CKSyncEngineEventType.didSendChanges](./cksyncengineeventtype/didsendchanges.md)
  The sync engine finished sending changes to the server.
### Initializers
- [init?(rawValue: Int)](./cksyncengineeventtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Handling sync events
- [func handleEvent(CKSyncEngine.Event, syncEngine: CKSyncEngine) async](./cksyncenginedelegate-1q7g8/handleevent%28_,syncengine%29.md)
  Tells the delegate to handle the specified sync event.
- [CKSyncEngine.Event](./cksyncengine-5sie5/event.md)
  Describes an event that occurs during a sync operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineeventtype)*