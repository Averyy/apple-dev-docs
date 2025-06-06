# MTLDrawPrimitivesIndirectArguments

**Framework**: Metal  
**Kind**: struct

The data layout required for drawing primitives via indirect buffer calls.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLDrawPrimitivesIndirectArguments
```

## Mentions

- [Specifying Drawing and Dispatch Arguments Indirectly](specifying-drawing-and-dispatch-arguments-indirectly.md)

#### Overview

See also the [`drawPrimitives(type:indirectBuffer:indirectBufferOffset:)`](mtlrendercommandencoder/drawprimitives(type:indirectbuffer:indirectbufferoffset:).md) method.

## Topics

### Fields
- [init()](mtldrawprimitivesindirectarguments/init.md)
  Returns a new data layout for drawing primitives via indirect buffer calls.
- [init(vertexCount: UInt32, instanceCount: UInt32, vertexStart: UInt32, baseInstance: UInt32)](mtldrawprimitivesindirectarguments/init(vertexcount:instancecount:vertexstart:baseinstance:).md)
  Returns a new data layout for drawing primitives via indirect buffer calls, with specified parameters.
### Instance Properties
- [var baseInstance: UInt32](mtldrawprimitivesindirectarguments/baseinstance.md)
  The first instance to draw.
- [var instanceCount: UInt32](mtldrawprimitivesindirectarguments/instancecount.md)
  The number of instances to draw.
- [var vertexCount: UInt32](mtldrawprimitivesindirectarguments/vertexcount.md)
  The number of vertices to draw.
- [var instanceCount: UInt32](mtldrawprimitivesindirectarguments/instancecount.md)
  The number of instances to draw.
- [var vertexStart: UInt32](mtldrawprimitivesindirectarguments/vertexstart.md)
  The first vertex to draw.
- [var baseInstance: UInt32](mtldrawprimitivesindirectarguments/baseinstance.md)
  The first instance to draw.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol MTLIndirectRenderCommand](mtlindirectrendercommand.md)
  A render command in an indirect command buffer.
- [struct MTLDrawPatchIndirectArguments](mtldrawpatchindirectarguments.md)
  The data layout required for drawing patches via indirect buffer calls.
- [struct MTLDrawIndexedPrimitivesIndirectArguments](mtldrawindexedprimitivesindirectarguments.md)
  The data layout required for drawing indexed primitives via indirect buffer calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawprimitivesindirectarguments)*