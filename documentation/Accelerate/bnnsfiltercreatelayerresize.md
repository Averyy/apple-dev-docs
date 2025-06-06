# BNNSFilterCreateLayerResize(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new resize layer.

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
func BNNSFilterCreateLayerResize(_ layer_params: UnsafePointer<BNNSLayerParametersResize>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

Use a resize layer to copy data between two differently sized tensors using a specified interpolation method. Resized dimensions must all either upsample or downsample; the resize layer doesn’t support combining both directions in a single operation.

For example, to resize the following source data to the specified destination dimensions:

```swift
let sourceData: [Float] = [0, 1, 0,
                           1, 1, 1,
                           0, 1, 0]

let destinationWidth = 24
let destinationHeight = 9

var destinationData = [Float](repeating: 0,
                              count: destinationWidth * destinationHeight)
```

Use the following code:

```swift


let inputDescriptor = BNNSNDArrayDescriptor(flags: flags,
                                           layout: BNNSDataLayoutRowMajorMatrix,
                                           size: (3, 3, 0, 0, 0, 0, 0, 0),
                                           stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                           data: nil,
                                           data_type: .float,
                                           table_data: nil,
                                           table_data_type: .float,
                                           data_scale: 1,
                                           data_bias: 0)

let outputDescriptor = BNNSNDArrayDescriptor(flags: flags,
                                            layout: BNNSDataLayoutRowMajorMatrix,
                                            size: (destinationWidth, destinationHeight, 0, 0, 0, 0, 0, 0),
                                            stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                            data: nil,
                                            data_type: .float,
                                            table_data: nil,
                                            table_data_type: .float,
                                            data_scale: 1,
                                            data_bias: 0)

var params = BNNSLayerParametersResize(method: BNNSInterpolationMethodNearest,
                                       i_desc: inputDescriptor,
                                       o_desc: outputDescriptor,
                                       align_corners: false)

let filter = BNNSFilterCreateLayerResize(&params, nil)

defer {
    BNNSFilterDestroy(filter)
}

BNNSFilterApply(filter,
                sourceData,
                &destinationData)
```

On return, `destinationData` contains the following values:

```swift
0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 
```

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: The filter runtime parameters.

## See Also

- [class ResizeLayer](bnns/resizelayer.md)
  A layer object that wraps a resize filter and manages its deinitialization.
- [struct BNNSInterpolationMethod](bnnsinterpolationmethod.md)
  Constants that describe interpolation methods.
- [struct BNNSLayerParametersResize](bnnslayerparametersresize.md)
  A structure that contains the parameters of a resize layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayerresize(_:_:))*