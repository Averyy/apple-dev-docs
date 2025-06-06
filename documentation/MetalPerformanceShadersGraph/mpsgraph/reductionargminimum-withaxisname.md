# reductionArgMinimum(with:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a reduction argMin operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func reductionArgMinimum(with tensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `tensor`: Input tensor
- `axis`: Axis of reduction
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/reductionargminimum(with:axis:name:))*