# reductionMaximumPropagateNaN(with:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a reduction max propagate NaN operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func reductionMaximumPropagateNaN(with tensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `tensor`: Input tensor
- `axis`: Axis of reduction
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/reductionmaximumpropagatenan(with:axis:name:))*