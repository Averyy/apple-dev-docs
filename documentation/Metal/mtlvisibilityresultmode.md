# MTLVisibilityResultMode

**Framework**: Metal  
**Kind**: enum

The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
enum MTLVisibilityResultMode
```

## Topics

### Constants
- [MTLVisibilityResultMode.disabled](mtlvisibilityresultmode/disabled.md)
  The result doesn’t contain any data because visibility testing was disabled.
- [MTLVisibilityResultMode.boolean](mtlvisibilityresultmode/boolean.md)
  The result records whether any samples passed depth and stencil tests.
- [MTLVisibilityResultMode.counting](mtlvisibilityresultmode/counting.md)
  The result records how many samples passed depth and stencil tests.
### Initializers
- [init?(rawValue: UInt)](mtlvisibilityresultmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func setVisibilityResultMode(MTLVisibilityResultMode, offset: Int)](mtlrendercommandencoder/setvisibilityresultmode(_:offset:).md)
  Configures which visibility test the GPU runs and the destination for any results it generates.
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
- [enum MTLIndexType](mtlindextype.md)
  The index type for an index buffer that references vertices of geometric primitives.
- [enum MTLDepthClipMode](mtldepthclipmode.md)
  The mode that determines how to deal with fragments outside of the near or far planes.
- [enum MTLVisibilityResultType](mtlvisibilityresulttype.md)
  This enumeration controls if Metal accumulates visibility results between render encoders or resets them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode)*