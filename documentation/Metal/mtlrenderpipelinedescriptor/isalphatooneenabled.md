# isAlphaToOneEnabled

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isAlphaToOneEnabled: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isAlphaToOneEnabled) BOOL alphaToOneEnabled;
```

## Discussion

The default value is [`false`](../../Swift/false.md).

If enabled, alpha channel fragment values are only forced for `colorAttachments[0]`. Other attachments are unaffected.

You may use `alphaToOneEnabled` when you want to write an alpha value that represents partial coverage of the pixel, but also want to disable blending (by forcing alpha to one).

## See Also

### Specifying rasterization and visibility state
- [var isAlphaToCoverageEnabled: Bool](./isalphatocoverageenabled.md)
  A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [var isRasterizationEnabled: Bool](./israsterizationenabled.md)
  A Boolean value that determines whether the pipeline rasterizes primitives.
- [var inputPrimitiveTopology: MTLPrimitiveTopologyClass](./inputprimitivetopology.md)
  The type of primitive topology the pipeline renders.
- [var rasterSampleCount: Int](./rastersamplecount.md)
  The number of samples the pipeline applies for each fragment.
- [enum MTLPrimitiveTopologyClass](../mtlprimitivetopologyclass.md)
  The primitive topologies available for rendering.
- [var sampleCount: Int](./samplecount.md)
  The number of samples the pipeline applies for each fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/isalphatooneenabled)*