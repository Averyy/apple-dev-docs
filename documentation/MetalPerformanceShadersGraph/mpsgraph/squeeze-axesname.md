# squeeze(_:axes:name:)

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
func squeeze(_ tensor: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Squeezes the tensor, removing dimensions with size 1 at specified axes. The size of the input tensor must be 1 at all specified axes.

## Parameters

- `tensor`: The input tensor.
- `axes`: The axes to squeeze.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/squeeze(_:axes:name:))*