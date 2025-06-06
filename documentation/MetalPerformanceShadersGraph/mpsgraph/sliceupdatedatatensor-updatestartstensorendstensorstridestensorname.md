# sliceUpdateDataTensor(_:update:startsTensor:endsTensor:stridesTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a strided-slice update operation with zero masks and returns the result tensor.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func sliceUpdateDataTensor(_ dataTensor: MPSGraphTensor, update updateTensor: MPSGraphTensor, startsTensor: MPSGraphTensor, endsTensor: MPSGraphTensor, stridesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `dataTensor`: The large tensor that will receive the update.
- `updateTensor`: The tensor with the new values that will replace values in the dataTensor.
- `startsTensor`: A Tensor that contains an array of numbers that specify the starting points for each dimension.
- `endsTensor`: A Tensor that contains an array of numbers that specify the ending points for each dimension.
- `stridesTensor`: A Tensor that contains an array of numbers that specify the strides for each dimension.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/sliceupdatedatatensor(_:update:startstensor:endstensor:stridestensor:name:))*