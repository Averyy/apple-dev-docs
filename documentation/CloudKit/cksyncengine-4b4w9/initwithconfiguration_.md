# initWithConfiguration:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a sync engine with the specified configuration.

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
- (instancetype) initWithConfiguration:(CKSyncEngineConfiguration *) configuration;
```

#### Return Value

A configured sync engine.

## Parameters

- `configuration`: The attributes of the new sync engine, such as the associated database and the object to use as the engine’s delegate. For more information, see [`CKSyncEngineConfiguration`](../cksyncengineconfiguration.md).

## See Also

### Creating a sync engine
- [CKSyncEngineConfiguration](../cksyncengineconfiguration.md)
  A type that configures the attributes and behavior of a sync engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncengine-4b4w9/initwithconfiguration:)*