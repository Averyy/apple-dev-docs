# BNNSLayerParametersResize

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a resize layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct BNNSLayerParametersResize
```

## Topics

### Initializers
- [init(method: BNNSInterpolationMethod, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, align_corners: Bool)](bnnslayerparametersresize/init(method:i_desc:o_desc:align_corners:).md)
  Returns a new resize-layer parameters structure from the specified parameters.
- [init()](bnnslayerparametersresize/init.md)
  Returns a new resize-layer parameters structure.
### Instance Properties
- [var method: BNNSInterpolationMethod](bnnslayerparametersresize/method.md)
  The interpolation method for resizing.
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersresize/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersresize/o_desc.md)
  The descriptor of the output.
- [var align_corners: Bool](bnnslayerparametersresize/align_corners.md)
  A Boolean value that specifies whether to align the corners of the upscaling grid to the center of scaling dimensions instead of to the edges.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class ResizeLayer](bnns/resizelayer.md)
  A layer object that wraps a resize filter and manages its deinitialization.
- [struct BNNSInterpolationMethod](bnnsinterpolationmethod.md)
  Constants that describe interpolation methods.
- [func BNNSFilterCreateLayerResize(UnsafePointer<BNNSLayerParametersResize>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerresize(_:_:).md)
  Returns a new resize layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersresize)*