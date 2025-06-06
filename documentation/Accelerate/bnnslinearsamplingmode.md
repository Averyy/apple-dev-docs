# BNNSLinearSamplingMode

**Framework**: Accelerate  
**Kind**: struct

Constants that specify how a crop-resize layer samples a grid.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSLinearSamplingMode
```

## Topics

### Constants
- [init(UInt32)](bnnslinearsamplingmode/init(_:).md)
- [init(rawValue: UInt32)](bnnslinearsamplingmode/init(rawvalue:).md)
- [var rawValue: UInt32](bnnslinearsamplingmode/rawvalue.md)
- [var BNNSLinearSamplingDefault: BNNSLinearSamplingMode](bnnslinearsamplingdefault.md)
  The default linear sampling mode.
- [var BNNSLinearSamplingAlignCorners: BNNSLinearSamplingMode](bnnslinearsamplingaligncorners.md)
  The align corners sampling mode.
- [var BNNSLinearSamplingUnalignCorners: BNNSLinearSamplingMode](bnnslinearsamplingunaligncorners.md)
  The unalign corners sampling mode.
- [var BNNSLinearSamplingStrictAlignCorners: BNNSLinearSamplingMode](bnnslinearsamplingstrictaligncorners.md)
  The strict align corners sampling mode.
- [var BNNSLinearSamplingOffsetCorners: BNNSLinearSamplingMode](bnnslinearsamplingoffsetcorners.md)
  The offset corners sampling mode.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CropResizeLayer](bnns/cropresizelayer.md)
  A layer object that wraps a crop-resize filter and manages its deinitialization.
- [func BNNSCropResize(UnsafePointer<BNNSLayerParametersCropResize>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresize(_:_:_:_:_:).md)
  Extracts and resizes regions of interest of an input tensor.
- [func BNNSCropResizeBackward(UnsafePointer<BNNSLayerParametersCropResize>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresizebackward(_:_:_:_:_:).md)
  Applies a crop-resize filter backward to generate gradients.
- [struct BNNSLayerParametersCropResize](bnnslayerparameterscropresize.md)
  A set of parameters that describe a crop-resize operation.
- [struct BNNSBoxCoordinateMode](bnnsboxcoordinatemode.md)
  Constants that define the convention to specify the four bounding box coordinates for crop-resize operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslinearsamplingmode)*