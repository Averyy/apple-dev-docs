# LowLevelRenderContextStandalone.Resources

**Framework**: RealityKit  
**Kind**: struct

Pre-compiled shader and pipeline resources shared across multiple render context instances.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Resources
```

## Topics

### Creating render resources
- [init(device: any MTLDevice) async throws](lowlevelrendercontextstandalone/resources/init(device:).md)
  Asynchronously compiles the shared shader and pipeline resources for the given device.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(configuration: LowLevelRenderContextStandalone.Configuration, resources: LowLevelRenderContextStandalone.Resources) throws](lowlevelrendercontextstandalone/init(configuration:resources:).md)
  Creates a standalone render context using pre-compiled shader and pipeline resources.
- [init(configuration: LowLevelRenderContextStandalone.Configuration) async throws](lowlevelrendercontextstandalone/init(configuration:).md)
  Creates a standalone render context, asynchronously compiling all required shader and pipeline resources.
- [LowLevelRenderContextStandalone.Configuration](lowlevelrendercontextstandalone/configuration.md)
  Configuration for creating a standalone render context backed by a Metal device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/resources)*