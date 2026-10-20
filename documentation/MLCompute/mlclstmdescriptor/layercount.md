# layerCount

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The number of recurrent layers.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var layerCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger layerCount;
```

## See Also

### Inspecting LSTM Descriptors
- [var batchFirst: Bool](./batchfirst.md)
  A Boolean that indicates whether the input and output shape is batch first.
- [var dropout: Float](./dropout.md)
  The dropout probability.
- [var hiddenSize: Int](./hiddensize.md)
  The number of features in the hidden state.
- [var inputSize: Int](./inputsize.md)
  The number of expected features in the input.
- [var isBidirectional: Bool](./isbidirectional.md)
  A Boolean that indicates whether the layer is bidirectional.
- [var resultMode: MLCLSTMResultMode](./resultmode.md)
  The mode that indicates whether the layer produces a single result tensor or three result tensors — final output, last hidden state, and the cell state.
- [var returnsSequences: Bool](./returnssequences.md)
  A Boolean that indicates whether the layer returns output for all sequences.
- [var usesBiases: Bool](./usesbiases.md)
  A Boolean that indicates whether you use bias weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmdescriptor/layercount)*