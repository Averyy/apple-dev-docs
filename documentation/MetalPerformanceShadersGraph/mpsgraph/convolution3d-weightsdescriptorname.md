# convolution3D(_:weights:descriptor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a 3D forward convolution operation and returns the result tensor.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
func convolution3D(_ source: MPSGraphTensor, weights: MPSGraphTensor, descriptor: MPSGraphConvolution3DOpDescriptor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `source`: Source tensor - must be of rank 5. The layout is defined by  .
- `weights`: Weights tensor, must be rank 5. The layout is defined by  .
- `descriptor`: Specifies strides, dilation rates, paddings and layouts.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/convolution3d(_:weights:descriptor:name:))*