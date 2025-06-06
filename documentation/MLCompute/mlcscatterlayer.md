# MLCScatterLayer

**Framework**: ML Compute  
**Kind**: class

A layer that updates the output at an index you specify.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
class MLCScatterLayer
```

## Topics

### Creating Scatter Layers
- [convenience init?(dimension: Int, reductionType: MLCReductionType)](mlcscatterlayer/init(dimension:reductiontype:).md)
  Creates a scatter layer with the dimension and reduction type you specify.
### Inspecting Scatter Layers
- [var dimension: Int](mlcscatterlayer/dimension.md)
  The dimension to index.
- [var reductionType: MLCReductionType](mlcscatterlayer/reductiontype.md)
  The reduction type that applies to all values in the source tensor.

## Relationships

### Inherits From
- [MLCLayer](mlclayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCTransposeLayer](mlctransposelayer.md)
  A layer that permutes the dimensions you specify.
- [class MLCConcatenationLayer](mlcconcatenationlayer.md)
  A layer that combines tensors into a single tensor.
- [class MLCReshapeLayer](mlcreshapelayer.md)
  A layer that reshapes a tensor with the shape you specify.
- [class MLCSliceLayer](mlcslicelayer.md)
  A layer that extracts a slice from a tensor.
- [class MLCSplitLayer](mlcsplitlayer.md)
  A layer that splits a tensor value into a list of subtensors.
- [class MLCPaddingLayer](mlcpaddinglayer.md)
  A layer that pads a tensor with the padding sizes you specify.
- [class MLCSelectionLayer](mlcselectionlayer.md)
  A layer for selecting elements from two tensors.
- [class MLCGatherLayer](mlcgatherlayer.md)
  A layer that fetches data at the locations you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcscatterlayer)*