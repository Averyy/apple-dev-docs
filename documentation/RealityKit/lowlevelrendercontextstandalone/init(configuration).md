# init(configuration:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a standalone render context, asynchronously preparing required resources.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated(nonsending)
init(configuration: LowLevelRenderContextStandalone.Configuration) async throws
```

## Discussion

Prefer this overload when creating a single render context. If you need to share prepared resources across multiple contexts, create a [`LowLevelRenderContextStandalone.Resources`](./resources.md) value first and use [`init(configuration:resources:)`](./init%28configuration,resources%29.md) instead.

> **Throws**: An error if resource preparation or context creation fails.

## Parameters

- `configuration`: The configuration for the new context.

## See Also

### Creating a render context
- [init(configuration: LowLevelRenderContextStandalone.Configuration, resources: LowLevelRenderContextStandalone.Resources) throws](./init%28configuration,resources%29.md)
  Creates a standalone render context using resources prepared ahead of time.
- [LowLevelRenderContextStandalone.Configuration](./configuration.md)
  Configuration for creating a standalone render context backed by a Metal device.
- [LowLevelRenderContextStandalone.Resources](./resources.md)
  Resources needed for a render context


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/init(configuration:))*