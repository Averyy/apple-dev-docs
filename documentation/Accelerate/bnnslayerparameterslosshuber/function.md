# function

**Framework**: Accelerate  
**Kind**: property

The function that’s used to compute loss.

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
var function: BNNSLossFunction
```

## See Also

- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparameterslosshuber/i_desc.md)
  The descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparameterslosshuber/o_desc.md)
  The descriptor of the output.
- [var reduction: BNNSLossReductionFunction](bnnslayerparameterslosshuber/reduction.md)
  The function that’s used to reduce the computed loss.
- [var huber_delta: Float](bnnslayerparameterslosshuber/huber_delta.md)
  The boundary value that defines where Huber loss returns mean absolute error or mean square error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparameterslosshuber/function)*