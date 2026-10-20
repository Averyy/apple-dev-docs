# CKSyncEngine.FetchChangesOptions.Scope

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

The scope for fetching changes from the server.

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
enum Scope
```

## Topics

### Enumeration Cases
- [CKSyncEngine.FetchChangesOptions.Scope.all](./scope-swift.enum/all.md)
  Fetch changes for all zones.
- [CKSyncEngine.FetchChangesOptions.Scope.allExcluding(_:)](./scope-swift.enum/allexcluding%28_%29.md)
  Fetch changes for all zones except the given set of zones.
- [CKSyncEngine.FetchChangesOptions.Scope.zoneIDs(_:)](./scope-swift.enum/zoneids%28_%29.md)
  Fetch changes in a specific set of zones.
### Instance Methods
- [func contains(CKRecordZone.ID) -> Bool](./scope-swift.enum/contains%28_%29.md)
  Returns true if the specified zone ID is included in this scope.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/fetchchangesoptions/scope-swift.enum)*