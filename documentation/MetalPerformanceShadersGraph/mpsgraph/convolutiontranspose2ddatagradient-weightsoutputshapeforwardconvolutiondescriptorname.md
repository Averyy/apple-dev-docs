# convolutionTranspose2DDataGradient(_:weights:outputShape:forwardConvolutionDescriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a convolution transpose gradient operation with respect to the source tensor of convolution transpose operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func convolutionTranspose2DDataGradient(_ incomingGradient: MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Inserts an operation in graph to compute gradient of convolution transpose with respect to source tensor of the corresponding convolution transpose operation.

## Parameters

- `incomingGradient`: Incoming gradient tensor
- `weights`: Forward pass weights tensor
- `outputShape`: Shape of the forward pass source tensor
- `forwardConvolutionDescriptor`: Forward pass op descriptor
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/convolutiontranspose2ddatagradient(_:weights:outputshape:forwardconvolutiondescriptor:name:))*