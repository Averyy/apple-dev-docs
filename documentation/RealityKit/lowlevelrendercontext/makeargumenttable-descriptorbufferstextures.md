# makeArgumentTable(descriptor:buffers:textures:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Creates an argument table that binds the provided buffer slices and textures.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeArgumentTable(descriptor: LowLevelArgumentTable.Descriptor, buffers: [LowLevelBufferSlice], textures: [LowLevelTextureResource]) throws -> LowLevelArgumentTable
```

#### Return Value

A newly created [`LowLevelArgumentTable`](lowlevelargumenttable.md).

#### Discussion

The `descriptor` must match the `argumentTableDescriptor` of the corresponding material function. The counts and sizes of `buffers` and `textures` must match the slots declared in the descriptor.

> **Note**: An error if the counts or sizes of `buffers` or `textures` do not match the descriptor, or if the underlying GPU allocation fails.

## Parameters

- `descriptor`: The argument table layout describing expected buffer and texture slots.
- `buffers`: The buffer slices to bind, in slot order.
- `textures`: The texture resources to bind, in slot order.

## See Also

- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) throws -> sending LowLevelRenderPipelineState](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-7j32p.md)
  Synchronous variant of [`makeRenderPipelineState(descriptor:)`](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-7j32p.md). Blocks the current thread until compilation completes.
- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) async throws -> sending LowLevelRenderPipelineState](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-55ty6.md)
  Asynchronously compiles a Metal render pipeline state from the given descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makeargumenttable(descriptor:buffers:textures:))*