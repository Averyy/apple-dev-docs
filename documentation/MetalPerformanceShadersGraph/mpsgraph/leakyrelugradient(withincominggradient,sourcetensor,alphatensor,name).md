# leakyReLUGradient(withIncomingGradient:sourceTensor:alphaTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the gradient of the leaky rectified linear unit (ReLU) activation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func leakyReLUGradient(withIncomingGradient gradient: MPSGraphTensor, sourceTensor source: MPSGraphTensor, alphaTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) object

#### Discussion

This operation supports broadcasting with the alpha tensor.

## Parameters

- `gradient`: The incoming gradient tensor.
- `source`: The input tensor in forward pass.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/leakyrelugradient(withincominggradient:sourcetensor:alphatensor:name:))*