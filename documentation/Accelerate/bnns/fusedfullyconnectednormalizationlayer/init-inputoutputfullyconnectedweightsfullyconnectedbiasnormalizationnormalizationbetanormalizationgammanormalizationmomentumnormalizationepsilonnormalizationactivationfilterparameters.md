# init(input:output:fullyConnectedWeights:fullyConnectedBias:normalization:normalizationBeta:normalizationGamma:normalizationMomentum:normalizationEpsilon:normalizationActivation:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new fused, fully connected normalization layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fullyConnectedWeights: BNNSNDArrayDescriptor, fullyConnectedBias: BNNSNDArrayDescriptor?, normalization: BNNS.NormalizationType, normalizationBeta: BNNSNDArrayDescriptor, normalizationGamma: BNNSNDArrayDescriptor, normalizationMomentum: Float, normalizationEpsilon: Float, normalizationActivation: BNNS.ActivationFunction, filterParameters: BNNSFilterParameters? = nil)
```

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `fullyConnectedWeights`: The descriptor of the fully connected weights.
- `fullyConnectedBias`: The descriptor of the fully connected bias.
- `normalization`: An enumeration that specifies the normalization type.
- `normalizationBeta`: The descriptor of the normalization beta.
- `normalizationGamma`: The descriptor of the normalization gamma.
- `normalizationMomentum`: A value between 0 and 1 that the normalization operation uses to update the moving mean and moving variance during training.
- `normalizationEpsilon`: The epsilon in the computation of the standard deviation.
- `normalizationActivation`: The activation function that the layer applies to the output.
- `filterParameters`: The runtime filter parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedfullyconnectednormalizationlayer/init(input:output:fullyconnectedweights:fullyconnectedbias:normalization:normalizationbeta:normalizationgamma:normalizationmomentum:normalizationepsilon:normalizationactivation:filterparameters:))*