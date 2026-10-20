# CKSyncEngine.SendChangesOptions

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A set of options to use when sending changes to the server.

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
struct SendChangesOptions
```

## Topics

### Managing attributes
- [var description: String](./sendchangesoptions/description.md)
  A textual description of the options that’s suitable for logging.
- [var operationGroup: CKOperationGroup](./sendchangesoptions/operationgroup.md)
  The operation group to use for the underlying CloudKit operations.
### Debugging options
- [var description: String](./sendchangesoptions/description.md)
  A textual description of the options that’s suitable for logging.
### Initializers
- [init(scope: CKSyncEngine.SendChangesOptions.Scope, operationGroup: CKOperationGroup?)](./sendchangesoptions/init%28scope,operationgroup%29.md)
  Creates a new set of send changes options.
### Instance Properties
- [var scope: CKSyncEngine.SendChangesOptions.Scope](./sendchangesoptions/scope-swift.property.md)
  The scope of the changes to send.
### Enumerations
- [CKSyncEngine.SendChangesOptions.Scope](./sendchangesoptions/scope-swift.enum.md)
  The scope for sending changes to the server.
### Default Implementations
- [CustomStringConvertible Implementations](./sendchangesoptions/customstringconvertible-implementations.md)

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
- [CKSyncEngine.FetchChangesOptions](./fetchchangesoptions.md)
  A set of options to use when fetching changes from the server.
- [func sendChanges(CKSyncEngine.SendChangesOptions) async throws](./sendchanges%28_%29.md)
  Sends pending local changes to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/sendchangesoptions)*