# BNNSLayerParametersPermute

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters of a permute layer.

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
struct BNNSLayerParametersPermute
```

```c
typedef struct { ... } BNNSLayerParametersPermute;
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, permutation: (Int, Int, Int, Int, Int, Int, Int, Int))](./bnnslayerparameterspermute/init%28i_desc,o_desc,permutation%29.md)
  Returns a new permute layer parameters structure from the specified parameters.
- [init()](./bnnslayerparameterspermute/init%28%29.md)
  Returns a new permute layer parameters structure.
### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](./bnnslayerparameterspermute/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./bnnslayerparameterspermute/o_desc.md)
  The descriptor of the output.
- [var permutation: (Int, Int, Int, Int, Int, Int, Int, Int)](./bnnslayerparameterspermute/permutation.md)
  The tuple that defines the permutation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Permute layers
- [class PermuteLayer](./bnns/permutelayer.md)
  A layer object that wraps a permute filter and manages its deinitialization.
- [func BNNSFilterCreateLayerPermute(UnsafePointer<BNNSLayerParametersPermute>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerpermute%28_,_%29.md)
  Returns a new permute layer.
- [func BNNSPermuteFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](./bnnspermutefilterapplybackwardbatch%28_,_,_,_,_,_%29.md)
  Applies a permute filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspermute)*