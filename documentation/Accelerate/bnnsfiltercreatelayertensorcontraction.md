# BNNSFilterCreateLayerTensorContraction(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new tensor-contraction layer.

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
func BNNSFilterCreateLayerTensorContraction(_ layer_params: UnsafePointer<BNNSLayerParametersTensorContraction>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

A tensor contraction is the summation of the elements of two tensors over one or more indices. BNNS represents this in the `operation` parameter of a [`BNNSLayerParametersTensorContraction`](bnnslayerparameterstensorcontraction.md) structure as a string using Einstein’s summation convention.

For example, the string:

```c
"a_ijp, b_ijq -> o_pq" 
```

Represents the operation:

![General formula that describes mathematically the equation represented by the string a underscore i j p comma b underscore i j q hyphen greater than o underscore p q. o sub p sub q equals alpha times summation over i j times a sub i sub j sub p times b sub i sub j sub q](https://docs-assets.developer.apple.com/published/c0c5777fa3a46aa2aa5826c438c5a9d5/media-3581536%402x.png)

Inputs may be either trained parameters or inputs.

If the name preceding the underscore is `“w”`, the operation assumes the tensor is a trained parameter (weights). Otherwise the operation assumes the tensor is an input (the letter has no other effect and may be whatever you wish). At most, one of the inputs may be a trained parameter.

If the names of the left-hand side inputs match, the operation assumes the contraction is of a tensor with itself, for example, to calculate the Gram matrix or a dot product.

In the case where one of the inputs is a weight or the operation is a contraction of a tensor with itself, use [`BNNSFilterApply(_:_:_:)`](bnnsfilterapply(_:_:_:).md) or [`BNNSFilterApplyBatch(_:_:_:_:_:_:)`](bnnsfilterapplybatch(_:_:_:_:_:_:).md). If the operation has two inputs, use [`BNNSFilterApplyTwoInput(_:_:_:_:)`](bnnsfilterapplytwoinput(_:_:_:_:).md) or [`BNNSFilterApplyTwoInputBatch(_:_:_:_:_:_:_:_:)`](bnnsfilterapplytwoinputbatch(_:_:_:_:_:_:_:_:).md).

Use a tensor contraction layer to also copy from one layer to another with a permutation of indices. For example, the string:

```c
"a_ij -> c_ji"
```

Represents the operation:

![General formula that describes mathematically the equation represented by the a underscore i j hyphen greater than c underscore j i. Cap C equals alpha times Cap A sup cap T.](https://docs-assets.developer.apple.com/published/4f0e29c8ceb0e4cfc574293be1d66b53/media-3581537%402x.png)

BNNS tensor contraction supports broadcasting by using `“*”` as the final index, for example, the following string matches additional indices of `a` and `c`.

```swift
"a_ij*, b_ij -> c_*"
```

`“*”` always represents indices that occur on both sides of the operation, and never an index over which contraction performs summation.

A `“*”` on one side only matches indices represent by a `“*”` on the other side, and never indices represented by a letter.

Note that where contraction matches index letters, the sizes of the corresponding dimensions for the tensors must also match, unless one tensor has size 1. In that case the operation repeats (broadcasts) to match the corresponding dimension.

##### Perform a Tensor Contraction

The following code performs a tensor contraction over two 2 x 1 row-major matrices, writing the result to a 2 x 2 row-major matrix.

First, define the input and output matrices and their descriptors:

```swift
let aValues: [Float] = [1, 2]
let bValues: [Float] = [3, 4]

let inputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                            layout: BNNSDataLayoutRowMajorMatrix,
                                            size: (2, 1, 0, 0, 0, 0, 0, 0),
                                            stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                            data: nil,
                                            data_type: .float,
                                            table_data: nil,
                                            table_data_type: .float,
                                            data_scale: 1,
                                            data_bias: 0)

var outputValues = [Float](repeating: -1,
                           count: aValues.count * bValues.count)

let outputDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                             layout: BNNSDataLayoutRowMajorMatrix,
                                             size: (2, 2, 0, 0, 0, 0, 0, 0),
                                             stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                             data: nil,
                                             data_type: .float,
                                             table_data: nil,
                                             table_data_type: .float,
                                             data_scale: 1,
                                             data_bias: 0)
```

Use the following code to perform the contraction:

```swift
let operation = "a_ip, b_iq -> o_pq"

operation.withCString { operationPtr in
    
    var layer_params = BNNSLayerParametersTensorContraction(operation: operationPtr,
                                                            alpha: 10,
                                                            beta: 0,
                                                            iA_desc: inputDescriptor,
                                                            iB_desc: inputDescriptor,
                                                            o_desc: outputDescriptor)
    
    let layer = BNNSFilterCreateLayerTensorContraction(&layer_params,
                                                       nil)
    
    BNNSFilterApplyTwoInput(layer, aValues, bValues, &outputValues)
}
```

On return, `outputValues` contains the following values:

```swift
[ 30.0,    // 10.0 * (1.0 * 3.0) 
  40.0,    // 10.0 * (1.0 * 4.0)
  60.0,    // 10.0 * (2.0 * 3.0)
  80.0 ]   // 10.0 * (2.0 * 4.0)
```

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: The filter runtime parameters.

## See Also

- [struct BNNSLayerParametersTensorContraction](bnnslayerparameterstensorcontraction.md)
  A structure that contains the parameters of a tensor-contraction layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayertensorcontraction(_:_:))*