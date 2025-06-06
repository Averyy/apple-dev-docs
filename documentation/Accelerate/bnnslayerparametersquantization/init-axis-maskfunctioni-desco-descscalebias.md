# init(axis_mask:function:i_desc:o_desc:scale:bias:)

**Framework**: Accelerate  
**Kind**: init

Returns a new quantization layer parameters structure using the supplied parameters.

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
init(axis_mask: Int, function: BNNSQuantizerFunction, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, scale: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor)
```

## Parameters

- `axis_mask`: A bitmask that defines the axis to which the function applies scale and bias. Set to   to apply scale and bias to the entire tensor.
- `function`: The quantize function.
- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `scale`: The descriptor of the scale.
- `bias`: The descriptor of the bias.

## See Also

- [init()](bnnslayerparametersquantization/init.md)
  Returns a new quantization layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersquantization/init(axis_mask:function:i_desc:o_desc:scale:bias:))*