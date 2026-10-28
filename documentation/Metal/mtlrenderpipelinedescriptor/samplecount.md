# sampleCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The number of samples the pipeline applies for each fragment.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`rasterSampleCount`](./rastersamplecount.md) instead.

## Declaration

```swift
var sampleCount: Int { get set }
```

```objc
@property (nonatomic, readwrite) NSUInteger sampleCount;
```

## Discussion

The render pipeline state honors this property only if the pipeline render targets support multisampling.

> ❗ **Important**:  This property needs to be `1` if the render targets don’t support multisampling.

When your create an [`MTLRenderCommandEncoder`](../mtlrendercommandencoder.md) instance, this property’s value needs to be equal to the number of render target textures. Furthermore, the texture type of all render target textures need to be [`MTLTextureType.type2DMultisample`](../mtltexturetype/type2dmultisample.md).

The number of samples a GPU supports varies by device. You can check whether an [`MTLDevice`](../mtldevice.md) instance supports a specific sample count by calling its [`supportsTextureSampleCount(_:)`](../mtldevice/supportstexturesamplecount%28_%29.md) method.

The default value for this property is `1`.

## See Also

### Specifying rasterization and visibility state
- [var isAlphaToCoverageEnabled: Bool](./isalphatocoverageenabled.md)
  A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [var isAlphaToOneEnabled: Bool](./isalphatooneenabled.md)
  A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [var isRasterizationEnabled: Bool](./israsterizationenabled.md)
  A Boolean value that determines whether the pipeline rasterizes primitives.
- [var inputPrimitiveTopology: MTLPrimitiveTopologyClass](./inputprimitivetopology.md)
  The type of primitive topology the pipeline renders.
- [var rasterSampleCount: Int](./rastersamplecount.md)
  The number of samples the pipeline applies for each fragment.
- [enum MTLPrimitiveTopologyClass](../mtlprimitivetopologyclass.md)
  The primitive topologies available for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/samplecount)*