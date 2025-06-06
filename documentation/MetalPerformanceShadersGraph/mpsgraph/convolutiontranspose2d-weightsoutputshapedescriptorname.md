# convolutionTranspose2D(_:weights:outputShape:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a convolution transpose operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func convolutionTranspose2D(_ source: MPSGraphTensor, weights: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Convolution Tranpose operation is exactly the same as convolution gradint with respect to input image `convolution2DDataGradientWithIncomingGradient`. Weights tensor and source tensors are interpreted as they are in `convolution2DDataGradientWithIncomingGradient`. Convolution with stride `s` downsamples source tensor by factor `s` in spatial dimensions whereas convolution tranpose with stride `s` upsamples source tensor by factor `s`. Convolution transpose can map the same source size to multiple destination sizes. The relationship between the width of the source and the width of the destination is `(sourceWidth - 1)stride + 1 + (kernelWidth - 1)dilationRate <= destinationWidth + paddingLeft + paddingRight` so there are stride -1 values of the width of the destination that give same width of the source. In order to disambiguate, outputShape parameter is used.

## Parameters

- `source`: Input tensor
- `weights`: Weights tensor
- `outputShape`: Shape of the result tensor.
- `descriptor`: Descriptor for the corresponding forward 2D-convolution operation
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/convolutiontranspose2d(_:weights:outputshape:descriptor:name:))*