# BNNSCropResizeBackward(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a crop-resize filter backward to generate gradients.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func BNNSCropResizeBackward(_ layer_params: UnsafePointer<BNNSLayerParametersCropResize>, _ in_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ roi: UnsafePointer<BNNSNDArrayDescriptor>, _ out_delta: UnsafePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

## Parameters

- `layer_params`: A pointer to the layer parameters.
- `in_delta`: A pointer to the input delta descriptor.
- `roi`: A pointer to the regions of interest array descriptor.
- `out_delta`: A pointer to the output delta descriptor.
- `filter_params`: Runtime filter parameters.

## See Also

- [class CropResizeLayer](bnns/cropresizelayer.md)
  A layer object that wraps a crop-resize filter and manages its deinitialization.
- [func BNNSCropResize(UnsafePointer<BNNSLayerParametersCropResize>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresize(_:_:_:_:_:).md)
  Extracts and resizes regions of interest of an input tensor.
- [struct BNNSLayerParametersCropResize](bnnslayerparameterscropresize.md)
  A set of parameters that describe a crop-resize operation.
- [struct BNNSBoxCoordinateMode](bnnsboxcoordinatemode.md)
  Constants that define the convention to specify the four bounding box coordinates for crop-resize operations.
- [struct BNNSLinearSamplingMode](bnnslinearsamplingmode.md)
  Constants that specify how a crop-resize layer samples a grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnscropresizebackward(_:_:_:_:_:))*