# MTLVisibilityResultMode

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

The mode that determines what, if anything, the GPU writes to the results buffer, after the GPU executes the render pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
enum MTLVisibilityResultMode
```

```c
enum MTLVisibilityResultMode : NSUInteger;
```

## Topics

### Result modes
- [MTLVisibilityResultMode.disabled](./mtlvisibilityresultmode/disabled.md)
  The result doesn’t contain any data because visibility testing was disabled.
- [MTLVisibilityResultMode.boolean](./mtlvisibilityresultmode/boolean.md)
  The result records whether any samples passed depth and stencil tests.
- [MTLVisibilityResultMode.counting](./mtlvisibilityresultmode/counting.md)
  The result records how many samples passed depth and stencil tests.
### Initializers
- [init?(rawValue: UInt)](./mtlvisibilityresultmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [func setVisibilityResultMode(MTLVisibilityResultMode, offset: Int)](./mtlrendercommandencoder/setvisibilityresultmode%28_,offset%29.md)
  Configures which visibility test the GPU runs and the destination for any results it generates.
### Encoding a render pass
- [protocol MTL4RenderCommandEncoder](./mtl4rendercommandencoder.md)
  Encodes configuration and draw commands for a single render pass into a command buffer.
- [protocol MTLRenderCommandEncoder](./mtlrendercommandencoder.md)
  Encodes configuration and draw commands for a single render pass into a command buffer.
- [struct MTL4RenderEncoderOptions](./mtl4renderencoderoptions.md)
  Custom render pass options you specify at encoder creation time.
- [enum MTLTriangleFillMode](./mtltrianglefillmode.md)
  Specifies how to rasterize triangle and triangle strip primitives.
- [enum MTLWinding](./mtlwinding.md)
  The vertex winding rule that determines a front-facing primitive.
- [enum MTLCullMode](./mtlcullmode.md)
  The mode that determines whether to perform culling and which type of primitive to cull.
- [enum MTLPrimitiveType](./mtlprimitivetype.md)
  The geometric primitive type for drawing commands.
- [enum MTLIndexType](./mtlindextype.md)
  The index type for an index buffer that references vertices of geometric primitives.
- [enum MTLDepthClipMode](./mtldepthclipmode.md)
  The mode that determines how to deal with fragments outside of the near or far planes.
- [enum MTLVisibilityResultType](./mtlvisibilityresulttype.md)
  Actions for visibility results between render passes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisibilityresultmode)*