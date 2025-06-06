# reductionOr(with:axes:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a reduction or operation and returns the result tensor.

**Availability**:
- iOS 15.3+
- iPadOS 15.3+
- Mac Catalyst 15.3+
- macOS 12.2+
- tvOS 15.3+
- visionOS 1.0+

## Declaration

```swift
func reductionOr(with tensor: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `tensor`: Input tensor
- `axes`: Axes of reduction
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/reductionor(with:axes:name:))*