# topKGradient(_:input:kTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a TopKGradient operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func topKGradient(_ gradient: MPSGraphTensor, input source: MPSGraphTensor, kTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Finds the K largest values along the minor dimension of the input. The input must have at least K elements along its minor dimension.

## Parameters

- `gradient`: Tensor containing the incoming gradient.
- `source`: Tensor containing source data.
- `kTensor`: Tensor of the number of largest values to return.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/topkgradient(_:input:ktensor:name:))*