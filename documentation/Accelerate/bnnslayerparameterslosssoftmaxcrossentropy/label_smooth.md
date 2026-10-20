# label_smooth

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A value that defines the smoothing that the loss function applies to the labels.

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
var label_smooth: Float
```

```c
float label_smooth;
```

## See Also

### Instance Properties
- [var function: BNNSLossFunction](./function.md)
  The function that’s used to compute loss.
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.
- [var reduction: BNNSLossReductionFunction](./reduction.md)
  The function that’s used to reduce the computed loss.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslosssoftmaxcrossentropy/label_smooth)*