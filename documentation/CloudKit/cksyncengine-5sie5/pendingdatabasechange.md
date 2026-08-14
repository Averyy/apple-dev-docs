# CKSyncEngine.PendingDatabaseChange

**Framework**: CloudKit  
**Kind**: enum

Describes an unsent database modification.

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
enum PendingDatabaseChange
```

## Topics

### Database change types
- [enum CKSyncEnginePendingDatabaseChangeType](cksyncenginependingdatabasechangetype.md)
  Describes the type of a pending database change.
### Identifying and comparing changes
- [static func == (CKSyncEngine.PendingDatabaseChange, CKSyncEngine.PendingDatabaseChange) -> Bool](cksyncengine-5sie5/pendingdatabasechange/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Debugging the change
- [var description: String](cksyncengine-5sie5/pendingdatabasechange/description.md)
  A textual description of the change that’s suitable for logging.
### Enumeration Cases
- [CKSyncEngine.PendingDatabaseChange.deleteZone(_:)](cksyncengine-5sie5/pendingdatabasechange/deletezone(_:).md)
  A pending deletion of a zone from the server.
- [CKSyncEngine.PendingDatabaseChange.saveZone(_:)](cksyncengine-5sie5/pendingdatabasechange/savezone(_:).md)
  A pending save of a zone to the server.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/pendingdatabasechange/customstringconvertible-implementations.md)
- [Equatable Implementations](cksyncengine-5sie5/pendingdatabasechange/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func add(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/add(pendingdatabasechanges:).md)
  Adds the specified database changes to the state.
- [func remove(pendingDatabaseChanges: [CKSyncEngine.PendingDatabaseChange])](cksyncengine-5sie5/state-swift.class/remove(pendingdatabasechanges:).md)
  Removes the specified database changes from the state.
- [func add(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](cksyncengine-5sie5/state-swift.class/add(pendingrecordzonechanges:).md)
  Adds the specified record zone changes to the state.
- [func remove(pendingRecordZoneChanges: [CKSyncEngine.PendingRecordZoneChange])](cksyncengine-5sie5/state-swift.class/remove(pendingrecordzonechanges:).md)
  Removes the specified record zone changes from the state.
- [CKSyncEngine.PendingRecordZoneChange](cksyncengine-5sie5/pendingrecordzonechange.md)
  Describes an unsent record modification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/pendingdatabasechange)*