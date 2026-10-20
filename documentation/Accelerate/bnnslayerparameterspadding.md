# BNNSLayerParametersPadding

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters of a padding layer.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
struct BNNSLayerParametersPadding
```

```c
typedef struct { ... } BNNSLayerParametersPadding;
```

## Topics

### Initializers
- [init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, padding_size: ((Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int)), padding_mode: BNNSPaddingMode, padding_value: UInt32)](./bnnslayerparameterspadding/init%28i_desc,o_desc,padding_size,padding_mode,padding_value%29.md)
  Returns a new padding-layer parameters structure from the specified parameters.
- [init()](./bnnslayerparameterspadding/init%28%29.md)
  Returns a new padding-layer parameters structure.
### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](./bnnslayerparameterspadding/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./bnnslayerparameterspadding/o_desc.md)
  The descriptor of the output.
- [var padding_size: ((Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int))](./bnnslayerparameterspadding/padding_size.md)
  The number of padding elements to add before and after the original data.
- [var padding_mode: BNNSPaddingMode](./bnnslayerparameterspadding/padding_mode.md)
  The mode the operation uses to pad.
- [var padding_value: UInt32](./bnnslayerparameterspadding/padding_value.md)
  The value the operation uses to fill the padding area when the mode is constant.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Padding layers
- [class PaddingLayer](./bnns/paddinglayer.md)
  A layer object that wraps a padding filter and manages its deinitialization.
- [struct BNNSPaddingMode](./bnnspaddingmode.md)
  Constants that define padding modes.
- [func BNNSFilterCreateLayerPadding(UnsafePointer<BNNSLayerParametersPadding>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerpadding%28_,_%29.md)
  Returns a new loss layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspadding)*