# reLU(with:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the ReLU (rectified linear activation unit) function with the input tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func reLU(with tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) object.

#### Discussion

The operation is:  f(x) = max(x, 0).

## Parameters

- `tensor`: The input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/relu(with:name:))*