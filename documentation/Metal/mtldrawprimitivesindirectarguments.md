# MTLDrawPrimitivesIndirectArguments

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

The data layout required for drawing primitives via indirect buffer calls.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MTLDrawPrimitivesIndirectArguments
```

```c
typedef struct { ... } MTLDrawPrimitivesIndirectArguments;
```

## Mentions

- [Specifying drawing and dispatch arguments indirectly](./specifying-drawing-and-dispatch-arguments-indirectly.md)

#### Overview

See also the [`drawPrimitives(type:indirectBuffer:indirectBufferOffset:)`](./mtlrendercommandencoder/drawprimitives%28type,indirectbuffer,indirectbufferoffset%29.md) method.

## Topics

### Initializers
- [init()](./mtldrawprimitivesindirectarguments/init%28%29.md)
  Returns a new data layout for drawing primitives via indirect buffer calls.
- [init(vertexCount: UInt32, instanceCount: UInt32, vertexStart: UInt32, baseInstance: UInt32)](./mtldrawprimitivesindirectarguments/init%28vertexcount,instancecount,vertexstart,baseinstance%29.md)
  Returns a new data layout for drawing primitives via indirect buffer calls, with specified parameters.
### Instance Properties
- [var baseInstance: UInt32](./mtldrawprimitivesindirectarguments/baseinstance.md)
  The first instance to draw.
- [var instanceCount: UInt32](./mtldrawprimitivesindirectarguments/instancecount.md)
  The number of instances to draw.
- [var vertexCount: UInt32](./mtldrawprimitivesindirectarguments/vertexcount.md)
  The number of vertices to draw.
- [var vertexStart: UInt32](./mtldrawprimitivesindirectarguments/vertexstart.md)
  The first vertex to draw.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Render compute commands
- [protocol MTLIndirectRenderCommand](./mtlindirectrendercommand.md)
  A render command in an indirect command buffer.
- [struct MTLDrawPatchIndirectArguments](./mtldrawpatchindirectarguments.md)
  The data layout required for drawing patches via indirect buffer calls.
- [struct MTLDrawIndexedPrimitivesIndirectArguments](./mtldrawindexedprimitivesindirectarguments.md)
  The data layout required for drawing indexed primitives via indirect buffer calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawprimitivesindirectarguments)*