# sliceGradientTensor(_:fwdInShapeTensor:start:sizeTensor:squeezeMask:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a slice gradient operation and returns the result tensor.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
func sliceGradientTensor(_ inputGradientTensor: MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, start startTensor: MPSGraphTensor, sizeTensor: MPSGraphTensor, squeezeMask: UInt32, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `inputGradientTensor`: The input gradient.
- `fwdInShapeTensor`: The shape of the forward pass input, that is the shape of the gradient output.
- `startTensor`: The tensor that specifies the starting points for each dimension.
- `sizeTensor`: The tensor that specifies the size of the forward result for each dimension.
- `squeezeMask`: A bitmask that indicates dimensions the operation will squeeze out from the result.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/slicegradienttensor(_:fwdinshapetensor:start:sizetensor:squeezemask:name:))*