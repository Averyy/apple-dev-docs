# BNNSMHAProjectionParameters

**Framework**: Accelerate  
**Kind**: struct

A structure that contains multihead attention projection parameters.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSMHAProjectionParameters
```

## Topics

### Initializers
- [init(target_desc: BNNSNDArrayDescriptor, weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor)](bnnsmhaprojectionparameters/init(target_desc:weights:bias:).md)
  Returns a new multihead attention projection parameters structure from the specified parameters.
- [init()](bnnsmhaprojectionparameters/init.md)
  Returns a new multihead attention projection parameters structure.
### Instance Properties
- [var target_desc: BNNSNDArrayDescriptor](bnnsmhaprojectionparameters/target_desc.md)
  The descriptor—which is either an input query, key, or value, or an output—of the main target of the operation.
- [var weights: BNNSNDArrayDescriptor](bnnsmhaprojectionparameters/weights.md)
  The descriptor of the initial projection’s weights.
- [var bias: BNNSNDArrayDescriptor](bnnsmhaprojectionparameters/bias.md)
  The descriptor of the initial projection’s bias.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct BNNSLayerParametersMultiheadAttention](bnnslayerparametersmultiheadattention.md)
  A structure that contains the parameters of a multihead attention layer.
- [func BNNSFilterCreateLayerMultiheadAttention(UnsafePointer<BNNSLayerParametersMultiheadAttention>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayermultiheadattention(_:_:).md)
  Returns a new multihead attention layer.
- [func BNNSApplyMultiheadAttention(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeRawPointer, Int, UnsafePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, UnsafePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?) -> Int32](bnnsapplymultiheadattention(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a mutihead attention filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSApplyMultiheadAttentionBackward(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafeRawPointer?, Int, UnsafePointer<BNNSNDArrayDescriptor>?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>?, UnsafePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSMHAProjectionParameters>, Int, UnsafeMutableRawPointer?, UnsafeMutablePointer<Int>?, UnsafeMutableRawPointer?) -> Int32](bnnsapplymultiheadattentionbackward(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a multihead attention filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsmhaprojectionparameters)*