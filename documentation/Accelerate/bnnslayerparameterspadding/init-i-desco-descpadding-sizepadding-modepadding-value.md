# init(i_desc:o_desc:padding_size:padding_mode:padding_value:)

**Framework**: Accelerate  
**Kind**: init

Returns a new padding-layer parameters structure from the specified parameters.

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
init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, padding_size: ((Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int), (Int, Int)), padding_mode: BNNSPaddingMode, padding_value: UInt32)
```

#### Discussion

> ❗ **Important**:  Padding isn’t supported beyond 4D tensors.

## Parameters

- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `padding_size`: The number of padding elements to add before and after the original data.
- `padding_mode`: The mode the operation uses to pad.
- `padding_value`: The value the operation uses to fill the padding area when the mode is constant.

## See Also

- [init()](bnnslayerparameterspadding/init.md)
  Returns a new padding-layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterspadding/init(i_desc:o_desc:padding_size:padding_mode:padding_value:))*