# depthwiseConvolution2D(_:weights:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a 2D-depthwise convolution operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func depthwiseConvolution2D(_ source: MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphDepthwiseConvolution2DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `source`: A 2D Image source as tensor - must be of rank=4. The layout is defined by  .
- `weights`: The weights tensor, must be rank=4. The layout is defined by  .
- `descriptor`: The descriptor object that specifies strides, dilation rates, paddings and layouts.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/depthwiseconvolution2d(_:weights:descriptor:name:))*