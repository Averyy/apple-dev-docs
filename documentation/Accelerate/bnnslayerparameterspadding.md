# BNNSLayerParametersPadding

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of a padding layer.

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
struct BNNSLayerParametersPadding
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, padding_size: ((Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int)), padding_mode: BNNSPaddingMode, padding_value: UInt32)](bnnslayerparameterspadding/init(i_desc:o_desc:padding_size:padding_mode:padding_value:).md)
  Returns a new padding-layer parameters structure from the specified parameters.
- [init()](bnnslayerparameterspadding/init.md)
  Returns a new padding-layer parameters structure.
### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparameterspadding/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparameterspadding/o_desc.md)
  The descriptor of the output.
- [var padding_size: ((Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int))](bnnslayerparameterspadding/padding_size.md)
  The number of padding elements to add before and after the original data.
- [var padding_mode: BNNSPaddingMode](bnnslayerparameterspadding/padding_mode.md)
  The mode the operation uses to pad.
- [var padding_value: UInt32](bnnslayerparameterspadding/padding_value.md)
  The value the operation uses to fill the padding area when the mode is constant.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class PaddingLayer](bnns/paddinglayer.md)
  A layer object that wraps a padding filter and manages its deinitialization.
- [struct BNNSPaddingMode](bnnspaddingmode.md)
  Constants that define padding modes.
- [func BNNSFilterCreateLayerPadding(UnsafePointer<BNNSLayerParametersPadding>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerpadding(_:_:).md)
  Returns a new loss layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspadding)*