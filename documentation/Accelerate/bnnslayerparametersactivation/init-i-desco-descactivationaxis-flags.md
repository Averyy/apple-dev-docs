# init(i_desc:o_desc:activation:axis_flags:)

**Framework**: Accelerate  
**Kind**: init

Returns a new activation layer parameters structure from the supplied descriptors, activation function, and axis flags.

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
init(i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, activation: BNNSActivation, axis_flags: UInt32)
```

#### Discussion

> ❗ **Important**:  The input dimensions must be equal to the output dimensions. For activation types other than identity, the input and output must be `float`.

## Parameters

- `i_desc`: The descriptor of the input.
- `o_desc`: The descriptor of the output.
- `activation`: The activation function that the layer applies to the output.
- `axis_flags`: Flags that indicate axes on which the layer applies certain activation functions.

## See Also

- [init()](bnnslayerparametersactivation/init.md)
  Returns a new activation layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersactivation/init(i_desc:o_desc:activation:axis_flags:))*