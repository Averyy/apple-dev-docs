# BNNSLinearSamplingMode

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that specify how a crop-resize layer samples a grid.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSLinearSamplingMode
```

```c
typedef enum { ... } BNNSLinearSamplingMode;
```

## Topics

### Constants
- [init(UInt32)](./bnnslinearsamplingmode/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnslinearsamplingmode/init%28rawvalue%29.md)
- [var rawValue: UInt32](./bnnslinearsamplingmode/rawvalue.md)
- [var BNNSLinearSamplingDefault: BNNSLinearSamplingMode](./bnnslinearsamplingdefault.md)
  The default linear sampling mode.
- [var BNNSLinearSamplingAlignCorners: BNNSLinearSamplingMode](./bnnslinearsamplingaligncorners.md)
  The align corners sampling mode.
- [var BNNSLinearSamplingUnalignCorners: BNNSLinearSamplingMode](./bnnslinearsamplingunaligncorners.md)
  The unalign corners sampling mode.
- [var BNNSLinearSamplingStrictAlignCorners: BNNSLinearSamplingMode](./bnnslinearsamplingstrictaligncorners.md)
  The strict align corners sampling mode.
- [var BNNSLinearSamplingOffsetCorners: BNNSLinearSamplingMode](./bnnslinearsamplingoffsetcorners.md)
  The offset corners sampling mode.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Crop-resize layers
- [class CropResizeLayer](./bnns/cropresizelayer.md)
  A layer object that wraps a crop-resize filter and manages its deinitialization.
- [func BNNSCropResize(UnsafePointer<BNNSLayerParametersCropResize>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnscropresize%28_,_,_,_,_%29.md)
  Extracts and resizes regions of interest of an input tensor.
- [func BNNSCropResizeBackward(UnsafePointer<BNNSLayerParametersCropResize>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnscropresizebackward%28_,_,_,_,_%29.md)
  Applies a crop-resize filter backward to generate gradients.
- [struct BNNSLayerParametersCropResize](./bnnslayerparameterscropresize.md)
  A set of parameters that describe a crop-resize operation.
- [struct BNNSBoxCoordinateMode](./bnnsboxcoordinatemode.md)
  Constants that define the convention to specify the four bounding box coordinates for crop-resize operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslinearsamplingmode)*