# cumulativeMaximum(_:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the cumulative maximum of the input tensor along the specified axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func cumulativeMaximum(_ tensor: MPSGraphTensor, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `tensor`: The input tensor
- `axis`: The tensor dimension where you compute the cumulative operation
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/cumulativemaximum(_:axis:name:))*