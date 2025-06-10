# CKSyncEngine.FetchChangesOptions

**Framework**: CloudKit  
**Kind**: struct

A set of options to use with a fetch operation.

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
struct FetchChangesOptions
```

## Topics

### Managing attributes
- [var operationGroup: CKOperationGroup](cksyncengine-5sie5/fetchchangesoptions/operationgroup.md)
  The operation group to use for the underlying CloudKit operations.
### Initializers
- [init(scope: CKSyncEngine.FetchChangesOptions.Scope, operationGroup: CKOperationGroup?)](cksyncengine-5sie5/fetchchangesoptions/init(scope:operationgroup:).md)
### Instance Properties
- [var prioritizedZoneIDs: [CKRecordZone.ID]](cksyncengine-5sie5/fetchchangesoptions/prioritizedzoneids.md)
- [var scope: CKSyncEngine.FetchChangesOptions.Scope](cksyncengine-5sie5/fetchchangesoptions/scope-swift.property.md)
### Enumerations
- [CKSyncEngine.FetchChangesOptions.Scope](cksyncengine-5sie5/fetchchangesoptions/scope-swift.enum.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func fetchChanges(CKSyncEngine.FetchChangesOptions) async throws](cksyncengine-5sie5/fetchchanges(_:).md)
  Fetches pending remote changes from the server.
- [func sendChanges(CKSyncEngine.SendChangesOptions) async throws](cksyncengine-5sie5/sendchanges(_:).md)
  Sends pending local changes to the server.
- [CKSyncEngine.SendChangesOptions](cksyncengine-5sie5/sendchangesoptions.md)
  A set of options to use with a send operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/fetchchangesoptions)*