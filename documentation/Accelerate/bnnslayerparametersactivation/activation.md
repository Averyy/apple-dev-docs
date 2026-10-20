# activation

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The activation function that the layer applies to the output.

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
var activation: BNNSActivation
```

```c
BNNSActivation activation;
```

## See Also

### Instance Properties
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.
- [var axis_flags: UInt32](./axis_flags.md)
  Flags that indicate axes on which to apply certain activation functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersactivation/activation)*