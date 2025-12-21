# lstm(initialHiddenStates:initialCellStates:inputHiddenWeight:hiddenHiddenWeight:bias:direction:activation:recurrentActivation:cellActivation:outputSequence:)

**Framework**: Accelerate  
**Kind**: method

Adds an LSTM operation to the current graph.

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
func lstm(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, initialCellStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, direction: BNNSGraph.Builder.Direction, activation: BNNSGraph.Builder.Activation, recurrentActivation: BNNSGraph.Builder.Activation, cellActivation: BNNSGraph.Builder.Activation, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>, memoryStates: BNNSGraph.Builder.Tensor<T>)
```

#### Discussion

For each time t from 0 to L-1, this operation computes the following:

Input gate:

```None
i[t, ...] = RA(matmul(W_ii, x[t, ...]) + b_ii + matmul(W_hi, h[t-1, ...]) + b_hi)
```

Forget gate:

```None
f[t, ...] = RA(matmul(W_if, x[t, ...]) + b_if + matmul(W_hf, h[t-1, ...]) + b_hf)
```

Cell gate:

```None
g[t, ...] = CA(matmul(W_ig, x[t, ...]) + b_ig + matmul(W_hg, h[t-1, ...]) + b_hg)
```

Output gate:

```None
o[t, ...] = RA(matmul(W_io, x[t, ...]) + b_io + matmul(W_ho, h[t-1, ...]) + b_ho)
```

Cell state:

```None
c[t, ...] = f[t, ...] * c[t-1, ...] + i[t, ...] * g[t, ...]
```

Hidden state:

```None
h[t, ...] = o[t, ...] * A(c[t, ...])
```

where:

- `A` is the `activation` function
- `RA` is the `recurrentActivation` function
- `CA` is the `cellActivation` function
- `inputHiddenWeight = concat(W_ii, W_if, W_io, W_ig, axis=-2)`
- `hiddenHiddenWeight = concat(W_hi, W_hf, W_ho, W_hg, axis=-2)`
- `bias = concat(b_ii + b_hi, b_if + b_hf, b_ig + b_hg, b_io + b_ho, axis=-1)`
- `initialHiddenStates` is used for `h[t-1, ...]` at the first step
- `initialCellStates` is used for `c[t-1, ...]` at the first step
- `*` denotes the Hadamard/elementwise product

The input tensor `x` is of shape `(L, N, Hin)`

`hiddenStates` is of shape `(N, Hout)` and contains hidden states from the last step, `h[-1, ...]`

`memoryStates` is of shape `(N, Hout)` and contains memory states from the last step, `c[-1, ...]`

- Parameter inputHiddenWeightL The input-hidden weight  with the shape `(4*Hout, Hin)`.

## Parameters

- `initialHiddenStates`: The initial hidden states  with the shape  .
- `initialCellStates`: The initial hidden states with the shape  .
- `hiddenHiddenWeight`: The hidden-hidden weight with the shape  .
- `bias`: The bias (the sum of input-hidden and hidden-hidden biases)  with the shape  .
- `direction`: An enumeration that specifies a forward or backward RNN.
- `activation`: An enumeration that controls the output activation function.
- `recurrentActivation`: An enumeration that controls the recurrent activation function.
- `cellActivation`: An enumeration that controls the cell activation function.
- `outputSequence`: When  ,   is of shape   and contains   hidden states from every step,  . When  ,   is of shape    and contains hidden states from the last step,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/lstm(initialhiddenstates:initialcellstates:inputhiddenweight:hiddenhiddenweight:bias:direction:activation:recurrentactivation:cellactivation:outputsequence:))*