# bidirectionalLSTM(initialHiddenStates:initialCellStates:inputHiddenWeight:hiddenHiddenWeight:bias:inputHiddenWeightBack:hiddenHiddenWeightBack:biasBack:activation:recurrentActivation:cellActivation:outputSequence:)

**Framework**: Accelerate  
**Kind**: method

Adds a bidirectional LSTM operation to the current graph.

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
func bidirectionalLSTM(initialHiddenStates: BNNSGraph.Builder.Tensor<T>, initialCellStates: BNNSGraph.Builder.Tensor<T>, inputHiddenWeight: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeight: BNNSGraph.Builder.Tensor<T>, bias: BNNSGraph.Builder.Tensor<T>, inputHiddenWeightBack: BNNSGraph.Builder.Tensor<T>, hiddenHiddenWeightBack: BNNSGraph.Builder.Tensor<T>, biasBack: BNNSGraph.Builder.Tensor<T>, activation: BNNSGraph.Builder.Activation, recurrentActivation: BNNSGraph.Builder.Activation, cellActivation: BNNSGraph.Builder.Activation, outputSequence: Bool) -> (output: BNNSGraph.Builder.Tensor<T>, hiddenStates: BNNSGraph.Builder.Tensor<T>, memoryStates: BNNSGraph.Builder.Tensor<T>)
```

#### Discussion

The input tensor `x` is of shape `(L, N, Hin)`

- Parameter hiddenHiddenWeight The hidden-hidden weight with the shape `(4*Hout, Hout)`.

`hiddenStates` is of shape `(N, 2*Hout)` and contains hidden states from the last step, `h[-1, ...]`

`memoryStates` is of shape `(N, 2*Hout)` and contains memory states from the last step, `c[-1, ...]`

> **Note**: [`lstm(initialHiddenStates:initialCellStates:inputHiddenWeight:hiddenHiddenWeight:bias:direction:activation:recurrentActivation:cellActivation:outputSequence:)`](bnnsgraph/builder/tensor/lstm(initialhiddenstates:initialcellstates:inputhiddenweight:hiddenhiddenweight:bias:direction:activation:recurrentactivation:cellactivation:outputsequence:).md)

## Parameters

- `initialHiddenStates`: The initial hidden states with the shape `(N, 2*Hout)`.
- `initialCellStates`: The initial hidden states with the shape `(N, 2*Hout)`.
- `inputHiddenWeight`: The input-hidden weight with the shape `(4*Hout, Hin)`.
- `bias`: The bias (the sum of input-hidden and hidden-hidden biases)  with the shape `(4*Hout,)`.
- `inputHiddenWeightBack`: The backward input-hidden weight with the shape `(4*Hout, Hin)`.
- `hiddenHiddenWeightBack`: The backward hidden-hidden weight with the shape `(4*Hout, Hout)`.
- `biasBack`: The backward bias (the sum of input-hidden and hidden-hidden biases)  with the shape`(4*Hout,)`.
- `activation`: An enumeration that controls the output activation function.
- `recurrentActivation`: An enumeration that controls the recurrent activation function.
- `cellActivation`: An enumeration that controls the cell activation function.
- `outputSequence`: When `true`, `output` is of shape `(L, N, 2*Hout)` and contains hidden states from every step, `h[:, ...]`. When `false`, ` output` is of shape `(1, N, 2*Hout)` and contains hidden states from the last step, `h[-1, ...]`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/builder/tensor/bidirectionallstm(initialhiddenstates:initialcellstates:inputhiddenweight:hiddenhiddenweight:bias:inputhiddenweightback:hiddenhiddenweightback:biasback:activation:recurrentactivation:cellactivation:outputsequence:))*