# rnn(initialHiddenStates:inputHiddenWeight:hiddenHiddenWeight:bias:direction:activation:outputSequence:)

**Framework**: Accelerate  
**Kind**: method

Adds an RNN operation to the current graph.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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

- `initialHiddenStates`: The initial hidden states, with the shape  ,   that the operation uses in the second matrix multiplication above when computing  .
- `inputHiddenWeight`: The input-hidden weight with the shape  .
- `hiddenHiddenWeight`: The hidden-hidden weight with the shape  .
- `bias`: The bias (the sum of input-hidden and hidden-hidden biases) with the shape   .
- `direction`: An enumeration that specifies a forward or backward RNN.
- `activation`: An enumeration that controls the output activation function.
- `outputSequence`: When  ,   is of shape   and   contains hidden states from every step,  . When  ,   is of shape    and contains hidden states from the last step,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/rnn(initialhiddenstates:inputhiddenweight:hiddenhiddenweight:bias:direction:activation:outputsequence:))*