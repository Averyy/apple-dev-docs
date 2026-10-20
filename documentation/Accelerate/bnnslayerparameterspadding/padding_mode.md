# padding_mode

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The mode the operation uses to pad.

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
var padding_mode: BNNSPaddingMode
```

```c
BNNSPaddingMode padding_mode;
```

## See Also

### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.
- [var padding_size: ((Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int))](./padding_size.md)
  The number of padding elements to add before and after the original data.
- [var padding_value: UInt32](./padding_value.md)
  The value the operation uses to fill the padding area when the mode is constant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspadding/padding_mode)*