# BNNSFilterCreateLayerMultiheadAttention(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a new multihead attention layer.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
func BNNSFilterCreateLayerMultiheadAttention(_ layer_params: UnsafePointer<BNNSLayerParametersMultiheadAttention>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

```c
BNNSFilterBNNSFilterCreateLayerMultiheadAttention(const BNNSLayerParametersMultiheadAttention *layer_params, const BNNSFilterParameters *filter_params);
```

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: The filter runtime parameters.

## See Also

### Multihead attention layers
- [struct BNNSMHAProjectionParameters](./bnnsmhaprojectionparameters.md)
  A structure that contains multihead attention projection parameters.
- [struct BNNSLayerParametersMultiheadAttention](./bnnslayerparametersmultiheadattention.md)
  A structure that contains the parameters of a multihead attention layer.
- [func BNNSApplyMultiheadAttention(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, UnsafePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?) -> Int32](./bnnsapplymultiheadattention%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a mutihead attention filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSApplyMultiheadAttentionBackward(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>, Int, UnsafeMutableRawPointer?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?) -> Int32](./bnnsapplymultiheadattentionbackward%28_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a multihead attention filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayermultiheadattention(_:_:))*