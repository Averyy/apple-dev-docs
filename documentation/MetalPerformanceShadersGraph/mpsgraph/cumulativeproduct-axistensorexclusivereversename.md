# cumulativeProduct(_:axisTensor:exclusive:reverse:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Computes the cumulative product of the input tensor along the specified axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func cumulativeProduct(_ tensor: MPSGraphTensor, axisTensor: MPSGraphTensor, exclusive: Bool, reverse: Bool, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `tensor`: The input tensor
- `axisTensor`: The tensor dimension where you compute the cumulative operation
- `exclusive`: If true, perform the exclusive cumulative operation, and the first element will be equal to one
- `reverse`: If true, reverse the direction of the cumulative operation along the specified axis
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/cumulativeproduct(_:axistensor:exclusive:reverse:name:))*