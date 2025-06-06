# axis_mask

**Framework**: Accelerate  
**Kind**: property

A bitmask that defines the axis  to which the function applies scale and bias.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var axis_mask: Int
```

#### Discussion

Set to `0` to apply scale and bias to the entire tensor.

## See Also

- [var function: BNNSQuantizerFunction](bnnslayerparametersquantization/function.md)
  The quantize function.
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersquantization/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersquantization/o_desc.md)
  The descriptor of the output.
- [var scale: BNNSNDArrayDescriptor](bnnslayerparametersquantization/scale.md)
  The descriptor of the scale.
- [var bias: BNNSNDArrayDescriptor](bnnslayerparametersquantization/bias.md)
  The descriptor of the bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersquantization/axis_mask)*