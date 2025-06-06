# leakyReLU(with:alpha:name:)

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
func leakyReLU(with tensor: MPSGraphTensor, alpha: Double, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) object

#### Discussion

The operation is: f(x) = max(x, alpha).

## Parameters

- `tensor`: An input tensor.
- `alpha`: The scalar value alpha used by all elements in the input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/leakyrelu(with:alpha:name:))*