# MLCConcatenationLayer

**Framework**: ML Compute  
**Kind**: class

A layer that combines tensors into a single tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCConcatenationLayer
```

## Topics

### Creating Concatenation Layers
- [convenience init()](mlcconcatenationlayer/init.md)
  Creates a concatenation layer with a dimension value of 1, which typically represents feature channels.
- [convenience init(dimension: Int)](mlcconcatenationlayer/init(dimension:).md)
  Creates a concatenation layer with the dimension you specify.
### Inspecting Concatenation Layers
- [var dimension: Int](mlcconcatenationlayer/dimension.md)
  The dimension, or axis, along which you concatenate tensors.

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
- [class MLCReshapeLayer](mlcreshapelayer.md)
  A layer that reshapes a tensor with the shape you specify.
- [class MLCSliceLayer](mlcslicelayer.md)
  A layer that extracts a slice from a tensor.
- [class MLCSplitLayer](mlcsplitlayer.md)
  A layer that splits a tensor value into a list of subtensors.
- [class MLCPaddingLayer](mlcpaddinglayer.md)
  A layer that pads a tensor with the padding sizes you specify.
- [class MLCScatterLayer](mlcscatterlayer.md)
  A layer that updates the output at an index you specify.
- [class MLCSelectionLayer](mlcselectionlayer.md)
  A layer for selecting elements from two tensors.
- [class MLCGatherLayer](mlcgatherlayer.md)
  A layer that fetches data at the locations you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconcatenationlayer)*