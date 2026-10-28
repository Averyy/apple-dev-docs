# iw_desc

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The descriptor of the input weights.

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
var iw_desc: (BNNSNDArrayDescriptor, BNNSNDArrayDescriptor)
```

```c
BNNSNDArrayDescriptor iw_desc[2];
```

## Discussion

Weights are ordered as `[num_layers][num_directions][hidden_size][input_size]` (C style multi array notation).

`iw_desc` is duplicated for the case where `num_layers > 1 && input_size != hidden_size`.

## See Also

### Instance Properties
- [var hw_desc: BNNSNDArrayDescriptor](./hw_desc.md)
  The descriptor of the hidden weights.
- [var cw_desc: BNNSNDArrayDescriptor](./cw_desc.md)
  The descriptor of the cell weights.
- [var b_desc: BNNSNDArrayDescriptor](./b_desc.md)
  The descriptor of the bias.
- [var activation: BNNSActivation](./activation.md)
  The activation function that the layer applies to the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslstmgatedescriptor/iw_desc)*