# sliceTensor(_:start:sizeTensor:squeezeMask:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a slice operation and returns the result tensor.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+

## Declaration

```swift
func sliceTensor(_ tensor: MPSGraphTensor, start startTensor: MPSGraphTensor, sizeTensor: MPSGraphTensor, squeezeMask: UInt32, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Slices a tensor starting from `startTensor`, stopping short before `startTensor + endTensor` stepping a single pace between each value. Semantics based on [`TensorFlow Strided Slice Op`](https://developer.apple.comhttps://www.tensorflow.org/api_docs/python/tf/strided_slice).

## Parameters

- `tensor`: The Tensor to be sliced.
- `startTensor`: The tensor that specifies the starting points for each dimension.
- `sizeTensor`: The tensor that specifies the size of the result for each dimension.
- `squeezeMask`: A bitmask that indicates dimensions the operation will squeeze out from the result.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/slicetensor(_:start:sizetensor:squeezemask:name:))*