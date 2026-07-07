# makeRenderPipelineState(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Synchronous variant of [`makeRenderPipelineState(descriptor:)`](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-7j32p.md). Blocks the current thread until compilation completes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) throws -> sending LowLevelRenderPipelineState
```

## See Also

- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) async throws -> sending LowLevelRenderPipelineState](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-55ty6.md)
  Asynchronously compiles a Metal render pipeline state from the given descriptor.
- [func makeArgumentTable(descriptor: LowLevelArgumentTable.Descriptor, buffers: [LowLevelBufferSlice], textures: [LowLevelTextureResource]) throws -> LowLevelArgumentTable](lowlevelrendercontext/makeargumenttable(descriptor:buffers:textures:).md)
  Creates an argument table that binds the provided buffer slices and textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makerenderpipelinestate(descriptor:)-7j32p)*