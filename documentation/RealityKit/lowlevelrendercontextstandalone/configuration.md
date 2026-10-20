# LowLevelRenderContextStandalone.Configuration

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Configuration for creating a standalone render context backed by a Metal device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(device: any MTLDevice)](./configuration/init%28device%29.md)
  Creates a configuration using the given device.
### Configuring the renderer
- [var device: any MTLDevice](./configuration/device.md)
  The Metal device to use for all rendering operations.
- [var memoryOwner: task_id_token_t?](./configuration/memoryowner.md)
  An optional task identity token used to associate GPU memory allocations with a specific process for memory accounting purposes.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a render context
- [init(configuration: LowLevelRenderContextStandalone.Configuration, resources: LowLevelRenderContextStandalone.Resources) throws](./init%28configuration,resources%29.md)
  Creates a standalone render context using resources prepared ahead of time.
- [init(configuration: LowLevelRenderContextStandalone.Configuration) async throws](./init%28configuration%29.md)
  Creates a standalone render context, asynchronously preparing required resources.
- [LowLevelRenderContextStandalone.Resources](./resources.md)
  Resources needed for a render context


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/configuration)*