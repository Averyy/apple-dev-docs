# CKSyncEngine.FetchChangesOptions

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A set of options to use when fetching changes from the server.

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
struct FetchChangesOptions
```

## Topics

### Managing attributes
- [var operationGroup: CKOperationGroup](./fetchchangesoptions/operationgroup.md)
  The operation group to use for the underlying CloudKit operations.
### Debugging the options
- [var description: String](./fetchchangesoptions/description.md)
  A textual description of the options that’s suitable for logging.
### Initializers
- [init(scope: CKSyncEngine.FetchChangesOptions.Scope, operationGroup: CKOperationGroup?)](./fetchchangesoptions/init%28scope,operationgroup%29.md)
  Creates a new set of fetch changes options.
### Instance Properties
- [var prioritizedZoneIDs: [CKRecordZone.ID]](./fetchchangesoptions/prioritizedzoneids.md)
  A list of zones that should be prioritized over others while fetching changes.
- [var scope: CKSyncEngine.FetchChangesOptions.Scope](./fetchchangesoptions/scope-swift.property.md)
  The scope in which to fetch changes.
### Enumerations
- [CKSyncEngine.FetchChangesOptions.Scope](./fetchchangesoptions/scope-swift.enum.md)
  The scope for fetching changes from the server.
### Default Implementations
- [CustomStringConvertible Implementations](./fetchchangesoptions/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Invoking manual sync operations
- [func fetchChanges(CKSyncEngine.FetchChangesOptions) async throws](./fetchchanges%28_%29.md)
  Fetches pending remote changes from the server.
- [func sendChanges(CKSyncEngine.SendChangesOptions) async throws](./sendchanges%28_%29.md)
  Sends pending local changes to the server.
- [CKSyncEngine.SendChangesOptions](./sendchangesoptions.md)
  A set of options to use when sending changes to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/fetchchangesoptions)*