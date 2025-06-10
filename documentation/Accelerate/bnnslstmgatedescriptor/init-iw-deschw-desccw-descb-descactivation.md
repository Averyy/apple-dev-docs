# init(iw_desc:hw_desc:cw_desc:b_desc:activation:)

**Framework**: Accelerate  
**Kind**: init

Returns a new long short-term memory (LSTM) gate descriptor structure from the specified parameters.

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
init(iw_desc: (BNNSNDArrayDescriptor, BNNSNDArrayDescriptor), hw_desc: BNNSNDArrayDescriptor, cw_desc: BNNSNDArrayDescriptor, b_desc: BNNSNDArrayDescriptor, activation: BNNSActivation)
```

## Parameters

- `iw_desc`: The descriptor of the input weights.
- `hw_desc`: The descriptor of the hidden weights.
- `cw_desc`: The descriptor of the cell weights.
- `b_desc`: The descriptor of the bias.
- `activation`: The activation function that the layer applies to the output.

## See Also

- [init()](bnnslstmgatedescriptor/init.md)
  Returns a new long short-term memory (LSTM) gate descriptor structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslstmgatedescriptor/init(iw_desc:hw_desc:cw_desc:b_desc:activation:))*