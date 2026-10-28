# init(configuration:renderContext:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a renderer, asynchronously compiling all required GPU resources.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated(nonsending)
convenience init(configuration: LowLevelRenderer.Configuration, renderContext: any LowLevelRenderContext) async throws
```

## Discussion

> **Throws**: An error if GPU resource compilation fails.

## Parameters

- `configuration`: The immutable configuration for this renderer, including output formats and MSAA settings.
- `renderContext`: The render context that provides the Metal device and factory methods.

## See Also

### Creating a renderer
- [LowLevelRenderer.Configuration](./configuration.md)
  The configuration for a renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/init(configuration:rendercontext:))*