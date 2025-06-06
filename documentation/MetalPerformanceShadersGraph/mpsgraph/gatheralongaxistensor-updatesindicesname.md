# gatherAlongAxisTensor(_:updates:indices:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a GatherAlongAxis operation and returns the result tensor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func gatherAlongAxisTensor(_ axisTensor: MPSGraphTensor, updates updatesTensor: MPSGraphTensor, indices indicesTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Gather values from `updatesTensor` along the specified `axis` at indices in `indicesTensor`. The shape of `updatesTensor` and `indicesTensor` must match except at `axis`. The shape of the result tensor is equal to the shape of `indicesTensor`. If an index is out of bounds of the `updatesTensor` along `axis` a 0 is inserted.

## Parameters

- `axisTensor`: Scalar Int32 tensor. The axis to gather from. Negative values wrap around
- `updatesTensor`: The input tensor to gather values from
- `indicesTensor`: Int32 or Int64 tensor used to index 
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/gatheralongaxistensor(_:updates:indices:name:))*