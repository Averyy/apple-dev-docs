# dropout

**Framework**: ML Compute  
**Kind**: property

The dropout probability.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var dropout: Float { get }
```

#### Discussion

If `dropout` is non-zero, the layer adds a dropout layer to the outputs of each layer except the last, with the dropout rate equal to `dropout`.

## See Also

- [var batchFirst: Bool](mlclstmdescriptor/batchfirst.md)
  A Boolean that indicates whether the input and output shape is batch first.
- [var hiddenSize: Int](mlclstmdescriptor/hiddensize.md)
  The number of features in the hidden state.
- [var inputSize: Int](mlclstmdescriptor/inputsize.md)
  The number of expected features in the input.
- [var isBidirectional: Bool](mlclstmdescriptor/isbidirectional.md)
  A Boolean that indicates whether the layer is bidirectional.
- [var layerCount: Int](mlclstmdescriptor/layercount.md)
  The number of recurrent layers.
- [var resultMode: MLCLSTMResultMode](mlclstmdescriptor/resultmode.md)
  The mode that indicates whether the layer produces a single result tensor or three result tensors — final output, last hidden state, and the cell state.
- [var returnsSequences: Bool](mlclstmdescriptor/returnssequences.md)
  A Boolean that indicates whether the layer returns output for all sequences.
- [var usesBiases: Bool](mlclstmdescriptor/usesbiases.md)
  A Boolean that indicates whether you use bias weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclstmdescriptor/dropout)*