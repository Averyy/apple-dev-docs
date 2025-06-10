# CKSyncEngine.PendingRecordZoneChange

**Framework**: CloudKit  
**Kind**: enum

Describes an unsent record modification.

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
enum PendingRecordZoneChange
```

## Topics

### Record change types
- [enum CKSyncEnginePendingRecordZoneChangeType](cksyncenginependingrecordzonechangetype.md)
  Describes a type of modification a record zone change makes.
### Enumeration Cases
- [CKSyncEngine.PendingRecordZoneChange.deleteRecord(_:)](cksyncengine-5sie5/pendingrecordzonechange/deleterecord(_:).md)
- [CKSyncEngine.PendingRecordZoneChange.saveRecord(_:)](cksyncengine-5sie5/pendingrecordzonechange/saverecord(_:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func add(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/add(pendingdatabasechanges:).md)
  Adds the specified database changes to the state.
- [func remove(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/remove(pendingdatabasechanges:).md)
  Removes the specified database changes from the state.
- [CKSyncEngine.PendingDatabaseChange](cksyncengine-5sie5/pendingdatabasechange.md)
  Describes an unsent database modification.
- [func add(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](cksyncengine-5sie5/state-swift.class/add(pendingrecordzonechanges:).md)
  Adds the specified record zone changes to the state.
- [func remove(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](cksyncengine-5sie5/state-swift.class/remove(pendingrecordzonechanges:).md)
  Removes the specified record zone changes from the state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/pendingrecordzonechange)*