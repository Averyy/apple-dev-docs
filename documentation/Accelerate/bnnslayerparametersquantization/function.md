# function

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The quantize function.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- tvOS 15.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 8.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
var function: BNNSQuantizerFunction
```

```c
BNNSQuantizerFunction function;
```

## See Also

### Instance Properties
- [var axis_mask: Int](./axis_mask.md)
  A bitmask that defines the axis  to which the function applies scale and bias.
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.
- [var scale: BNNSNDArrayDescriptor](./scale.md)
  The descriptor of the scale.
- [var bias: BNNSNDArrayDescriptor](./bias.md)
  The descriptor of the bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersquantization/function)*