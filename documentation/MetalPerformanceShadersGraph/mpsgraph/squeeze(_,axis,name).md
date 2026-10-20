# squeeze(_:axis:name:)

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
func squeeze(_ tensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Squeezes the tensor, removing a dimension with size 1 at the specified axis. The size of the input tensor must be 1 at the specified axis.

## Parameters

- `tensor`: The input tensor.
- `axis`: The axis to squeeze.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/squeeze(_:axis:name:))*