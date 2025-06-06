# rasterSampleCount

**Framework**: Metal  
**Kind**: property

The number of samples the pipeline applies for each fragment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var rasterSampleCount: Int { get set }
```

#### Discussion

The render pipeline state honors this property only if the pipeline render targets support multisampling.

> ❗ **Important**:  This property needs to be `1` if the render targets don’t support multisampling.

 This property needs to be `1` if the render targets don’t support multisampling.

When your create an [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) instance, this property’s value needs to be equal to the number of render target textures. Furthermore, the texture type of all render target textures must be [`MTLTextureType.type2DMultisample`](mtltexturetype/type2dmultisample.md).

The number of samples a GPU supports varies by device. You can check whether an [`MTLDevice`](mtldevice.md) instance supports a specific sample count by calling its [`supportsTextureSampleCount(_:)`](mtldevice/supportstexturesamplecount(_:).md) method.

The default value for this property is `1`.

## See Also

- [var isAlphaToCoverageEnabled: Bool](mtlrenderpipelinedescriptor/isalphatocoverageenabled.md)
  A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [var isAlphaToOneEnabled: Bool](mtlrenderpipelinedescriptor/isalphatooneenabled.md)
  A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [var isRasterizationEnabled: Bool](mtlrenderpipelinedescriptor/israsterizationenabled.md)
  A Boolean value that determines whether the pipeline rasterizes primitives.
- [var inputPrimitiveTopology: MTLPrimitiveTopologyClass](mtlrenderpipelinedescriptor/inputprimitivetopology.md)
  The type of primitive topology the pipeline renders.
- [enum MTLPrimitiveTopologyClass](mtlprimitivetopologyclass.md)
  The primitive topologies available for rendering.
- [var sampleCount: Int](mtlrenderpipelinedescriptor/samplecount.md)
  The number of samples the pipeline applies for each fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/rastersamplecount)*