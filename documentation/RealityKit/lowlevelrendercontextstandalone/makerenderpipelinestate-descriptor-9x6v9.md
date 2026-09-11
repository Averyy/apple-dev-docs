# makeRenderPipelineState(descriptor:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously compiles a Metal render pipeline state from the given descriptor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
(nonsending) final func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) async throws -> sending LowLevelRenderPipelineState
```

#### Return Value

A compiled [`LowLevelRenderPipelineState`](lowlevelrenderpipelinestate.md).

#### Discussion

The descriptor’s mesh format, material, and render target configuration are baked into the pipeline at compile time. Create pipeline states once and reuse them across frames.

> **Note**: An error if pipeline compilation fails.

## Parameters

- `descriptor`: The mesh descriptor, material, render targets, and optional blending configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makerenderpipelinestate(descriptor:)-9x6v9)*