# init(configuration:renderContext:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously compiles all shader and pipeline resources for the given configuration and render context.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) init(configuration: LowLevelRenderer.Configuration, renderContext: any LowLevelRenderContext) async throws
```

#### Discussion

> **Note**: An error if shader or pipeline compilation fails.

## Parameters

- `configuration`: The renderer configuration that determines which pipelines to compile.
- `renderContext`: The render context that provides the Metal device and factory methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/resources/init(configuration:rendercontext:))*