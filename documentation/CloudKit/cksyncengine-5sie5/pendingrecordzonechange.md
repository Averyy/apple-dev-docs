# CKSyncEngine.PendingRecordZoneChange

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Describes an unsent record modification.

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
enum PendingRecordZoneChange
```

## Topics

### Record change types
- [enum CKSyncEnginePendingRecordZoneChangeType](../cksyncenginependingrecordzonechangetype.md)
  A type of change in a record zone that needs to be sent to the server.
### Debugging the change
- [var description: String](./pendingrecordzonechange/description.md)
  A textual description of the change that’s suitable for logging.
### Enumeration Cases
- [CKSyncEngine.PendingRecordZoneChange.deleteRecord(_:)](./pendingrecordzonechange/deleterecord%28_%29.md)
  A pending deletion of a record from the server.
- [CKSyncEngine.PendingRecordZoneChange.saveRecord(_:)](./pendingrecordzonechange/saverecord%28_%29.md)
  A pending save of a record to the server.
### Default Implementations
- [CustomStringConvertible Implementations](./pendingrecordzonechange/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Manipulating pending changes
- [func add(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](./state-swift.class/add%28pendingdatabasechanges%29.md)
  Adds the specified database changes to the state.
- [func remove(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](./state-swift.class/remove%28pendingdatabasechanges%29.md)
  Removes the specified database changes from the state.
- [CKSyncEngine.PendingDatabaseChange](./pendingdatabasechange.md)
  Describes an unsent database modification.
- [func add(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](./state-swift.class/add%28pendingrecordzonechanges%29.md)
  Adds the specified record zone changes to the state.
- [func remove(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](./state-swift.class/remove%28pendingrecordzonechanges%29.md)
  Removes the specified record zone changes from the state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/pendingrecordzonechange)*