# MTLIndexType

**Framework**: Metal  
**Kind**: enum

The index type for an index buffer that references vertices of geometric primitives.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLIndexType
```

## Topics

### Constants
- [MTLIndexType.uint16](mtlindextype/uint16.md)
  A 16-bit unsigned integer used as a primitive index.
- [MTLIndexType.uint32](mtlindextype/uint32.md)
  A 32-bit unsigned integer used as a primitive index.
### Initializers
- [init?(rawValue: UInt)](mtlindextype/init(rawvalue:).md)

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
- [enum MTLPrimitiveType](mtlprimitivetype.md)
  The geometric primitive type for drawing commands.
- [enum MTLDepthClipMode](mtldepthclipmode.md)
  The mode that determines how to deal with fragments outside of the near or far planes.
- [enum MTLVisibilityResultMode](mtlvisibilityresultmode.md)
  The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.
- [enum MTLVisibilityResultType](mtlvisibilityresulttype.md)
  This enumeration controls if Metal accumulates visibility results between render encoders or resets them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlindextype)*