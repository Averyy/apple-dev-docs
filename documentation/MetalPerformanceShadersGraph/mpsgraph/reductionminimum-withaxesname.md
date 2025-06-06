# reductionMinimum(with:axes:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a reduction min operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func reductionMinimum(with tensor: MPSGraphTensor, axes: [NSNumber]?, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `tensor`: Input tensor
- `axes`: Axes of reduction
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/reductionminimum(with:axes:name:))*