# concatTensor(_:with:dimension:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a concatenation operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func concatTensor(_ tensor: MPSGraphTensor, with tensor2: MPSGraphTensor, dimension dimensionIndex: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Concatenates two input tensors along the specified dimension. Tensors must be broadcast compatible along all other dimensions, and have the same datatype.

## Parameters

- `tensor`: The first tensor to concatenate.
- `tensor2`: The second tensor to concatenate.
- `dimensionIndex`: The dimension to concatenate across, must be in range:  .
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/concattensor(_:with:dimension:name:))*