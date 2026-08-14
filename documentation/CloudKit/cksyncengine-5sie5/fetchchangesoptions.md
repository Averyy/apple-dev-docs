# CKSyncEngine.FetchChangesOptions

**Framework**: CloudKit  
**Kind**: struct

A set of options to use when fetching changes from the server.

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
### Debugging the options
- [var description: String](cksyncengine-5sie5/fetchchangesoptions/description.md)
  A textual description of the options that’s suitable for logging.
### Initializers
- [init(scope: CKSyncEngine.FetchChangesOptions.Scope, operationGroup: CKOperationGroup?)](cksyncengine-5sie5/fetchchangesoptions/init(scope:operationgroup:).md)
  Creates a new set of fetch changes options.
### Instance Properties
- [var prioritizedZoneIDs: [CKRecordZone.ID]](cksyncengine-5sie5/fetchchangesoptions/prioritizedzoneids.md)
  A list of zones that should be prioritized over others while fetching changes.
- [var scope: CKSyncEngine.FetchChangesOptions.Scope](cksyncengine-5sie5/fetchchangesoptions/scope-swift.property.md)
  The scope in which to fetch changes.
### Enumerations
- [CKSyncEngine.FetchChangesOptions.Scope](cksyncengine-5sie5/fetchchangesoptions/scope-swift.enum.md)
  The scope for fetching changes from the server.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/fetchchangesoptions/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func fetchChanges(CKSyncEngine.FetchChangesOptions) async throws](cksyncengine-5sie5/fetchchanges(_:).md)
  Fetches pending remote changes from the server.
- [func sendChanges(CKSyncEngine.SendChangesOptions) async throws](cksyncengine-5sie5/sendchanges(_:).md)
  Sends pending local changes to the server.
- [CKSyncEngine.SendChangesOptions](cksyncengine-5sie5/sendchangesoptions.md)
  A set of options to use when sending changes to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/fetchchangesoptions)*