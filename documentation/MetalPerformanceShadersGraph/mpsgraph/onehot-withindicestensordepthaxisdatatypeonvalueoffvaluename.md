# oneHot(withIndicesTensor:depth:axis:dataType:onValue:offValue:name:)

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
func oneHot(withIndicesTensor indicesTensor: MPSGraphTensor, depth: Int, axis: Int, dataType: MPSDataType, onValue: Double, offValue: Double, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Creates a tensor of rank equal to the indicesTensor rank + 1. Inserts a new axis at the axis specified, or the minor axis if axis is -1. The values at the indices in the indicesTensor will have the onValue, and all other values will be set to the offValue.

## Parameters

- `indicesTensor`: Tensor of indices for on values
- `depth`: Depth of the oneHot vector along the axis
- `axis`: The axis to insert the new oneHot vector at. Defaults to -1, the minor axis
- `dataType`: MPSDataType of the result tensor Defaults to MPSDataTypeFloat
- `onValue`: The value for indices designated by the indicesTensor. This value must match the specified data type. Defaults to 1.0f
- `offValue`: The value for indices not designated by the indicesTensor. This value must match the specified data type. Defaults to 0.0f
- `name`: Name for the operation


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/onehot(withindicestensor:depth:axis:datatype:onvalue:offvalue:name:))*