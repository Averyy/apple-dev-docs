# CKSyncEngineConfiguration

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

A type that configures the attributes and behavior of a sync engine.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@interface CKSyncEngineConfiguration : NSObject
```

## Topics

### Creating configurations
- [- initWithDatabase:stateSerialization:delegate:](./cksyncengineconfiguration/initwithdatabase_stateserialization_delegate_.md)
  Creates a configuration for the specified database and serialized state.
### Handling record changes
- [delegate](./cksyncengineconfiguration/delegate.md)
  The object that provides the records to sync and handles any related events.
- [CKSyncEngineDelegate](./cksyncenginedelegate-3c38p.md)
  An interface for providing record data to a sync engine and customizing that engine’s behavior.
### Managing attributes
- [automaticallySync](./cksyncengineconfiguration/automaticallysync.md)
  A Boolean value that determines whether the engine syncs automatically.
- [database](./cksyncengineconfiguration/database.md)
  The associated database.
- [subscriptionID](./cksyncengineconfiguration/subscriptionid.md)
  The subscription identifier for the associated database.
- [stateSerialization](./cksyncengineconfiguration/stateserialization.md)
  The sync engine’s serialized state.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Creating a sync engine
- [- initWithConfiguration:](./cksyncengine-4b4w9/initwithconfiguration_.md)
  Creates a sync engine with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengineconfiguration)*