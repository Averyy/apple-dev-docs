# gather(withUpdatesTensor:indicesTensor:axis:batchDimensions:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a Gather operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func gather(withUpdatesTensor updatesTensor: MPSGraphTensor, indicesTensor: MPSGraphTensor, axis: Int, batchDimensions: Int, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Gathers the values in updatesTensor to the result tensor along the indices in indicesTensor. The gather is defined as

```md
B = batchDims 
U = updates.rank 
P = res.rank 
Q = inds.rank 
res[p_{0},...p_{axis-1}, i_{B},...,i_{Q}, ...,p_{axis+1},...,p{U-1}] = 
updates[p_{0},...p_{axis-1}, indices[p_{0},...,p_{B-1},i_{B},...,i_{Q}, ...,p_{axis+1},...,p{U-1}] 
```

The tensors have the following shape requirements

```md
P = Q-B + U-1 
indices.shape[0:B] = updates.shape[0:B] = res.shape[0:B] 
res.shape[0:axis] = updates.shape[0:axis] 
res.shape[axis:axis+Q-B] = indices.shape[B:] 
res.shape[axis+1+Q-B:] = updates.shape[axis+1:] 
```

## Parameters

- `updatesTensor`: Tensor containing slices to be inserted into the result tensor.
- `indicesTensor`: Tensor containg the updates indices to read slices from
- `axis`: The dimension on which to perform the gather
- `batchDimensions`: The number of batch dimensions
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/gather(withupdatestensor:indicestensor:axis:batchdimensions:name:))*