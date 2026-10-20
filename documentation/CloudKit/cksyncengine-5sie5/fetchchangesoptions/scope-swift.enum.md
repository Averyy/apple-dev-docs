# CKSyncEngine.FetchChangesOptions.Scope

**Framework**: CloudKit  
**Kind**: enum

The scope for fetching changes from the server.

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
- [CKSyncEngine.FetchChangesOptions.Scope.all](cksyncengine-5sie5/fetchchangesoptions/scope-swift.enum/all.md)
  Fetch changes for all zones.
- [CKSyncEngine.FetchChangesOptions.Scope.allExcluding(_:)](cksyncengine-5sie5/fetchchangesoptions/scope-swift.enum/allexcluding(_:).md)
  Fetch changes for all zones except the given set of zones.
- [CKSyncEngine.FetchChangesOptions.Scope.zoneIDs(_:)](cksyncengine-5sie5/fetchchangesoptions/scope-swift.enum/zoneids(_:).md)
  Fetch changes in a specific set of zones.
### Instance Methods
- [func contains(CKRecordZone.ID) -> Bool](cksyncengine-5sie5/fetchchangesoptions/scope-swift.enum/contains(_:).md)
  Returns true if the specified zone ID is included in this scope.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/fetchchangesoptions/scope-swift.enum)*