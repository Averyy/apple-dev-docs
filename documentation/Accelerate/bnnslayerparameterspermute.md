# BNNSLayerParametersPermute

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a permute layer.

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
struct BNNSLayerParametersPermute
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, permutation: (Int, Int, Int, Int, Int, Int, Int, Int))](bnnslayerparameterspermute/init(i_desc:o_desc:permutation:).md)
  Returns a new permute layer parameters structure from the specified parameters.
- [init()](bnnslayerparameterspermute/init.md)
  Returns a new permute layer parameters structure.
### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparameterspermute/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparameterspermute/o_desc.md)
  The descriptor of the output.
- [var permutation: (Int, Int, Int, Int, Int, Int, Int, Int)](bnnslayerparameterspermute/permutation.md)
  The tuple that defines the permutation.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class PermuteLayer](bnns/permutelayer.md)
  A layer object that wraps a permute filter and manages its deinitialization.
- [func BNNSFilterCreateLayerPermute(UnsafePointer<BNNSLayerParametersPermute>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerpermute(_:_:).md)
  Returns a new permute layer.
- [func BNNSPermuteFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnspermutefilterapplybackwardbatch(_:_:_:_:_:_:).md)
  Applies a permute filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspermute)*