# scatter(_:indices:shape:axis:mode:name:)

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
func scatter(_ updatesTensor: MPSGraphTensor, indices indicesTensor: MPSGraphTensor, shape: [NSNumber], axis: Int, mode: MPSGraphScatterMode, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

Scatters the slices in updatesTensor to the result tensor along the indices in indicesTensor. The scatter is defined as

```md
U = updates.rank 
P = res.rank 
res[i_{0},...,i_{axis-1},indices[i_{axis}],i_{axis+1},...,i_{U-1}] = updates[i_{0},...,i_{axis-1},i_{axis},i_{axis+1},...,i_{U-1}] 
```

Collisions will be updated according to mode. The tensors have the following shape requirements

```md
U = P 
indices.rank = 1 
updates.shape[0:axis-1] = res.shape[0:axis-1] 
updates.shape[axis] = indices.shape[0] 
updates.shape[axis+1:U] = res.shape[0:P] 
```

## Parameters

- `updatesTensor`: Tensor containing values to be inserted into the result tensor.
- `indicesTensor`: Tensor containg the result indices to insert values at.
- `shape`: The shape of the result tensor.
- `axis`: The axis of the result tensor to scatter values along.
- `mode`: The type of update to use on the destination.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/scatter(_:indices:shape:axis:mode:name:))*