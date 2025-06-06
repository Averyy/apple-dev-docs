# BNNSFilterCreateLayerPermute(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new permute layer.

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
func BNNSFilterCreateLayerPermute(_ layer_params: UnsafePointer<BNNSLayerParametersPermute>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

Use a permute layer to copy one tensor to another while permuting the order of the axes. For example, given a [`BNNSDataLayoutImageCHW`](bnnsdatalayoutimagechw.md) tensor containing the following values:

```swift
let sourceData: [Int8] = [ 1,  2,
                           3,  4] +
                         [10, 20,
                          30, 40]
```

The following code copies the data from `sourceData` to `destinationData`, but with the axis order permuted from [0, 1, 2] to [2, 1, 0]:

```swift
var destinationData = [Int8](repeating: 0,
                              count: sourceData.count)

let descriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                       layout: BNNSDataLayoutImageCHW,
                                       size: (2, 2, 2, 0, 0, 0, 0, 0),
                                       stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                       data: nil,
                                       data_type: .int8,
                                       table_data: nil,
                                       table_data_type: .int8,
                                       data_scale: 1,
                                       data_bias: 0)

var params = BNNSLayerParametersPermute(i_desc: descriptor,
                                        o_desc: descriptor,
                                        permutation: (2, 1, 0, 0, 0, 0, 0, 0))

let filter = BNNSFilterCreateLayerPermute(&params, nil)
        
defer {
    BNNSFilterDestroy(filter)
}

BNNSFilterApply(filter,
                sourceData,
                &destinationData)

```

On return, `destinationData` contains `[1, 10, 3, 30, 2, 20, 4, 40]`.

The following figure shows the source data on the left, and the permute result on the right:

![Figure that shows a three dimensional tensor before and after permutation. The original tensor is shown on the left, with axis zero running left to right, axis one running top to bottom, and axis two running front to back. The permuted tensor is shown on the right, with axis zero running front to back, axis one running top to bottom, and axis two running left to right.](https://docs-assets.developer.apple.com/published/a4336952fa0d08822a12e7566770962d/media-3633102%402x.png)

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: The filter runtime parameters.

## See Also

- [class PermuteLayer](bnns/permutelayer.md)
  A layer object that wraps a permute filter and manages its deinitialization.
- [struct BNNSLayerParametersPermute](bnnslayerparameterspermute.md)
  A structure that contains the parameters of a permute layer.
- [func BNNSPermuteFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnspermutefilterapplybackwardbatch(_:_:_:_:_:_:).md)
  Applies a permute filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayerpermute(_:_:))*