# BNNSApplyMultiheadAttentionBackward(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a multihead attention filter backward to generate gradients.

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
func BNNSApplyMultiheadAttentionBackward(_ F: BNNSFilter?, _ batch_size: Int, _ query: UnsafeRawPointer?, _ query_stride: Int, _ query_param_delta: UnsafeMutablePointer<BNNSMHAProjectionParameters>?, _ key: UnsafeRawPointer?, _ key_stride: Int, _ key_mask: UnsafePointer<BNNSNDArrayDescriptor>?, _ key_mask_stride: Int, _ key_param_delta: UnsafeMutablePointer<BNNSMHAProjectionParameters>?, _ value: UnsafeRawPointer?, _ value_stride: Int, _ value_param_delta: UnsafeMutablePointer<BNNSMHAProjectionParameters>?, _ add_to_attention: UnsafePointer<BNNSNDArrayDescriptor>?, _ key_attn_bias_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ value_attn_bias_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>?, _ output: UnsafeRawPointer?, _ output_stride: Int, _ output_param_delta: UnsafeMutablePointer<BNNSMHAProjectionParameters>, _ backprop_cache_size: Int, _ backprop_cache: UnsafeMutableRawPointer?, _ workspace_size: UnsafeMutablePointer<Int>?, _ workspace: UnsafeMutableRawPointer?) -> Int32
```

## Parameters

- `F`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `query`: Pointer to data for query input matrix.
- `query_stride`: Batch stride for query.
- `query_param_delta`: Pointer to the data structure used to hold deltas for corresponding components.
- `key`: Pointer to data for key input matrix.
- `key_stride`: Batch stride for key.
- `key_mask`: Mask applied to key for ignoring entries.
- `key_mask_stride`: Batch stride for key mask.
- `key_param_delta`: Pointer to the data structure used to hold deltas for corresponding components.
- `value`: Pointer to the data for value input matrix,.
- `value_stride`: Batch stride for value.
- `value_param_delta`: Pointer to the data structure used to hold deltas for corresponding components.
- `add_to_attention`: Pointer to the 2D tensor that’s used as part of the mask function prior to softmax in the attention calculation.
- `key_attn_bias_delta`: Pointer to the data structure used to hold deltas for corresponding components.
- `value_attn_bias_delta`: Pointer to the data structure used to hold deltas for corresponding components.
- `output`: Pointer to the data for output matrix.
- `output_stride`: Batch stride for output.
- `output_param_delta`: Pointer to the data structure used to hold deltas for corresponding components.
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
- [func BNNSApplyMultiheadAttention(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, UnsafePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?) -> Int32](bnnsapplymultiheadattention(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a mutihead attention filter to a set of input objects, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsapplymultiheadattentionbackward(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:))*