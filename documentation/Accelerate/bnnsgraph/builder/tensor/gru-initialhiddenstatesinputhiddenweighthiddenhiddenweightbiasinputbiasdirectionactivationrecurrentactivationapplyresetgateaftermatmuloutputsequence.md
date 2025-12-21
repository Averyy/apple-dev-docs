# gru(initialHiddenStates:inputHiddenWeight:hiddenHiddenWeight:bias:inputBias:direction:activation:recurrentActivation:applyResetGateAfterMatMul:outputSequence:)

**Framework**: Accelerate  
**Kind**: method

Adds a GRU operation to the current graph.

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
func gru(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, inputBias: BNNSGraph.Builder.Tensor<T>, direction: BNNSGraph.Builder.Direction, activation: BNNSGraph.Builder.Activation, recurrentActivation: BNNSGraph.Builder.Activation, applyResetGateAfterMatMul: Bool, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>)
```

#### Discussion

If `applyResetGateAfterMatMul` is false, For each time `t`, from `0` to `L-1`, computes:

Reset gate:

```None
r[t, ...] = RA(matmul(W_ir, x[t, ...]) + b_ir + matmul(W_hr, h[t-1, ...]) + b_hr)
```

Update gate:

```None
z[t, ...] = RA(matmul(W_iz, x[t, ...]) + b_iz + matmul(W_hz, h[t-1, ...]) + b_hz)
```

New gate:

```None
n[t, ...] =  A(matmul(W_in, x[t, ...]) + b_in + matmul(W_hn, h[t-1, ...]) * r[t, ...] + b_hn)
```

Hidden state:

```None
h[t, ...] = (1 - z[t, ...]) * n[t, ...] + z[t, ...] * h[t-1, ...]
```

Where:

- `A` is the `activation` function,
- `RA` is the `recurrentActivation` function,
- `inputHiddenWeight = concat(W_ir, W_in, W_iz, axis=-2)`
- `hiddenHiddenWeight = concat(W_hr, W_hn, W_hz, axis=-2)`
- `bias = concat(b_hr, b_hn, b_hz, axis=-1)`,
- `inputBias = concat(b_ir, b_in, b_iz, axis=-1`
- `initialHiddenStates` is used for `h[t-1, ...]`at the first step
- `*` denotes the Hadamard/elementwise product

If `applyResetGateAfterMatMul` is `true`, the calculation for the new gate changes to

New gate:

```None
n[t, ...] =  A(matmul(W_in, x[t, ...]) + b_in + (matmul(W_hn, h[t-1, ...]) + b_hn) * r[t, ...])
```

The input tensor `x` is of shape `(L, N, Hin)`

`hiddenStates` is of shape `(N, Hout)` and contains hidden states from the last step, `h[-1, ...]`.

## Parameters

- `initialHiddenStates`: The initial hidden states with the shape  .
- `inputHiddenWeight`: The input-hidden weight with the shape  .
- `hiddenHiddenWeight`: The hidden-hidden weight with the shape  .
- `bias`: The bias (the sum of input-hidden and hidden-hidden biases) with the shape   .
- `inputBias`: Used when   is  , and is the same shape as  .
- `direction`: An enumeration that specifies a forward or reverse GRU op. Reverse GRU computes time steps in the reverse direction.
- `activation`: An enumeration that controls the output activation function.
- `recurrentActivation`: An enumeration that controls the recurrent activation function.
- `applyResetGateAfterMatMul`: An enumeration that specifies that the reset gate is applied after the matrix multiply.
- `outputSequence`: When   ,   is of shape   and contains hidden states from every step,  . When     is of shape   and contains hidden states from the last step,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/gru(initialhiddenstates:inputhiddenweight:hiddenhiddenweight:bias:inputbias:direction:activation:recurrentactivation:applyresetgateaftermatmul:outputsequence:))*