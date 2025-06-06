# resizeNearest(withGradientTensor:input:scale:offsetTensor:nearestRoundingMode:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a Resize gradient operation and returns the result tensor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func resizeNearest(withGradientTensor gradient: MPSGraphTensor, input: MPSGraphTensor, scale: MPSGraphTensor, offsetTensor offset: MPSGraphTensor, nearestRoundingMode: MPSGraphResizeNearestRoundingMode, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Computes the gradient for the forward pass Resize op with nearest neighbor sampling and identical parameters. See discussion of resizeTensor for more in depth description of resize paramters.

## Parameters

- `gradient`: Incoming gradient tensor
- `input`: Forward pass input tensor
- `scale`: 1D float tensor of size equal to rank of input.
- `offset`: 1D float tensor of size equal to rank of input.
- `nearestRoundingMode`: The rounding mode to use when using nearest resampling. Default is roundPreferCeil.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/resizenearest(withgradienttensor:input:scale:offsettensor:nearestroundingmode:name:))*