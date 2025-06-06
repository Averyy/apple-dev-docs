# squeeze(_:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a squeeze operation and returns the result tensor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func squeeze(_ tensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Squeezes the tensor, removing all dimensions with size 1.

## Parameters

- `tensor`: The input tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/squeeze(_:name:))*