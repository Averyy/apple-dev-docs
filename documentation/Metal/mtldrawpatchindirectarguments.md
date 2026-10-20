# MTLDrawPatchIndirectArguments

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

The data layout required for drawing patches via indirect buffer calls.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MTLDrawPatchIndirectArguments
```

```c
typedef struct { ... } MTLDrawPatchIndirectArguments;
```

## Mentions

- [Specifying drawing and dispatch arguments indirectly](./specifying-drawing-and-dispatch-arguments-indirectly.md)

#### Overview

See also the following methods:

- [`drawPatches(numberOfPatchControlPoints:patchIndexBuffer:patchIndexBufferOffset:indirectBuffer:indirectBufferOffset:)`](./mtlrendercommandencoder/drawpatches%28numberofpatchcontrolpoints,patchindexbuffer,patchindexbufferoffset,indirectbuffer,indirectbufferoffset%29.md)
- [`drawIndexedPatches(numberOfPatchControlPoints:patchIndexBuffer:patchIndexBufferOffset:controlPointIndexBuffer:controlPointIndexBufferOffset:indirectBuffer:indirectBufferOffset:)`](./mtlrendercommandencoder/drawindexedpatches%28numberofpatchcontrolpoints,patchindexbuffer,patchindexbufferoffset,controlpointindexbuffer,controlpointindexbufferoffset,indirectbuffer,indirectbufferoffset%29.md)

## Topics

### Initializers
- [init()](./mtldrawpatchindirectarguments/init%28%29.md)
  Returns a new data layout for drawing patches via indirect buffer calls.
- [init(patchCount: UInt32, instanceCount: UInt32, patchStart: UInt32, baseInstance: UInt32)](./mtldrawpatchindirectarguments/init%28patchcount,instancecount,patchstart,baseinstance%29.md)
  Returns a new data layout for drawing patches via indirect buffer calls, with specified parameters.
### Instance Properties
- [var baseInstance: UInt32](./mtldrawpatchindirectarguments/baseinstance.md)
  The first instance to draw.
- [var instanceCount: UInt32](./mtldrawpatchindirectarguments/instancecount.md)
  The number of instances to draw.
- [var patchCount: UInt32](./mtldrawpatchindirectarguments/patchcount.md)
  The number of patches in each instance.
- [var patchStart: UInt32](./mtldrawpatchindirectarguments/patchstart.md)
  The patch start index.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Render compute commands
- [protocol MTLIndirectRenderCommand](./mtlindirectrendercommand.md)
  A render command in an indirect command buffer.
- [struct MTLDrawPrimitivesIndirectArguments](./mtldrawprimitivesindirectarguments.md)
  The data layout required for drawing primitives via indirect buffer calls.
- [struct MTLDrawIndexedPrimitivesIndirectArguments](./mtldrawindexedprimitivesindirectarguments.md)
  The data layout required for drawing indexed primitives via indirect buffer calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawpatchindirectarguments)*