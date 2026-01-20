# MPSLSTMDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class

A description of a long short-term memory block or layer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSLSTMDescriptor
```

#### Overview

The recurrent neural network (RNN) layer initialized with [`MPSLSTMDescriptor`](mpslstmdescriptor.md) transforms the input data (image or matrix), the memory cell data, and previous output with a set of filters. Each produces one feature map in the output data and memory cell according to the long short-term memory (LSTM) formula detailed below.

You may provide the LSTM unit with a single input or a sequence of inputs.

##### Description of Operation

1. Let `x_j` be the input data (at time index `t` of sequence, `j` index containing quadruplet: batch index, `x`,`y` and feature index (`x = y = 0` for matrices)).
2. Let `h0_j` be the recurrent input (previous output) data from previous time step (at time index `t-1` of sequence).
3. Let `h1_i` be the output data produced at this time step.
4. Let `c0_j` be the previous memory cell data (at time index `t-1` of sequence).
5. Let `c1_i` be the new memory cell data (at time index `t-1` of sequence).
6. Let `Wi_ij`, `Ui_ij`, `Vi_ij` be the input gate weights for input, recurrent input, and memory cell (peephole) data, respectively.
7. Let `bi_i` be the bias for the input gate.
8. Let `Wf_ij`, `Uf_ij`, `Vf_ij` be the forget gate weights for input, recurrent input, and memory cell data, respectively.
9. Let `bf_i` be the bias for the forget gate.
10. Let `Wo_ij`, `Uo_ij`, `Vo_ij` be the output gate weights for input, recurrent input, and memory cell data, respectively.
11. Let `bo_i` be the bias for the output gate.
12. Let `Wc_ij`, `Uc_ij`, `Vc_ij` be the memory cell gate weights for input, recurrent input, and memory cell data, respectively.
13. Let `bc_i` be the bias for the memory cell gate.
14. Let `gi(x)`, `gf(x)`, `go(x)`, `gc(x)` be the neuron activation function for the input, forget, output gate, and memory cell gate.
15. Let `gh(x)` be the activation function applied to result memory cell data.

The output of the LSTM layer is computed as follows:

```other
I_i = gi(  Wi_ij * x_j  +  Ui_ij * h0_j  +  Vi_ij * c0_j  + bi_i  )
F_i = gf(  Wf_ij * x_j  +  Uf_ij * h0_j  +  Vf_ij * c0_j  + bf_i  )
C_i = gc(  Wc_ij * x_j  +  Uc_ij * h0_j  +  Vc_ij * c0_j  + bc_i  )

c1_i = F_i c0_i  +  I_i C_i

O_i = go(  Wo_ij * x_j  +  Uo_ij * h0_j  +  Vo_ij * c1_j  + bo_i  )
h1_i = O_i gh( c1_i )
```

The `*` stands for convolution (see [`MPSRNNImageInferenceLayer`](mpsrnnimageinferencelayer.md)) or matrix-vector/matrix multiplication (see [`MPSRNNMatrixInferenceLayer`](mpsrnnmatrixinferencelayer.md)).

Summation is over index `j` (except for the batch index), but there’s no summation over repeated index `i` (the output index).

Note that for validity, all intermediate images must be of same size, and all `U` and `V` matrices must be square (that is, [`outputFeatureChannels`](mpsrnndescriptor/outputfeaturechannels.md) == [`inputFeatureChannels`](mpsrnndescriptor/inputfeaturechannels.md)). Also, the bias terms are scalars with regard to spatial dimensions.

## Topics

### Instance Properties
- [var cellGateInputWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/cellgateinputweights.md)
- [var cellGateMemoryWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/cellgatememoryweights.md)
- [var cellGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/cellgaterecurrentweights.md)
- [var cellToOutputNeuronParamA: Float](mpslstmdescriptor/celltooutputneuronparama.md)
- [var cellToOutputNeuronParamB: Float](mpslstmdescriptor/celltooutputneuronparamb.md)
- [var cellToOutputNeuronType: MPSCNNNeuronType](mpslstmdescriptor/celltooutputneurontype.md)
- [enum MPSCNNNeuronType](mpscnnneurontype.md)
  The types of neuron filter to append to a convolution.
- [var forgetGateInputWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/forgetgateinputweights.md)
- [var forgetGateMemoryWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/forgetgatememoryweights.md)
- [var forgetGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/forgetgaterecurrentweights.md)
- [var inputGateInputWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/inputgateinputweights.md)
- [var inputGateMemoryWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/inputgatememoryweights.md)
- [var inputGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/inputgaterecurrentweights.md)
- [var memoryWeightsAreDiagonal: Bool](mpslstmdescriptor/memoryweightsarediagonal.md)
- [var outputGateInputWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/outputgateinputweights.md)
- [var outputGateMemoryWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/outputgatememoryweights.md)
- [var outputGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](mpslstmdescriptor/outputgaterecurrentweights.md)
- [protocol MPSCNNConvolutionDataSource](mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [var cellToOutputNeuronParamC: Float](mpslstmdescriptor/celltooutputneuronparamc.md)
### Type Methods
- [class func createLSTMDescriptor(withInputFeatureChannels: Int, outputFeatureChannels: Int) -> Self](mpslstmdescriptor/createlstmdescriptor(withinputfeaturechannels:outputfeaturechannels:).md)

## Relationships

### Inherits From
- [MPSRNNDescriptor](mpsrnndescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSRNNImageInferenceLayer](mpsrnnimageinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders images.
- [class MPSRNNMatrixInferenceLayer](mpsrnnmatrixinferencelayer.md)
  A recurrent neural network layer for inference on Metal Performance Shaders matrices.
- [class MPSRNNSingleGateDescriptor](mpsrnnsinglegatedescriptor.md)
  A description of a simple recurrent block or layer.
- [class MPSGRUDescriptor](mpsgrudescriptor.md)
  A description of a gated recurrent unit block or layer.
- [enum MPSRNNSequenceDirection](mpsrnnsequencedirection.md)
  Directions that a sequence of inputs can be processed by a recurrent neural network layer.
- [class MPSRNNMatrixTrainingLayer](mpsrnnmatrixtraininglayer.md)
  A layer for training recurrent neural networks on Metal Performance Shaders matrices.
- [class MPSRNNMatrixTrainingState](mpsrnnmatrixtrainingstate.md)
  A class that holds data from a forward pass to be used in a backward pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpslstmdescriptor)*