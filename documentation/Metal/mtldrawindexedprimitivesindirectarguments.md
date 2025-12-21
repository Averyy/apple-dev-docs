# MTLDrawIndexedPrimitivesIndirectArguments

**Framework**: Metal  
**Kind**: struct

The data layout required for drawing indexed primitives via indirect buffer calls.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLDrawIndexedPrimitivesIndirectArguments
```

## Mentions

- [Specifying drawing and dispatch arguments indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md)

#### Overview

See also the [`drawIndexedPrimitives(type:indexType:indexBuffer:indexBufferOffset:indirectBuffer:indirectBufferOffset:)`](mtlrendercommandencoder/drawindexedprimitives(type:indextype:indexbuffer:indexbufferoffset:indirectbuffer:indirectbufferoffset:).md) method.

## Topics

### Initializers
- [init()](mtldrawindexedprimitivesindirectarguments/init.md)
  Returns a new data layout for drawing indexed primitives via indirect buffer calls.
- [init(indexCount: UInt32, instanceCount: UInt32, indexStart: UInt32, baseVertex: Int32, baseInstance: UInt32)](mtldrawindexedprimitivesindirectarguments/init(indexcount:instancecount:indexstart:basevertex:baseinstance:).md)
  Returns a new data layout for drawing indexed primitives via indirect buffer calls, with specified parameters.
### Instance Properties
- [var baseInstance: UInt32](mtldrawindexedprimitivesindirectarguments/baseinstance.md)
  The first instance to draw.
- [var baseVertex: Int32](mtldrawindexedprimitivesindirectarguments/basevertex.md)
  The first vertex to draw.
- [var indexCount: UInt32](mtldrawindexedprimitivesindirectarguments/indexcount.md)
  For each instance, the number of indices to read from the index buffer.
- [var indexStart: UInt32](mtldrawindexedprimitivesindirectarguments/indexstart.md)
  The first index to draw.
- [var instanceCount: UInt32](mtldrawindexedprimitivesindirectarguments/instancecount.md)
  The number of instances to draw.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLIndirectRenderCommand](mtlindirectrendercommand.md)
  A render command in an indirect command buffer.
- [struct MTLDrawPatchIndirectArguments](mtldrawpatchindirectarguments.md)
  The data layout required for drawing patches via indirect buffer calls.
- [struct MTLDrawPrimitivesIndirectArguments](mtldrawprimitivesindirectarguments.md)
  The data layout required for drawing primitives via indirect buffer calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawindexedprimitivesindirectarguments)*