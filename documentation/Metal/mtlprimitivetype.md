# MTLPrimitiveType

**Framework**: Metal  
**Kind**: enum

The geometric primitive type for drawing commands.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLPrimitiveType
```

## Topics

### Constants
- [MTLPrimitiveType.point](mtlprimitivetype/point.md)
  Rasterize a point at each vertex. The vertex shader must provide `[[point_size]]`, or the point size is undefined.
- [MTLPrimitiveType.line](mtlprimitivetype/line.md)
  Rasterize a line between each separate pair of vertices, resulting in a series of unconnected lines. If there are an odd number of vertices, the last vertex is ignored.
- [MTLPrimitiveType.lineStrip](mtlprimitivetype/linestrip.md)
  Rasterize a line between each pair of adjacent vertices, resulting in a series of connected lines (also called a polyline).
- [MTLPrimitiveType.triangle](mtlprimitivetype/triangle.md)
  For every separate set of three vertices, rasterize a triangle. If the number of vertices is not a multiple of three, either one or two vertices is ignored.
- [MTLPrimitiveType.triangleStrip](mtlprimitivetype/trianglestrip.md)
  For every three adjacent vertices, rasterize a triangle.
### Initializers
- [init?(rawValue: UInt)](mtlprimitivetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MTL4RenderCommandEncoder](mtl4rendercommandencoder.md)
  Encodes a render pass into a command buffer, including all its draw calls and configuration.
- [protocol MTLRenderCommandEncoder](mtlrendercommandencoder.md)
  An interface that encodes a render pass into a command buffer, including all its draw calls and configuration.
- [struct MTL4RenderEncoderOptions](mtl4renderencoderoptions.md)
  Custom render pass options you specify at encoder creation time.
- [enum MTLTriangleFillMode](mtltrianglefillmode.md)
  Specifies how to rasterize triangle and triangle strip primitives.
- [enum MTLWinding](mtlwinding.md)
  The vertex winding rule that determines a front-facing primitive.
- [enum MTLCullMode](mtlcullmode.md)
  The mode that determines whether to perform culling and which type of primitive to cull.
- [enum MTLIndexType](mtlindextype.md)
  The index type for an index buffer that references vertices of geometric primitives.
- [enum MTLDepthClipMode](mtldepthclipmode.md)
  The mode that determines how to deal with fragments outside of the near or far planes.
- [enum MTLVisibilityResultMode](mtlvisibilityresultmode.md)
  The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.
- [enum MTLVisibilityResultType](mtlvisibilityresulttype.md)
  This enumeration controls if Metal accumulates visibility results between render encoders or resets them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlprimitivetype)*