# BNNSLayerParametersTensorContraction

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters of a tensor-contraction layer.

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
struct BNNSLayerParametersTensorContraction
```

```c
typedef struct { ... } BNNSLayerParametersTensorContraction;
```

## Topics

### Initializers
- [init(operation: UnsafePointer<CChar>, alpha: Float, beta: Float, iA_desc: BNNSNDArrayDescriptor, iB_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor)](./bnnslayerparameterstensorcontraction/init%28operation,alpha,beta,ia_desc,ib_desc,o_desc%29.md)
  Returns a new tensor-contraction parameters structure.
### Instance Properties
- [var operation: UnsafePointer<CChar>](./bnnslayerparameterstensorcontraction/operation.md)
  The string that describes the operation.
- [var alpha: Float](./bnnslayerparameterstensorcontraction/alpha.md)
  Scaling that the operation applies to the result.
- [var beta: Float](./bnnslayerparameterstensorcontraction/beta.md)
  A value, that must be either 0.0 or 1.0, you use to scale the existing output before the operation adds it to the result.
- [var iA_desc: BNNSNDArrayDescriptor](./bnnslayerparameterstensorcontraction/ia_desc.md)
  The descriptor of input matrix *A*.
- [var iB_desc: BNNSNDArrayDescriptor](./bnnslayerparameterstensorcontraction/ib_desc.md)
  The descriptor of input matrix *B*.
- [var o_desc: BNNSNDArrayDescriptor](./bnnslayerparameterstensorcontraction/o_desc.md)
  The descriptor of the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Tensor contraction layers
- [func BNNSFilterCreateLayerTensorContraction(UnsafePointer<BNNSLayerParametersTensorContraction>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayertensorcontraction%28_,_%29.md)
  Returns a new tensor-contraction layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterstensorcontraction)*