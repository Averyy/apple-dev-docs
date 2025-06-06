# leakyReLU(with:alphaTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the leaky rectified linear unit (ReLU) activation function on the input tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func leakyReLU(with tensor: MPSGraphTensor, alphaTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) object

#### Discussion

The operation is: f(x) = max(x, alpha). This operation supports broadcasting with the alpha tensor.

## Parameters

- `tensor`: The input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/leakyrelu(with:alphatensor:name:))*