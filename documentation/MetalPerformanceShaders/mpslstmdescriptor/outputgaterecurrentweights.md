# outputGateRecurrentWeights

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var outputGateRecurrentWeights: (any MPSCNNConvolutionDataSource)? { get set }
```

```objc
@property (nonatomic, retain, readwrite, nullable) id<MPSCNNConvolutionDataSource> outputGateRecurrentWeights;
```

## See Also

### Instance Properties
- [var cellGateInputWeights: (any MPSCNNConvolutionDataSource)?](./cellgateinputweights.md)
- [var cellGateMemoryWeights: (any MPSCNNConvolutionDataSource)?](./cellgatememoryweights.md)
- [var cellGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](./cellgaterecurrentweights.md)
- [var cellToOutputNeuronParamA: Float](./celltooutputneuronparama.md)
- [var cellToOutputNeuronParamB: Float](./celltooutputneuronparamb.md)
- [var cellToOutputNeuronType: MPSCNNNeuronType](./celltooutputneurontype.md)
- [enum MPSCNNNeuronType](../mpscnnneurontype.md)
  The types of neuron filter to append to a convolution.
- [var forgetGateInputWeights: (any MPSCNNConvolutionDataSource)?](./forgetgateinputweights.md)
- [var forgetGateMemoryWeights: (any MPSCNNConvolutionDataSource)?](./forgetgatememoryweights.md)
- [var forgetGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](./forgetgaterecurrentweights.md)
- [var inputGateInputWeights: (any MPSCNNConvolutionDataSource)?](./inputgateinputweights.md)
- [var inputGateMemoryWeights: (any MPSCNNConvolutionDataSource)?](./inputgatememoryweights.md)
- [var inputGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](./inputgaterecurrentweights.md)
- [var memoryWeightsAreDiagonal: Bool](./memoryweightsarediagonal.md)
- [var outputGateInputWeights: (any MPSCNNConvolutionDataSource)?](./outputgateinputweights.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpslstmdescriptor/outputgaterecurrentweights)*