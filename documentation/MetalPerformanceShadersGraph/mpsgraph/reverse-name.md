# reverse(_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a reverse operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func reverse(_ tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Reverses a tensor on all axes. Semantics based on [`TensorFlow reverse op`](https://developer.apple.comhttps://www.tensorflow.org/api_docs/python/tf/reverse).

## Parameters

- `tensor`: The tensor to be reversed.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/reverse(_:name:))*