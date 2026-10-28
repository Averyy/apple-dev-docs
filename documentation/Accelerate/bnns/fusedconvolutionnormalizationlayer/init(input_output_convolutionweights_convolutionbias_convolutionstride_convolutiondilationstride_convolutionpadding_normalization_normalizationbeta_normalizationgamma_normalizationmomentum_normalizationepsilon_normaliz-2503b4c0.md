# init(input:output:convolutionWeights:convolutionBias:convolutionStride:convolutionDilationStride:convolutionPadding:normalization:normalizationBeta:normalizationGamma:normalizationMomentum:normalizationEpsilon:normalizationActivation:filterParameters:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new fused, convolution normalization layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, convolutionWeights: BNNSNDArrayDescriptor, convolutionBias: BNNSNDArrayDescriptor?, convolutionStride: (x: Int, y: Int), convolutionDilationStride: (x: Int, y: Int), convolutionPadding: BNNS.ConvolutionPadding, normalization: BNNS.NormalizationType, normalizationBeta: BNNSNDArrayDescriptor, normalizationGamma: BNNSNDArrayDescriptor, normalizationMomentum: Float, normalizationEpsilon: Float, normalizationActivation: BNNS.ActivationFunction, filterParameters: BNNSFilterParameters? = nil)
```

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `convolutionWeights`: The descriptor of the convolution weights.
- `convolutionBias`: The descriptor of the convolution bias.
- `convolutionStride`: The width and height increments of the input image.
- `convolutionDilationStride`: The width and height increments between elements in the input image during convolution.
- `convolutionPadding`: The padding, which is the number of virtual zeros added to the sides of each channel.
- `normalization`: An enumeration that specifies the normalization type.
- `normalizationBeta`: The descriptor of the normalization beta.
- `normalizationGamma`: The descriptor of the normalization gamma.
- `normalizationMomentum`: A value between 0 and 1 that the normalization operation uses to update the moving mean and moving variance during training.
- `normalizationEpsilon`: The epsilon in the computation of the standard deviation.
- `normalizationActivation`: The activation function that the layer applies to the output.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedconvolutionnormalizationlayer/init%28input:output:convolutionweights:convolutionbias:convolutionstride:convolutiondilationstride:convolutionpadding:normalization:normalizationbeta:normalizationgamma:normalizationmomentum:normalizationepsilon:normalizationactivation:filter-30cwy)*