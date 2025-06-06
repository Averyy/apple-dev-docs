# transpose(_:permutation:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a permutation operation and returns the result tensor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func transpose(_ tensor: MPSGraphTensor, permutation: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Permutes the dimensions of the input tensor according to values in `permutation`.

## Parameters

- `tensor`: The tensor to be permuted.
- `permutation`: An array of numbers defining the permutation, must be of length   and define a valid permutation.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/transpose(_:permutation:name:))*