# sigmoid(with:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the sigmoid operation on an input tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func sigmoid(with tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) object.

## Parameters

- `tensor`: The input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/sigmoid(with:name:))*