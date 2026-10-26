# MLCReshapeLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that reshapes a tensor with the shape you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCReshapeLayer
```

```objc
@interface MLCReshapeLayer : MLCLayer
```

## Topics

### Creating Reshape Layers
- [convenience init?(shape: [Int])](./mlcreshapelayer/init%28shape%29.md)
  Creates a reshape layer with the shape you specify.
### Inspecting Reshape Layers
- [var shape: [Int]](./mlcreshapelayer/shape-8k50y.md)
  An array that contains the size of each dimension.
- [shape](./mlcreshapelayer/shape-840ax.md)
  An array that contains the size of each dimension.
### Type Methods
- [+ layerWithShape:](./mlcreshapelayer/layerwithshape_.md)
  Creates a reshape layer with the shape you specify.

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
- [class MLCSliceLayer](./mlcslicelayer.md)
  A layer that extracts a slice from a tensor.
- [class MLCSplitLayer](./mlcsplitlayer.md)
  A layer that splits a tensor value into a list of subtensors.
- [class MLCPaddingLayer](./mlcpaddinglayer.md)
  A layer that pads a tensor with the padding sizes you specify.
- [class MLCScatterLayer](./mlcscatterlayer.md)
  A layer that updates the output at an index you specify.
- [class MLCSelectionLayer](./mlcselectionlayer.md)
  A layer for selecting elements from two tensors.
- [class MLCGatherLayer](./mlcgatherlayer.md)
  A layer that fetches data at the locations you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcreshapelayer)*