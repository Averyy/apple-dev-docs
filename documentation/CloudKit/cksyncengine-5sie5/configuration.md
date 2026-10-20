# CKSyncEngine.Configuration

**Framework**: CloudKit  
**Kind**: struct  
**Role**: Structure

A type that configures the attributes and behavior of a sync engine.

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
struct Configuration
```

## Topics

### Creating configurations
- [init(database: CKDatabase, stateSerialization: CKSyncEngine.State.Serialization?, delegate: any CKSyncEngineDelegate)](./configuration/init%28database,stateserialization,delegate%29.md)
  Creates a configuration for the specified database and serialized state.
### Handling record changes
- [var delegate: any CKSyncEngineDelegate](./configuration/delegate.md)
  The object that provides the records to sync and handles any related events.
- [protocol CKSyncEngineDelegate](../cksyncenginedelegate-1q7g8.md)
  An interface for providing record data to a sync engine and customizing that engine’s behavior.
### Managing attributes
- [var automaticallySync: Bool](./configuration/automaticallysync.md)
  A Boolean value that determines whether the engine syncs automatically.
- [var database: CKDatabase](./configuration/database.md)
  The associated database.
- [var subscriptionID: CKSubscription.ID?](./configuration/subscriptionid.md)
  The subscription identifier for the associated database.
- [var stateSerialization: CKSyncEngine.State.Serialization?](./configuration/stateserialization.md)
  The sync engine’s serialized state.
### Debugging the configuration
- [var description: String](./configuration/description.md)
  A textual description of the configuration that’s suitable for logging.
### Default Implementations
- [CustomStringConvertible Implementations](./configuration/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a sync engine
- [init(CKSyncEngine.Configuration)](./init%28_%29.md)
  Creates a sync engine with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/configuration)*