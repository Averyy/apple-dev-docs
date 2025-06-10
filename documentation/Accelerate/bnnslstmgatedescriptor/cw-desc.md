# cw_desc

**Framework**: Accelerate  
**Kind**: property

The descriptor of the cell weights.

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
var cw_desc: BNNSNDArrayDescriptor
```

#### Discussion

Weights are ordered as `[num_layers][num_directions][hidden_size][hidden_size]` (C style multi array notation).

## See Also

- [var iw_desc: (BNNSNDArrayDescriptor, BNNSNDArrayDescriptor)](bnnslstmgatedescriptor/iw_desc.md)
  The descriptor of the input weights.
- [var hw_desc: BNNSNDArrayDescriptor](bnnslstmgatedescriptor/hw_desc.md)
  The descriptor of the hidden weights.
- [var b_desc: BNNSNDArrayDescriptor](bnnslstmgatedescriptor/b_desc.md)
  The descriptor of the bias.
- [var activation: BNNSActivation](bnnslstmgatedescriptor/activation.md)
  The activation function that the layer applies to the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslstmgatedescriptor/cw_desc)*