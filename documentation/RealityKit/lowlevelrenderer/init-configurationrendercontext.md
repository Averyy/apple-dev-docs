# init(configuration:renderContext:)

**Framework**: RealityKit  
**Kind**: init

Creates a renderer, asynchronously compiling all required GPU resources.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) convenience init(configuration: LowLevelRenderer.Configuration, renderContext: any LowLevelRenderContext) async throws
```

#### Discussion

> **Note**: An error if GPU resource compilation fails.

## Parameters

- `configuration`: The immutable configuration for this renderer, including output formats and MSAA settings.
- `renderContext`: The render context that provides the Metal device and factory methods.

## See Also

- [LowLevelRenderer.Configuration](lowlevelrenderer/configuration.md)
  The immutable configuration for a renderer, established at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/init(configuration:rendercontext:))*