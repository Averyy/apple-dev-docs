# expandDims(_:axes:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates an expand-dimensions operation and returns the result tensor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func expandDims(_ tensor: MPSGraphTensor, axes: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Expands the tensor, inserting dimensions with size 1 at specified axes.

## Parameters

- `tensor`: The input tensor.
- `axes`: The axes to expand.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/expanddims(_:axes:name:))*