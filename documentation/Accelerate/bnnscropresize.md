# BNNSCropResize(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Extracts and resizes regions of interest of an input tensor.

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
func BNNSCropResize(_ layer_params: UnsafePointer<BNNSLayerParametersCropResize>, _ input: UnsafePointer<BNNSNDArrayDescriptor>, _ roi: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

#### Discussion

Use this function to resize the spatial dimensions (two dimensions with the smallest strides) of the first input according to the bounding boxes and box indices specified in the second input.

The operation works over contiguous 2D data and provides support for multiple channels and batches that contain more than one input-output pair.

For example, the following code defines a 6x5 matrix of single-precision values:

```swift
let batchSize = 1
let channelCount = 1

let values: [Float] = [ 0, 1, 0, 0, 0, 0,
                        1, 1, 1, 0, 0, 0,
                        0, 1, 0, 9, 0, 9,
                        0, 0, 0, 0, 9, 0,
                        0, 0, 0, 9, 0, 9 ]

var inputDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: values,
    shape: .tensor4DLastMajor(6,
                              5,
                              channelCount,
                              batchSize))
```

Define the regions of interest as sets of four coordinates. The code below specifies the regions of interest with [`BNNSCenterSizeWidthFirst`](bnnscentersizewidthfirst.md) coordinate mode, that is the coordinates are ordered as horizontal center, vertical center, width, and height.

```swift
// Extracts:
//      0.0, 1.0, 0.0,
//      1.0, 1.0, 1.0,
//      0.0, 1.0, 0.0
let roiValues0: [Float] = [1, // w_center
                           1, // h_center
                           3, // box_width
                           3] // box_height

// Extracts:
//      9.0, 0.0, 9.0,
//      0.0, 9.0, 0.0,
//      9.0, 0.0, 9.0
let roiValues1: [Float] = [4, // w_center
                           3, // h_center
                           3, // box_width
                           3] // box_height
let boxCount = 2

var roiDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: roiValues0 + roiValues1,
    shape: .matrixLastMajor(4,
                            boxCount))
```

Specify the output descriptor as a 5D tensor.

```swift
let outputWidth = 3
let outputHeight = 3

var outputDescriptor = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .tensor5DLastMajor(outputWidth,
                              outputHeight,
                              channelCount,
                              batchSize,
                              boxCount))
```

To perform the crop-resize, create a parameters structure and call [`BNNSCropResize(_:_:_:_:_:)`](bnnscropresize(_:_:_:_:_:).md).

```swift
var params = BNNSLayerParametersCropResize(
    normalized_coordinates: false,
    spatial_scale: 1,
    extrapolation_value: 0,
    sampling_mode: BNNSLinearSamplingOffsetCorners,
    box_coordinate_mode: BNNSCenterSizeWidthFirst,
    method: BNNSInterpolationMethodLinear)

BNNSCropResize(&params,
               &inputDescriptor,
               &roiDescriptor,
               &outputDescriptor, nil)
```

On return, `outputDescriptor` contains `boxCount` slices that contain the data with the regions of interest of the input tensor:

```swift
[ 0.0, 1.0, 0.0,
  1.0, 1.0, 1.0,
  0.0, 1.0, 0.0,

  9.0, 0.0, 9.0,
  0.0, 9.0, 0.0,
  9.0, 0.0, 9.0 ]
```

## Parameters

- `layer_params`: A pointer to the layer parameters.
- `input`: A pointer to the input array descriptor.
- `roi`: A pointer to the regions of interest array descriptor.
- `output`: A pointer to the output array descriptor.
- `filter_params`: Runtime filter parameters.

## See Also

- [class CropResizeLayer](bnns/cropresizelayer.md)
  A layer object that wraps a crop-resize filter and manages its deinitialization.
- [func BNNSCropResizeBackward(UnsafePointer<BNNSLayerParametersCropResize>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnscropresizebackward(_:_:_:_:_:).md)
  Applies a crop-resize filter backward to generate gradients.
- [struct BNNSLayerParametersCropResize](bnnslayerparameterscropresize.md)
  A set of parameters that describe a crop-resize operation.
- [struct BNNSBoxCoordinateMode](bnnsboxcoordinatemode.md)
  Constants that define the convention to specify the four bounding box coordinates for crop-resize operations.
- [struct BNNSLinearSamplingMode](bnnslinearsamplingmode.md)
  Constants that specify how a crop-resize layer samples a grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnscropresize(_:_:_:_:_:))*