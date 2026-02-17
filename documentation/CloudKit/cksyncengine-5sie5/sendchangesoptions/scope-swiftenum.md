# CKSyncEngine.SendChangesOptions.Scope

**Framework**: CloudKit  
**Kind**: enum

The scope for sending changes to the server.

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
enum Scope
```

## Topics

### Enumeration Cases
- [CKSyncEngine.SendChangesOptions.Scope.all](cksyncengine-5sie5/sendchangesoptions/scope-swift.enum/all.md)
  Send changes for all zones.
- [CKSyncEngine.SendChangesOptions.Scope.allExcluding(_:)](cksyncengine-5sie5/sendchangesoptions/scope-swift.enum/allexcluding(_:).md)
  Send changes for all zones except the given set of zones.
- [CKSyncEngine.SendChangesOptions.Scope.recordIDs(_:)](cksyncengine-5sie5/sendchangesoptions/scope-swift.enum/recordids(_:).md)
  Send changes for a specific set of records.
- [CKSyncEngine.SendChangesOptions.Scope.zoneIDs(_:)](cksyncengine-5sie5/sendchangesoptions/scope-swift.enum/zoneids(_:).md)
  Send changes in a specific set of zones.
### Instance Methods
- [func contains(CKRecord.ID) -> Bool](cksyncengine-5sie5/sendchangesoptions/scope-swift.enum/contains(_:)-59hve.md)
  Returns true if the specified record ID is included in this scope.
- [func contains(CKSyncEngine.PendingRecordZoneChange) -> Bool](cksyncengine-5sie5/sendchangesoptions/scope-swift.enum/contains(_:)-8qiyf.md)
  Returns true if the specified pending record zone change is included in this scope.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/sendchangesoptions/scope-swift.enum)*