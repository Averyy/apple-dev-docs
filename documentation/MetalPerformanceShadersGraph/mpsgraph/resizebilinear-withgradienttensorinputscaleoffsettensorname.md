# resizeBilinear(withGradientTensor:input:scale:offsetTensor:name:)

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
func resizeBilinear(withGradientTensor gradient: MPSGraphTensor, input: MPSGraphTensor, scale: MPSGraphTensor, offsetTensor offset: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Computes the gradient for the forward pass Resize op with bilinear sampling and identical parameters.

## Parameters

- `gradient`: Incoming gradient tensor
- `input`: Forward pass input tensor
- `scale`: 1D float tensor of size equal to rank of input.
- `offset`: 1D float tensor of size equal to rank of input.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/resizebilinear(withgradienttensor:input:scale:offsettensor:name:))*