# BNNS.PermuteLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A layer object that wraps a permute filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
class PermuteLayer
```

## Topics

### Creating a Permute Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, permutation: [Int], filterParameters: BNNSFilterParameters?)](./permutelayer/init%28input,output,permutation,filterparameters%29.md)
  Returns a new permute layer.

## Relationships

### Inherits From
- [BNNS.UnaryLayer](./unarylayer.md)

## See Also

### Permute layers
- [struct BNNSLayerParametersPermute](../bnnslayerparameterspermute.md)
  A structure that contains the parameters of a permute layer.
- [func BNNSFilterCreateLayerPermute(UnsafePointer<BNNSLayerParametersPermute>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatelayerpermute%28_,_%29.md)
  Returns a new permute layer.
- [func BNNSPermuteFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](../bnnspermutefilterapplybackwardbatch%28_,_,_,_,_,_%29.md)
  Applies a permute filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/permutelayer)*