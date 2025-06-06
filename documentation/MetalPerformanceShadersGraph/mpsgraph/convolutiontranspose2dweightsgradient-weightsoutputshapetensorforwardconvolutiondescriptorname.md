# convolutionTranspose2DWeightsGradient(_:weights:outputShapeTensor:forwardConvolutionDescriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a convolution transpose gradient operation with respect to the weights tensor of the convolution transpose operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func convolutionTranspose2DWeightsGradient(_ incomingGradientTensor: MPSGraphTensor, weights source: MPSGraphTensor, outputShapeTensor outputShape: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Inserts an operation in graph to compute gradient of convolution transpose with respect to the weights tensor of the corresponding convolution transpose operation.

## Parameters

- `incomingGradientTensor`: Incoming gradient tensor
- `source`: Forward pass source tensor
- `outputShape`: 1D Int32 or Int64 Tensor. Shape of the forward pass source weights tensor
- `forwardConvolutionDescriptor`: Forward pass op descriptor
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/convolutiontranspose2dweightsgradient(_:weights:outputshapetensor:forwardconvolutiondescriptor:name:))*