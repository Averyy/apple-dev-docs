# BNNS.PermuteLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a permute filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
class PermuteLayer
```

## Topics

### Creating a Permute Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, permutation: [Int], filterParameters: BNNSFilterParameters?)](bnns/permutelayer/init(input:output:permutation:filterparameters:).md)
  Returns a new permute layer.

## Relationships

### Inherits From
- [BNNS.UnaryLayer](bnns/unarylayer.md)

## See Also

- [struct BNNSLayerParametersPermute](bnnslayerparameterspermute.md)
  A structure that contains the parameters of a permute layer.
- [func BNNSFilterCreateLayerPermute(UnsafePointer<BNNSLayerParametersPermute>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerpermute(_:_:).md)
  Returns a new permute layer.
- [func BNNSPermuteFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnspermutefilterapplybackwardbatch(_:_:_:_:_:_:).md)
  Applies a permute filter backward to generate gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/permutelayer)*