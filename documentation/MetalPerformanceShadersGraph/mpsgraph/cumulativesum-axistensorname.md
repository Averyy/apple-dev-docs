# cumulativeSum(_:axisTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the cumulative sum of the input tensor along the specified axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func cumulativeSum(_ tensor: MPSGraphTensor, axisTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `tensor`: The input tensor
- `axisTensor`: The tensor dimension where you compute the cumulative operation
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/cumulativesum(_:axistensor:name:))*