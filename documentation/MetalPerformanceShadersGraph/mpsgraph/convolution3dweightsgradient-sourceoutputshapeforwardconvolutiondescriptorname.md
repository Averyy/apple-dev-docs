# convolution3DWeightsGradient(_:source:outputShape:forwardConvolutionDescriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a 3D convolution gradient operation with respect to the weights tensor of the forward convolution.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
func convolution3DWeightsGradient(_ incomingGradient: MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

If `W` is weights tensor to forward convolution, `R` is the result/returned tensor of forward convolution, and `L` is the loss function, convolution3DWeightsGradientWithIncomingGradientTensor returns tensor `dL/dW = dL/dR * dR/dW`, where `dL/dR` is the incomingGradient parameter.

## Parameters

- `incomingGradient`: Incoming loss gradient tensor
- `outputShape`: Shape of the forward pass source tensor
- `forwardConvolutionDescriptor`: Forward convolution 2D op 
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/convolution3dweightsgradient(_:source:outputshape:forwardconvolutiondescriptor:name:))*