# scatterNDWithData(_:updates:indices:batchDimensions:mode:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a ScatterND operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func scatterNDWithData(_ dataTensor: MPSGraphTensor, updates updatesTensor: MPSGraphTensor, indices indicesTensor: MPSGraphTensor, batchDimensions: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Scatters the slices in updatesTensor to the result tensor along the indices in indicesTensor, on top of dataTensor. The scatter is defined as

```md
B = batchDims 
U = updates.rank - B 
P = res.rank - B 
Q = inds.rank - B 
K = inds.shape[-1] 
index_slice = indices[i_{b0},...,i_{bB},i_{0},..,i_{Q-1}] 
res[...] = data[...] 
res[i_{b0},...,i_{bB},index_slice[0],...,index_slice[K-1]] += updates[i_{b0},...,i_{bB},i_{0},...,i_{Q-1}] // Note += is used but this depends on mode 
```

Collisions will be updated according to mode, and slices not set by indices are set to 0. The tensors have the following shape requirements

```md
K <= P 
U = (P-K) + Q-1 
data.shape = res.shape 
indices.shape[0:Q-1] = updates.shape[0:Q-1] 
updates.shape[Q:U] = res.shape[K:P] 
```

## Parameters

- `dataTensor`: Tensor containing inital values of same shape as result tensor
- `updatesTensor`: Tensor containing slices to be inserted into the result tensor.
- `indicesTensor`: Tensor containg the result indices to insert slices at
- `batchDimensions`: The number of batch dimensions
- `mode`: The type of update to use on the destination
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/scatterndwithdata(_:updates:indices:batchdimensions:mode:name:))*