# MLCSplitLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that splits a tensor value into a list of subtensors.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCSplitLayer
```

```objc
@interface MLCSplitLayer : MLCLayer
```

## Topics

### Creating Split Layers
- [convenience init(splitCount: Int, dimension: Int)](./mlcsplitlayer/init%28splitcount,dimension%29.md)
  Creates a split layer with the number of splits and dimension you specify.
- [convenience init(splitSectionLengths: [Int], dimension: Int)](./mlcsplitlayer/init%28splitsectionlengths,dimension%29.md)
  Creates a split layer with the lengths of each split section and dimension you specify.
### Inspecting Split Layers
- [var dimension: Int](./mlcsplitlayer/dimension.md)
  The dimension or axis along which to split the tensor.
- [var splitCount: Int](./mlcsplitlayer/splitcount.md)
  The number of splits.
- [var splitSectionLengths: [Int]?](./mlcsplitlayer/splitsectionlengths-5abch.md)
  An array that contains the lengths of each split section.

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
- [class MLCPaddingLayer](./mlcpaddinglayer.md)
  A layer that pads a tensor with the padding sizes you specify.
- [class MLCScatterLayer](./mlcscatterlayer.md)
  A layer that updates the output at an index you specify.
- [class MLCSelectionLayer](./mlcselectionlayer.md)
  A layer for selecting elements from two tensors.
- [class MLCGatherLayer](./mlcgatherlayer.md)
  A layer that fetches data at the locations you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsplitlayer)*