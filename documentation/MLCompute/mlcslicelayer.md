# MLCSliceLayer

**Framework**: ML Compute  
**Kind**: class

A layer that extracts a slice from a tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCSliceLayer
```

#### Overview

The framework supports positive stride.

Use a slice layer to slice a given source. Slicing won’t decrease the tensor dimension. The start, end, and stride vectors must be of the same size, equal to the source tensor dimension.

## Topics

### Creating Slice Layers
- [convenience init?(start: [Int], end: [Int], stride: [Int]?)](mlcslicelayer/init(start:end:stride:).md)
  Creates a slice layer with the start, end, and stride you specify.
### Inspecting Slice Layers
- [var start: [Int]](mlcslicelayer/start-6wsh6.md)
  The start vector.
- [var end: [Int]](mlcslicelayer/end-9xw91.md)
  The end vector.
- [var stride: [Int]?](mlcslicelayer/stride-84fhb.md)
  The stride vector.

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

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcslicelayer)*