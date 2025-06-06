# sliceGradientTensor(_:fwdInShapeTensor:start:end:strideTensor:startMask:endMask:squeezeMask:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a strided-slice gradient operation and returns the result tensor.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
func sliceGradientTensor(_ inputGradientTensor: MPSGraphTensor, fwdInShapeTensor: MPSGraphTensor, start startTensor: MPSGraphTensor, end endTensor: MPSGraphTensor, strideTensor: MPSGraphTensor, startMask: UInt32, endMask: UInt32, squeezeMask: UInt32, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `inputGradientTensor`: The input gradient.
- `fwdInShapeTensor`: The shape of the forward pass input, that is the shape of the gradient output.
- `startTensor`: The tensor that specifies the starting points for each dimension.
- `endTensor`: The tensor that specifies the ending points for each dimension.
- `strideTensor`: The tensor that specifies the strides for each dimension.
- `startMask`: A bitmask that indicates dimensions whose   values the operation should ignore.
- `endMask`: A bitmask that indicates dimensions whose   values the operation should ignore.
- `squeezeMask`: A bitmask that indicates dimensions the operation will squeeze out from the result.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/slicegradienttensor(_:fwdinshapetensor:start:end:stridetensor:startmask:endmask:squeezemask:name:))*