# depthwiseConvolution2DWeightsGradient(_:source:outputShape:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a 2D-depthwise convolution gradient for weights operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func depthwiseConvolution2DWeightsGradient(_ incomingGradient: MPSGraphTensor, source: MPSGraphTensor, outputShape: [NSNumber], descriptor: MPSGraphDepthwiseConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `incomingGradient`: A 2D input gradient tensor - must be of rank=4. The layout is defined by  .
- `source`: A 2D Image source as tensor - must be of rank=4. The layout is defined by  .
- `outputShape`: The shape of the οutput tensor (and therefore weight tensor of forward pass).
- `descriptor`: The descriptor object that specifies strides, dilation rates, paddings and layouts.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/depthwiseconvolution2dweightsgradient(_:source:outputshape:descriptor:name:))*