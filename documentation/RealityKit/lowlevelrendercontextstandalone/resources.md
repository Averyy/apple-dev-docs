# LowLevelRenderContextStandalone.Resources

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Resources needed for a render context

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Resources
```

## Topics

### Creating render resources
- [init(device: any MTLDevice) async throws](./resources/init%28device%29.md)
  Asynchronously prepare resources for the given device.

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
- [LowLevelRenderContextStandalone.Configuration](./configuration.md)
  Configuration for creating a standalone render context backed by a Metal device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/resources)*