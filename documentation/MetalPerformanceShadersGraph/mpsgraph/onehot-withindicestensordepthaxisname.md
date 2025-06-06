# oneHot(withIndicesTensor:depth:axis:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a oneHot operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func oneHot(withIndicesTensor indicesTensor: MPSGraphTensor, depth: Int, axis: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Creates a tensor of rank equal to the rank of `indicesTensor` + 1, of type MPSDataTypeFloat32. Inserts a new axis at the axis specified, or the minor axis if `axis` is -1. The values at the indices in the indicesTensor will be set to 1, and all other values will be set to 0.

## Parameters

- `indicesTensor`: Tensor of indices for on values
- `depth`: Depth of the oneHot vector along the axis
- `axis`: The axis to insert the new oneHot vector at
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/onehot(withindicestensor:depth:axis:name:))*