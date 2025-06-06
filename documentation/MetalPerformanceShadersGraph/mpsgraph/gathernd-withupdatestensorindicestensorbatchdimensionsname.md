# gatherND(withUpdatesTensor:indicesTensor:batchDimensions:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a GatherND operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func gatherND(withUpdatesTensor updatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, batchDimensions: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Gathers the slices in updatesTensor to the result tensor along the indices in indicesTensor. The gather is defined as

```md
B = batchDims 
U = updates.rank - B 
P = res.rank - B 
Q = inds.rank - B 
K = inds.shape[-1] 
index_slice = indices[i_{b0},...,i_{bB},i_{0},..,i_{Q-1}] 
res[i_{b0},...,i_{bB},i_{0},...,i_{Q-1}] = updates[i_{b0},...,i_{bB},index_slice[0],...,index_slice[K-1]] 
```

The tensors have the following shape requirements

```md
U > 0; P > 0; Q > 0 
K <= U 
P = (U-K) + Q-1 
indices.shape[0:Q-1] = res.shape[0:Q-1] 
res.shape[Q:P] = updates.shape[K:U] 
```

## Parameters

- `updatesTensor`: Tensor containing slices to be inserted into the result tensor.
- `indicesTensor`: Tensor containg the updates indices to read slices from
- `batchDimensions`: The number of batch dimensions
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/gathernd(withupdatestensor:indicestensor:batchdimensions:name:))*