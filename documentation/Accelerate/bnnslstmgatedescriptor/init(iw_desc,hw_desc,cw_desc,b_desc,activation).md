# init(iw_desc:hw_desc:cw_desc:b_desc:activation:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new long short-term memory (LSTM) gate descriptor structure from the specified parameters.

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
init(iw_desc: (BNNSNDArrayDescriptor, BNNSNDArrayDescriptor), hw_desc: BNNSNDArrayDescriptor, cw_desc: BNNSNDArrayDescriptor, b_desc: BNNSNDArrayDescriptor, activation: BNNSActivation)
```

## Parameters

- `iw_desc`: The descriptor of the input weights.
- `hw_desc`: The descriptor of the hidden weights.
- `cw_desc`: The descriptor of the cell weights.
- `b_desc`: The descriptor of the bias.
- `activation`: The activation function that the layer applies to the output.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Returns a new long short-term memory (LSTM) gate descriptor structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslstmgatedescriptor/init(iw_desc:hw_desc:cw_desc:b_desc:activation:))*