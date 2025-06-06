# softMax(with:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the softmax function on the input tensor along the specified axis.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func softMax(with tensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid [`MPSGraphTensor`](mpsgraphtensor.md) object

## Parameters

- `tensor`: The input tensor.
- `axis`: The axis along which softmax is computed.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/softmax(with:axis:name:))*