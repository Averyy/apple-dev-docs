# inputPrimitiveTopology

**Framework**: Metal  
**Kind**: property

The type of primitive topology the pipeline renders.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var inputPrimitiveTopology: MTLPrimitiveTopologyClass { get set }
```

## Mentions

- [Rendering to Multiple Texture Slices in a Draw Command](rendering-to-multiple-texture-slices-in-a-draw-command.md)

#### Discussion

Your app must specify this value when layered rendering is enabled.

The default value is `MTLPrimitiveTopologyClassUnspecified`.

## See Also

- [var renderTargetArrayLength: Int](mtlrenderpassdescriptor/rendertargetarraylength.md)
  The number of active layers that all attachments must have for layered rendering.
- [var isAlphaToCoverageEnabled: Bool](mtlrenderpipelinedescriptor/isalphatocoverageenabled.md)
  A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [var isAlphaToOneEnabled: Bool](mtlrenderpipelinedescriptor/isalphatooneenabled.md)
  A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [var isRasterizationEnabled: Bool](mtlrenderpipelinedescriptor/israsterizationenabled.md)
  A Boolean value that determines whether the pipeline rasterizes primitives.
- [var rasterSampleCount: Int](mtlrenderpipelinedescriptor/rastersamplecount.md)
  The number of samples the pipeline applies for each fragment.
- [enum MTLPrimitiveTopologyClass](mtlprimitivetopologyclass.md)
  The primitive topologies available for rendering.
- [var sampleCount: Int](mtlrenderpipelinedescriptor/samplecount.md)
  The number of samples the pipeline applies for each fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/inputprimitivetopology)*