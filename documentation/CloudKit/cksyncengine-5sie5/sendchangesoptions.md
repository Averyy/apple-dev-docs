# CKSyncEngine.SendChangesOptions

**Framework**: CloudKit  
**Kind**: struct

A set of options to use when sending changes to the server.

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
struct SendChangesOptions
```

## Topics

### Managing attributes
- [var description: String](cksyncengine-5sie5/sendchangesoptions/description.md)
  A textual description of the options that’s suitable for logging.
- [var operationGroup: CKOperationGroup](cksyncengine-5sie5/sendchangesoptions/operationgroup.md)
  The operation group to use for the underlying CloudKit operations.
### Debugging options
- [var description: String](cksyncengine-5sie5/sendchangesoptions/description.md)
  A textual description of the options that’s suitable for logging.
### Initializers
- [init(scope: CKSyncEngine.SendChangesOptions.Scope, operationGroup: CKOperationGroup?)](cksyncengine-5sie5/sendchangesoptions/init(scope:operationgroup:).md)
  Creates a new set of send changes options.
### Instance Properties
- [var scope: CKSyncEngine.SendChangesOptions.Scope](cksyncengine-5sie5/sendchangesoptions/scope-swift.property.md)
  The scope of the changes to send.
### Enumerations
- [CKSyncEngine.SendChangesOptions.Scope](cksyncengine-5sie5/sendchangesoptions/scope-swift.enum.md)
  The scope for sending changes to the server.
### Default Implementations
- [CustomStringConvertible Implementations](cksyncengine-5sie5/sendchangesoptions/customstringconvertible-implementations.md)

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
- [CKSyncEngine.FetchChangesOptions](cksyncengine-5sie5/fetchchangesoptions.md)
  A set of options to use when fetching changes from the server.
- [func sendChanges(CKSyncEngine.SendChangesOptions) async throws](cksyncengine-5sie5/sendchanges(_:).md)
  Sends pending local changes to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/sendchangesoptions)*