# LowLevelRenderContextStandalone.Configuration

**Framework**: RealityKit  
**Kind**: struct

Configuration for creating a standalone render context backed by a Metal device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Configuration
```

## Topics

### Creating a configuration
- [init(device: any MTLDevice)](lowlevelrendercontextstandalone/configuration/init(device:).md)
  Creates a configuration using the given device.
### Configuring the renderer
- [var device: any MTLDevice](lowlevelrendercontextstandalone/configuration/device.md)
  The Metal device to use for all rendering operations.
- [var memoryOwner: task_id_token_t?](lowlevelrendercontextstandalone/configuration/memoryowner.md)
  An optional task identity token used to associate GPU memory allocations with a specific process for memory accounting purposes.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init(configuration: LowLevelRenderContextStandalone.Configuration, resources: LowLevelRenderContextStandalone.Resources) throws](lowlevelrendercontextstandalone/init(configuration:resources:).md)
  Creates a standalone render context using resources prepared ahead of time.
- [init(configuration: LowLevelRenderContextStandalone.Configuration) async throws](lowlevelrendercontextstandalone/init(configuration:).md)
  Creates a standalone render context, asynchronously preparing required resources.
- [LowLevelRenderContextStandalone.Resources](lowlevelrendercontextstandalone/resources.md)
  Resources needed for a render context


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/configuration)*