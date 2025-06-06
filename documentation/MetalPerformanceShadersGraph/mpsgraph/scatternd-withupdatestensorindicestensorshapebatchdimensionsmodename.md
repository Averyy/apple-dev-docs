# scatterND(withUpdatesTensor:indicesTensor:shape:batchDimensions:mode:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a ScatterND operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func scatterND(withUpdatesTensor updatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, shape: [NSNumber], batchDimensions: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Scatters the slices in updatesTensor to the result tensor along the indices in indicesTensor. The scatter is defined as

```md
B = batchDims 
U = updates.rank - B 
P = res.rank - B 
Q = inds.rank - B 
K = inds.shape[-1] 
index_slice = indices[i_{b0},...,i_{bB},i_{0},..,i_{Q-1}] 
res[i_{b0},...,i_{bB},index_slice[0],...,index_slice[K-1]] = updates[i_{b0},...,i_{bB},i_{0},...,i_{Q-1}] 
```

Collisions will be summed, and slices not set by indices are set to 0. The tensors have the following shape requirements

```md
K <= P 
U = (P-K) + Q-1 
indices.shape[0:Q-1] = updates.shape[0:Q-1] 
updates.shape[Q:U] = res.shape[K:P] 
```

## Parameters

- `updatesTensor`: Tensor containing slices to be inserted into the result tensor.
- `indicesTensor`: Tensor containg the result indices to insert slices at
- `shape`: The shape of the result tensor.
- `batchDimensions`: The number of batch dimensions
- `mode`: The type of update to use on the destination
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/scatternd(withupdatestensor:indicestensor:shape:batchdimensions:mode:name:))*