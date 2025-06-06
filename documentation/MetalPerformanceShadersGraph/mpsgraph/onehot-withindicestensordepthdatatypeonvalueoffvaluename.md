# oneHot(withIndicesTensor:depth:dataType:onValue:offValue:name:)

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
func oneHot(withIndicesTensor indicesTensor: MPSGraphTensor, depth: Int, dataType: MPSDataType, onValue: Double, offValue: Double, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Creates a tensor of rank equal to the rank of `indicesTensor` + 1. Inserts a new axis at the minor dimension. The values at the indices in the indicesTensor will have the onValue, and all other values will be set to the offValue.

## Parameters

- `indicesTensor`: Tensor of indices for on values
- `depth`: Depth of the oneHot vector along the axis
- `dataType`: MPSDataType of the result tensor.
- `onValue`: The value for indices designated by the indicesTensor. This value must match the specified data type.
- `offValue`: The value for indices not designated by the indicesTensor. This value must match the specified data type.
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/onehot(withindicestensor:depth:datatype:onvalue:offvalue:name:))*