# BNNSLayerParametersMultiheadAttention

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a multihead attention layer.

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
struct BNNSLayerParametersMultiheadAttention
```

## Topics

### Initializers
- [init(query: BNNSMHAProjectionParameters, key: BNNSMHAProjectionParameters, value: BNNSMHAProjectionParameters, add_zero_attn: Bool, key_attn_bias: BNNSNDArrayDescriptor, value_attn_bias: BNNSNDArrayDescriptor, output: BNNSMHAProjectionParameters, dropout: Float, seed: UInt32)](bnnslayerparametersmultiheadattention/init(query:key:value:add_zero_attn:key_attn_bias:value_attn_bias:output:dropout:seed:).md)
  Returns a new multihead attention layer parameters structure from the specified parameters.
- [init()](bnnslayerparametersmultiheadattention/init.md)
  Returns a new multihead attention layer parameters structure.
### Instance Properties
- [var query: BNNSMHAProjectionParameters](bnnslayerparametersmultiheadattention/query.md)
  A projection parameter structure that describes the query-related input parameters and projection.
- [var key: BNNSMHAProjectionParameters](bnnslayerparametersmultiheadattention/key.md)
  A projection parameter structure that describes the key-related input parameters and projection.
- [var value: BNNSMHAProjectionParameters](bnnslayerparametersmultiheadattention/value.md)
  A projection parameter structure that describes the value-related input parameters and projection.
- [var add_zero_attn: Bool](bnnslayerparametersmultiheadattention/add_zero_attn.md)
  A Boolean value that, if true, adds a row of zeroes to the projected  and  inputs to the calculation.
- [var key_attn_bias: BNNSNDArrayDescriptor](bnnslayerparametersmultiheadattention/key_attn_bias.md)
  A 2D tensor that’s added to the value as part of the attention calculation.
- [var value_attn_bias: BNNSNDArrayDescriptor](bnnslayerparametersmultiheadattention/value_attn_bias.md)
  An optional `d_value` x `num_heads` 2D tensor that’s added as part of the attention calculation.
- [var output: BNNSMHAProjectionParameters](bnnslayerparametersmultiheadattention/output.md)
  A projection parameter structure that describes the output tensor and associated projection.
- [var dropout: Float](bnnslayerparametersmultiheadattention/dropout.md)
  The seed for the dropout layer’s random number generator.
- [var seed: UInt32](bnnslayerparametersmultiheadattention/seed.md)
  A random seed for the dropout layer.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct BNNSMHAProjectionParameters](bnnsmhaprojectionparameters.md)
  A structure that contains multihead attention projection parameters.
- [func BNNSFilterCreateLayerMultiheadAttention(UnsafePointer<BNNSLayerParametersMultiheadAttention>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayermultiheadattention(_:_:).md)
  Returns a new multihead attention layer.
- [func BNNSApplyMultiheadAttention(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, UnsafePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?) -> Int32](bnnsapplymultiheadattention(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a mutihead attention filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSApplyMultiheadAttentionBackward(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>, Int, UnsafeMutableRawPointer?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?) -> Int32](bnnsapplymultiheadattentionbackward(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a multihead attention filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersmultiheadattention)*