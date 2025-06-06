# convolution2DWeightsGradient(_:source:outputShapeTensor:forwardConvolutionDescriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a 2D convolution gradient operation with respect to weights tensor of forward convolution.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func convolution2DWeightsGradient(_ gradient: MPSGraphTensor, source: MPSGraphTensor, outputShapeTensor: MPSGraphTensor, forwardConvolutionDescriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

If `W` is weights tensor to forward convolution, `R` is the result/returned tensor of forward convolution, and `L` is the loss function, convolution2DWeightsGradientWithIncomingGradientTensor returns tensor `dL/dW = dL/dR * dR/dW`, where `dL/dR` is the incomingGradient parameter.

## Parameters

- `outputShapeTensor`: 4D int32 or Int64 Tensor. Shape of the forward pass source tensor
- `forwardConvolutionDescriptor`: Forward convolution 2D op 
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/convolution2dweightsgradient(_:source:outputshapetensor:forwardconvolutiondescriptor:name:))*