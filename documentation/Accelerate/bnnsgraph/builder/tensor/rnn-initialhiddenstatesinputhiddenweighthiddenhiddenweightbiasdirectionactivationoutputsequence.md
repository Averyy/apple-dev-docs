# rnn(initialHiddenStates:inputHiddenWeight:hiddenHiddenWeight:bias:direction:activation:outputSequence:)

**Framework**: Accelerate  
**Kind**: method

Adds an RNN operation to the current graph.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func rnn(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, direction: BNNSGraph.Builder.Direction, activation: BNNSGraph.Builder.Activation, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>)
```

#### Discussion

For each time `t`, from `0` to `L-1`, this operation performs the following:

```None
h[t, ...] = activation(matmul(x[t, ...], inputHiddenWeight^T) +
                       matmul(h[t-1, ...], hiddenHiddenWeight^T) +
                       bias)
```

The input tensor `x` is of shape `(L, N, Hin)`.

`hiddenStates` is of shape `(N, Hout)` and contains hidden states from the last step, `h[-1, ...]`.

## Parameters

- `initialHiddenStates`: The initial hidden states, with the shape `(N, Hout)`, that the operation uses in the second matrix multiplication above when computing `h[0, ...]`.
- `inputHiddenWeight`: The input-hidden weight with the shape `(Hout, Hin)`.
- `hiddenHiddenWeight`: The hidden-hidden weight with the shape `(Hout, Hout)`.
- `bias`: The bias (the sum of input-hidden and hidden-hidden biases) with the shape  `(Hout,)`.
- `direction`: An enumeration that specifies a forward or backward RNN.
- `activation`: An enumeration that controls the output activation function.
- `outputSequence`: When `true`, `output` is of shape `(L, N, Hout)` and contains hidden states from every step, `h[:, ...]`. When `false`, `output` is of shape `(1, N, Hout)` and contains hidden states from the last step, `h[-1, ...]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/rnn(initialhiddenstates:inputhiddenweight:hiddenhiddenweight:bias:direction:activation:outputsequence:))*