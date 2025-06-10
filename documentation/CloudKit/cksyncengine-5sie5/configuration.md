# CKSyncEngine.Configuration

**Framework**: CloudKit  
**Kind**: struct

A type that configures the attributes and behavior of a sync engine.

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
struct Configuration
```

## Topics

### Creating configurations
- [init(database: CKDatabase, stateSerialization: CKSyncEngine.State.Serialization?, delegate: any CKSyncEngineDelegate)](cksyncengine-5sie5/configuration/init(database:stateserialization:delegate:).md)
  Creates a configuration for the specified database and serialized state.
### Handling record changes
- [var delegate: any CKSyncEngineDelegate](cksyncengine-5sie5/configuration/delegate.md)
  The object that provides the records to sync and handles any related events.
- [protocol CKSyncEngineDelegate](cksyncenginedelegate-1q7g8.md)
  An interface for providing record data to a sync engine and customizing that engine’s behavior.
### Managing attributes
- [var automaticallySync: Bool](cksyncengine-5sie5/configuration/automaticallysync.md)
  A Boolean value that determines whether the engine syncs automatically.
- [var database: CKDatabase](cksyncengine-5sie5/configuration/database.md)
  The associated database.
- [var subscriptionID: CKSubscription.ID?](cksyncengine-5sie5/configuration/subscriptionid.md)
  The subscription identifier for the associated database.
- [var stateSerialization: CKSyncEngine.State.Serialization?](cksyncengine-5sie5/configuration/stateserialization.md)
  The sync engine’s serialized state.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(CKSyncEngine.Configuration)](cksyncengine-5sie5/init(_:).md)
  Creates a sync engine with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-5sie5/configuration)*