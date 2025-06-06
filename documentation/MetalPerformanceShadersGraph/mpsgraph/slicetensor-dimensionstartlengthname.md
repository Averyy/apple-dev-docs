# sliceTensor(_:dimension:start:length:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a slice operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func sliceTensor(_ tensor: MPSGraphTensor, dimension dimensionIndex: Int, start: Int, length: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `tensor`: The tensor to be sliced.
- `dimensionIndex`: The dimension to slice.
- `start`: The starting index of the slice, can be negative to count from the end of the tensor dimension.
- `length`: The length of the slice.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/slicetensor(_:dimension:start:length:name:))*