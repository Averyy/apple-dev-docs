# convolutionTranspose2DWeightsGradient(_:weights:outputShape:forwardConvolutionDescriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a convolution transpose gradient operation with respect to the weights tensor of the convolution transpose operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func convolutionTranspose2DWeightsGradient(_ incomingGradientTensor: MPSGraphTensor, weights source: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Inserts an operation in graph to compute gradient of convolution transpose with respect to the weights tensor of the corresponding convolution transpose operation.

## Parameters

- `incomingGradientTensor`: Incoming gradient tensor
- `source`: Forward pass source tensor
- `outputShape`: Shape of the forward pass source weights tensor
- `forwardConvolutionDescriptor`: Forward pass op descriptor
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/convolutiontranspose2dweightsgradient(_:weights:outputshape:forwardconvolutiondescriptor:name:))*