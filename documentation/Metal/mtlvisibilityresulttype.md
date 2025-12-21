# MTLVisibilityResultType

**Framework**: Metal  
**Kind**: enum

This enumeration controls if Metal accumulates visibility results between render encoders or resets them.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum MTLVisibilityResultType
```

#### Overview

You can specify this property for `MTLRenderCommandEncoders` and for `MTL4RenderCommandEncoders` through their descriptors’ `MTLRenderCommandEncoder/visibilityResultType` and `MTL4RenderCommandEncoder/visibilityResultType` methods.

## Topics

### Enumeration Cases
- [MTLVisibilityResultType.accumulate](mtlvisibilityresulttype/accumulate.md)
  Accumulate visibility results data across multiple render passes.
- [MTLVisibilityResultType.reset](mtlvisibilityresulttype/reset.md)
  Reset visibility result data when you create a render command encoder.
### Initializers
- [init?(rawValue: Int)](mtlvisibilityresulttype/init(rawvalue:).md)

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
  Encodes configuration and draw commands for a single render pass into a command buffer.
- [protocol MTLRenderCommandEncoder](mtlrendercommandencoder.md)
  Encodes configuration and draw commands for a single render pass into a command buffer.
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
- [enum MTLIndexType](mtlindextype.md)
  The index type for an index buffer that references vertices of geometric primitives.
- [enum MTLDepthClipMode](mtldepthclipmode.md)
  The mode that determines how to deal with fragments outside of the near or far planes.
- [enum MTLVisibilityResultMode](mtlvisibilityresultmode.md)
  The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisibilityresulttype)*