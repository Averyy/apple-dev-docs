# BNNSLayerParametersCropResize

**Framework**: Accelerate  
**Kind**: struct

A set of parameters that describe a crop-resize operation.

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
struct BNNSLayerParametersCropResize
```

## Topics

### Initializers
- [init(normalized_coordinates: Bool, spatial_scale: Float, extrapolation_value: Float, sampling_mode: BNNSLinearSamplingMode, box_coordinate_mode: BNNSBoxCoordinateMode, method: BNNSInterpolationMethod)](bnnslayerparameterscropresize/init(normalized_coordinates:spatial_scale:extrapolation_value:sampling_mode:box_coordinate_mode:method:).md)
  Creates a new layer parameters structure.
- [init()](bnnslayerparameterscropresize/init.md)
  Creates a new empty layer parameters structure.
### Instance Properties
- [var normalized_coordinates: Bool](bnnslayerparameterscropresize/normalized_coordinates.md)
  A Boolean value that specifies whether the operation treats the coordinates as normalized to `0...1`.
- [var spatial_scale: Float](bnnslayerparameterscropresize/spatial_scale.md)
  An additional spatial scale that mutliplies the bounding box coordinates.
- [var extrapolation_value: Float](bnnslayerparameterscropresize/extrapolation_value.md)
  A value that the operation uses for extrapolation. Default value is `0`.
- [var sampling_mode: BNNSLinearSamplingMode](bnnslayerparameterscropresize/sampling_mode.md)
  The sampling mode that the operation uses to select sample points.
- [var box_coordinate_mode: BNNSBoxCoordinateMode](bnnslayerparameterscropresize/box_coordinate_mode.md)
  A constant that defines the convention that the operation uses to specify the four bounding box coordinates.
- [var method: BNNSInterpolationMethod](bnnslayerparameterscropresize/method.md)
  The interpolation method.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class CropResizeLayer](bnns/cropresizelayer.md)
  A layer object that wraps a crop-resize filter and manages its deinitialization.
- [func BNNSCropResize(UnsafePointer<BNNSLayerParametersCropResize>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresize(_:_:_:_:_:).md)
  Extracts and resizes regions of interest of an input tensor.
- [func BNNSCropResizeBackward(UnsafePointer<BNNSLayerParametersCropResize>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresizebackward(_:_:_:_:_:).md)
  Applies a crop-resize filter backward to generate gradients.
- [struct BNNSBoxCoordinateMode](bnnsboxcoordinatemode.md)
  Constants that define the convention to specify the four bounding box coordinates for crop-resize operations.
- [struct BNNSLinearSamplingMode](bnnslinearsamplingmode.md)
  Constants that specify how a crop-resize layer samples a grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterscropresize)*