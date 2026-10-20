# outputGateInputGateWeights

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
var outputGateInputGateWeights: (any MPSCNNConvolutionDataSource)? { get set }
```

```objc
@property (nonatomic, retain, readwrite, nullable) id<MPSCNNConvolutionDataSource> outputGateInputGateWeights;
```

## See Also

### Instance Properties
- [var flipOutputGates: Bool](./flipoutputgates.md)
- [var gatePnormValue: Float](./gatepnormvalue.md)
- [var inputGateInputWeights: (any MPSCNNConvolutionDataSource)?](./inputgateinputweights.md)
- [var inputGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](./inputgaterecurrentweights.md)
- [var outputGateInputWeights: (any MPSCNNConvolutionDataSource)?](./outputgateinputweights.md)
- [var outputGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](./outputgaterecurrentweights.md)
- [var recurrentGateInputWeights: (any MPSCNNConvolutionDataSource)?](./recurrentgateinputweights.md)
- [var recurrentGateRecurrentWeights: (any MPSCNNConvolutionDataSource)?](./recurrentgaterecurrentweights.md)
- [protocol MPSCNNConvolutionDataSource](../mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsgrudescriptor/outputgateinputgateweights)*