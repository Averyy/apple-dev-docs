# sliceGradientTensor(_:fwdInShapeTensor:starts:ends:strides:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a strided-slice gradient operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func sliceGradientTensor(_ inputGradientTensor: MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, starts: [NSNumber], ends: [NSNumber], strides: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `inputGradientTensor`: The input gradient.
- `fwdInShapeTensor`: The shape of the forward pass input, that is the shape of the gradient output.
- `starts`: An array of numbers that specify the starting points for each dimension.
- `ends`: An array of numbers that specify the ending points for each dimension.
- `strides`: An array of numbers that specify the strides for each dimension.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/slicegradienttensor(_:fwdinshapetensor:starts:ends:strides:name:))*