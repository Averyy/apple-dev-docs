# isAlphaToCoverageEnabled

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isAlphaToCoverageEnabled: Bool { get set }
```

```objc
@property (nonatomic, readwrite, getter=isAlphaToCoverageEnabled) BOOL alphaToCoverageEnabled;
```

#### Discussion

The default value is [`false`](../../Swift/false.md).

## See Also

### Specifying rasterization and visibility state
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
- [var sampleCount: Int](./samplecount.md)
  The number of samples the pipeline applies for each fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor/isalphatocoverageenabled)*