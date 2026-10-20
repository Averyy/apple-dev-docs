# MLCPaddingLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that pads a tensor with the padding sizes you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCPaddingLayer
```

```objc
@interface MLCPaddingLayer : MLCLayer
```

## Topics

### Creating Padding Layers
- [convenience init(reflectionPadding: [Int])](./mlcpaddinglayer/init%28reflectionpadding%29.md)
  Creates a padding layer with the reflection padding sizes you specify.
- [convenience init(symmetricPadding: [Int])](./mlcpaddinglayer/init%28symmetricpadding%29.md)
  Creates a padding layer with the symmetric padding sizes you specify.
- [convenience init(zeroPadding: [Int])](./mlcpaddinglayer/init%28zeropadding%29.md)
  Creates a padding layer with the zero padding sizes you specify.
- [convenience init(constantPadding: [Int], constantValue: Float)](./mlcpaddinglayer/init%28constantpadding,constantvalue%29.md)
  Creates a padding layer with the constant padding sizes and constant value you specify.
### Inspecting Padding Layers
- [var paddingType: MLCPaddingType](./mlcpaddinglayer/paddingtype.md)
  The padding type.
- [var paddingLeft: Int](./mlcpaddinglayer/paddingleft.md)
  The left padding size.
- [var paddingRight: Int](./mlcpaddinglayer/paddingright.md)
  The right padding size.
- [var paddingTop: Int](./mlcpaddinglayer/paddingtop.md)
  The top padding size.
- [var paddingBottom: Int](./mlcpaddinglayer/paddingbottom.md)
  The bottom padding size.
- [var constantValue: Float](./mlcpaddinglayer/constantvalue.md)
  The constant value you use if padding type is constant.

## Relationships

### Inherits From
- [MLCLayer](./mlclayer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
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
- [class MLCScatterLayer](./mlcscatterlayer.md)
  A layer that updates the output at an index you specify.
- [class MLCSelectionLayer](./mlcselectionlayer.md)
  A layer for selecting elements from two tensors.
- [class MLCGatherLayer](./mlcgatherlayer.md)
  A layer that fetches data at the locations you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpaddinglayer)*