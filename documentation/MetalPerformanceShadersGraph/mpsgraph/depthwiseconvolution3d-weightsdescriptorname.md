# depthwiseConvolution3D(_:weights:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a 3D depthwise convolution operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func depthwiseConvolution3D(_ source: MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphDepthwiseConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Works exactly like depthwise convolution2D, but in three dimensions. Supports different layouts with the [`channelDimensionIndex`](mpsgraphdepthwiseconvolution3dopdescriptor/channeldimensionindex.md) property. If your weights need a different layout add a permute operation on them before this operation.

## Parameters

- `source`: A 3D Image source as tensor - must be at least rank=4 (CDHW when channelDimensionIndex = -4).
- `weights`: The weights tensor, must be rank=4 - axes are interpreted as CDHW when channelDimensionIndex = -4 .
- `descriptor`: The descriptor object that specifies strides, dilation rates and paddings.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/depthwiseconvolution3d(_:weights:descriptor:name:))*