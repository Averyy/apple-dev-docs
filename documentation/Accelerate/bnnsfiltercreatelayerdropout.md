# BNNSFilterCreateLayerDropout(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new dropout layer.

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
func BNNSFilterCreateLayerDropout(_ layer_params: UnsafePointer<BNNSLayerParametersDropout>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

Use a dropout layer to randomly set the elements—or entire dimensions—of a tensor to 0. The layer scales the unchanged elements by `1 / (1 -` [`rate`](bnnslayerparametersdropout/rate.md) `)`. The following code randomly drops half the elements from a 4 x 4 matrix:

```swift
let input: [Float] = [1, 1, 1, 1,
                      1, 1, 1, 1,
                      1, 1, 1, 1,
                      1, 1, 1, 1]

var output = [Float](repeating: 0,
                     count: input.count)

let descriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                       layout: BNNSDataLayoutRowMajorMatrix,
                                       size: (4, 4, 0, 0, 0, 0, 0, 0),
                                       stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                       data: nil,
                                       data_type: .float,
                                       table_data: nil,
                                       table_data_type: .float,
                                       data_scale: 0,
                                       data_bias: 0)

let control: UInt8 = 0b0000
let rate: Float = 0.5

var dropoutParams = BNNSLayerParametersDropout(i_desc: descriptor,
                                               o_desc: descriptor,
                                               rate: rate,
                                               seed: 0,
                                               control: control)

let dropoutFilter = BNNSFilterCreateLayerDropout(&dropoutParams, nil)

BNNSFilterApply(dropoutFilter, input, &output)
```

On return, output contains the following values:

```c
[ 2.0, 2.0, 0.0, 0.0, 
  2.0, 2.0, 0.0, 2.0, 
  2.0, 0.0, 0.0, 2.0, 
  0.0, 0.0, 0.0, 2.0 ]
```

Use the [`control`](bnnslayerparametersdropout/control.md) parameter to dropout entire dimensions. For example, setting `control` to `0b0010` and `rate` to `0.75` drops three quarters of the columns, and scales the remaining values by 4:

```c
[ 0.0, 4.0, 0.0, 0.0, 
  0.0, 4.0, 0.0, 0.0, 
  0.0, 4.0, 0.0, 0.0, 
  0.0, 4.0, 0.0, 0.0 ]
```

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: Filter runtime parameters.

## See Also

- [class DropoutLayer](bnns/dropoutlayer.md)
  A layer object that wraps a dropout filter and manages its deinitialization.
- [struct BNNSLayerParametersDropout](bnnslayerparametersdropout.md)
  A structure that contains the parameters of a dropout layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayerdropout(_:_:))*