# MTLPrimitiveTopologyClass

**Framework**: Metal  
**Kind**: enum

The primitive topologies available for rendering.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum MTLPrimitiveTopologyClass
```

## Topics

### Constants
- [MTLPrimitiveTopologyClass.unspecified](mtlprimitivetopologyclass/unspecified.md)
  An unspecified primitive.
- [MTLPrimitiveTopologyClass.point](mtlprimitivetopologyclass/point.md)
  A point primitive.
- [MTLPrimitiveTopologyClass.line](mtlprimitivetopologyclass/line.md)
  A line primitive.
- [MTLPrimitiveTopologyClass.triangle](mtlprimitivetopologyclass/triangle.md)
  A triangle primitive.
### Initializers
- [init?(rawValue: UInt)](mtlprimitivetopologyclass/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isAlphaToCoverageEnabled: Bool](mtlrenderpipelinedescriptor/isalphatocoverageenabled.md)
  A Boolean value that indicates whether to read and use the alpha channel fragment output for color attachments to compute a sample coverage mask.
- [var isAlphaToOneEnabled: Bool](mtlrenderpipelinedescriptor/isalphatooneenabled.md)
  A Boolean value that indicates whether to force alpha channel values for color attachments to the largest representable value.
- [var isRasterizationEnabled: Bool](mtlrenderpipelinedescriptor/israsterizationenabled.md)
  A Boolean value that determines whether the pipeline rasterizes primitives.
- [var inputPrimitiveTopology: MTLPrimitiveTopologyClass](mtlrenderpipelinedescriptor/inputprimitivetopology.md)
  The type of primitive topology the pipeline renders.
- [var rasterSampleCount: Int](mtlrenderpipelinedescriptor/rastersamplecount.md)
  The number of samples the pipeline applies for each fragment.
- [var sampleCount: Int](mtlrenderpipelinedescriptor/samplecount.md)
  The number of samples the pipeline applies for each fragment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlprimitivetopologyclass)*