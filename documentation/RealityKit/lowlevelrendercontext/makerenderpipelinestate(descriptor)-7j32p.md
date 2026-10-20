# makeRenderPipelineState(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Synchronous variant of [`makeRenderPipelineState(descriptor:)`](./makerenderpipelinestate%28descriptor%29-7j32p.md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) throws -> sending LowLevelRenderPipelineState
```

**Other overloads**:

```swift
nonisolated
(nonsending) func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) async throws -> sending LowLevelRenderPipelineState
```

## See Also

### Creating pipeline state
- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) async throws -> sending LowLevelRenderPipelineState](./makerenderpipelinestate%28descriptor%29-55ty6.md)
  Asynchronously compiles a Metal render pipeline state from the given descriptor.
- [func makeArgumentTable(descriptor: LowLevelArgumentTable.Descriptor, buffers: [LowLevelBufferSlice], textures: [LowLevelTextureResource]) throws -> LowLevelArgumentTable](./makeargumenttable%28descriptor,buffers,textures%29.md)
  Creates an argument table that binds the provided buffer slices and textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makerenderpipelinestate(descriptor:)-7j32p)*