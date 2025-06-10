# BNNSApplyMultiheadAttention(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a mutihead attention filter to a set of input objects, writing the result to a set of output objects.

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
func BNNSApplyMultiheadAttention(_ F: BNNSFilter?, _ batch_size: Int, _ query: UnsafeRawPointer, _ query_stride: Int, _ key: UnsafeRawPointer, _ key_stride: Int, _ key_mask: UnsafePointer<BNNSNDArrayDescriptor>?, _ key_mask_stride: Int, _ value: UnsafeRawPointer, _ value_stride: Int, _ output: UnsafeMutableRawPointer, _ output_stride: Int, _ add_to_attention: UnsafePointer<BNNSNDArrayDescriptor>?, _ backprop_cache_size: UnsafeMutablePointer<Int>?, _ backprop_cache: UnsafeMutableRawPointer?, _ workspace_size: UnsafeMutablePointer<Int>?, _ workspace: UnsafeMutableRawPointer?) -> Int32
```

#### Discussion

Provide `key_mask` as a 1D tensor containing `source_length` elements. Where the elements evaluate to true, the attention operation ignores the corresponding elements of the key matrix.

## Parameters

- `F`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `query`: Pointer to the data for query input matrix.
- `query_stride`: Batch stride for query.
- `key`: Pointer to the data for key input matrix.
- `key_stride`: Batch stride for key.
- `key_mask`: Mask applied to key for ignoring entries.
- `key_mask_stride`: Batch stride for key mask.
- `value`: Pointer to the data for value input matrix.
- `value_stride`: Batch stride for value.
- `output`: Pointer to the data for output matrix
- `output_stride`: Batch stride for output.
- `add_to_attention`: Pointer to the 2D tensor that’s used as part of the mask function prior to softmax in the attention calculation.
- `backprop_cache_size`: The size of the back propagation cache, in bytes.
- `backprop_cache`: A cache that stores intermediate results that BNNS can use to accelerate a future call to this function.
- `workspace_size`: The size of the array workspace, in bytes.
- `workspace`: A scratch buffer used during the calculation.

## See Also

- [struct BNNSMHAProjectionParameters](bnnsmhaprojectionparameters.md)
  A structure that contains multihead attention projection parameters.
- [struct BNNSLayerParametersMultiheadAttention](bnnslayerparametersmultiheadattention.md)
  A structure that contains the parameters of a multihead attention layer.
- [func BNNSFilterCreateLayerMultiheadAttention(UnsafePointer<BNNSLayerParametersMultiheadAttention>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayermultiheadattention(_:_:).md)
  Returns a new multihead attention layer.
- [func BNNSApplyMultiheadAttentionBackward(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>, Int, UnsafeMutableRawPointer?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?) -> Int32](bnnsapplymultiheadattentionbackward(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a multihead attention filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsapplymultiheadattention(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*