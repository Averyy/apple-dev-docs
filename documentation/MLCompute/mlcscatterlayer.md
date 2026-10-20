# MLCScatterLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that updates the output at an index you specify.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```swift
class MLCScatterLayer
```

```objc
@interface MLCScatterLayer : MLCLayer
```

## Topics

### Creating Scatter Layers
- [convenience init?(dimension: Int, reductionType: MLCReductionType)](./mlcscatterlayer/init%28dimension,reductiontype%29.md)
  Creates a scatter layer with the dimension and reduction type you specify.
### Inspecting Scatter Layers
- [var dimension: Int](./mlcscatterlayer/dimension.md)
  The dimension to index.
- [var reductionType: MLCReductionType](./mlcscatterlayer/reductiontype.md)
  The reduction type that applies to all values in the source tensor.

## Relationships

### Inherits From
- [MLCLayer](./mlclayer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Transformation Layers
- [class MLCTransposeLayer](./mlctransposelayer.md)
  A layer that permutes the dimensions you specify.
- [class MLCConcatenationLayer](./mlcconcatenationlayer.md)
  A layer that combines tensors into a single tensor.
- [class MLCReshapeLayer](./mlcreshapelayer.md)
  A layer that reshapes a tensor with the shape you specify.
- [class MLCSliceLayer](./mlcslicelayer.md)
  A layer that extracts a slice from a tensor.
- [class MLCSplitLayer](./mlcsplitlayer.md)
  A layer that splits a tensor value into a list of subtensors.
- [class MLCPaddingLayer](./mlcpaddinglayer.md)
  A layer that pads a tensor with the padding sizes you specify.
- [class MLCSelectionLayer](./mlcselectionlayer.md)
  A layer for selecting elements from two tensors.
- [class MLCGatherLayer](./mlcgatherlayer.md)
  A layer that fetches data at the locations you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcscatterlayer)*