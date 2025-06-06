# scatterWithData(_:updates:indices:axis:mode:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a Scatter operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func scatterWithData(_ dataTensor: MPSGraphTensor, updates updatesTensor: MPSGraphTensor, indices indicesTensor: MPSGraphTensor, axis: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Scatters the slices in updatesTensor to the result tensor along the indices in indicesTensor, on top of dataTensor. The scatter is defined as

```md
U = updates.rank 
P = res.rank 
res[...] = data[...] 
res[i_{0},...,i_{axis-1},indices[i_{axis}],i_{axis+1},...,i_{U-1}] += updates[i_{0},...,i_{axis-1},i_{axis},i_{axis+1},...,i_{U-1}] // Note += is used but this depends on mode 
```

Collisions will be updated according to mode. The tensors have the following shape requirements

```md
U = P 
indices.rank = 1 
data.shape = res.shape 
updates.shape[0:axis-1] = res.shape[0:axis-1] 
updates.shape[axis] = indices.shape[0] 
updates.shape[axis+1:U] = res.shape[0:P] 
```

## Parameters

- `dataTensor`: Tensor containing inital values of same shape as result tensor
- `updatesTensor`: Tensor containing values to be inserted into the result tensor.
- `indicesTensor`: Tensor containg the result indices to insert values at
- `axis`: The axis of the result tensor to scatter values along
- `mode`: The type of update to use on the destination
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/scatterwithdata(_:updates:indices:axis:mode:name:))*