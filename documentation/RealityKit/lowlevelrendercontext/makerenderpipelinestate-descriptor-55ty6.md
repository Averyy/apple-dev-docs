# makeRenderPipelineState(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Asynchronously compiles a Metal render pipeline state from the given descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) async throws -> sending LowLevelRenderPipelineState
```

#### Return Value

A compiled [`LowLevelRenderPipelineState`](lowlevelrenderpipelinestate.md).

#### Discussion

The descriptor’s mesh format, material, and render target configuration are baked into the pipeline at compile time. Create pipeline states once and reuse them across frames.

> **Note**: An error if pipeline compilation fails.

## Parameters

- `descriptor`: The mesh descriptor, material, render targets, and optional blending configuration.

## See Also

- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) throws -> sending LowLevelRenderPipelineState](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-7j32p.md)
  Synchronous variant of [`makeRenderPipelineState(descriptor:)`](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-7j32p.md). Blocks the current thread until compilation completes.
- [func makeArgumentTable(descriptor: LowLevelArgumentTable.Descriptor, buffers: [LowLevelBufferSlice], textures: [LowLevelTextureResource]) throws -> LowLevelArgumentTable](lowlevelrendercontext/makeargumenttable(descriptor:buffers:textures:).md)
  Creates an argument table that binds the provided buffer slices and textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makerenderpipelinestate(descriptor:)-55ty6)*