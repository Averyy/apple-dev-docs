# transposeTensor(_:dimension:withDimension:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a transpose operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func transposeTensor(_ tensor: MPSGraphTensor, dimension dimensionIndex: Int, withDimension dimensionIndex2: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Transposes the dimensions `dimensionIndex` and `dimensionIndex2` of the input tensor.

## Parameters

- `tensor`: The tensor to be transposed.
- `dimensionIndex`: The first dimension index to be transposed.
- `dimensionIndex2`: The second dimension index to be transposed.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/transposetensor(_:dimension:withdimension:name:))*