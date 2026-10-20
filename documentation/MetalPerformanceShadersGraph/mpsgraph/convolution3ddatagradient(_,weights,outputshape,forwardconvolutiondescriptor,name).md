# convolution3DDataGradient(_:weights:outputShape:forwardConvolutionDescriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method  
**Role**: Instance Method

Creates a 3D convolution gradient operation with respect to the source tensor of the forward convolution.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
func convolution3DDataGradient(_ incomingGradient: MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], forwardConvolutionDescriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor
```

```objc
- (MPSGraphTensor *) convolution3DDataGradientWithIncomingGradientTensor:(MPSGraphTensor *) incomingGradient weightsTensor:(MPSGraphTensor *) weights outputShape:(MPSShape *) outputShape forwardConvolutionDescriptor:(MPSGraphConvolution3DOpDescriptor *) forwardConvolutionDescriptor name:(NSString *) name;
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

If `S` is source tensor to forward convolution, `R` is the result/returned tensor of forward convolution, and `L` is the loss function, convolution3DDataGradientWithIncomingGradientTensor returns tensor `dL/dS = dL/dR * dR/dS`, where `dL/dR` is the incomingGradient parameter.

## Parameters

- `incomingGradient`: Incoming loss gradient tensor
- `weights`: Forward pass weights tensor
- `outputShape`: Shape of the forward pass source tensor
- `forwardConvolutionDescriptor`: Forward convolution 2D op `descriptor`
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/convolution3ddatagradient(_:weights:outputshape:forwardconvolutiondescriptor:name:))*