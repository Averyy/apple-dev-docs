# batchToSpace(_:spatialAxes:batchAxis:blockDimensions:usePixelShuffleOrder:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a batch-to-space operation and returns the result tensor.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 13.0+
- tvOS 16.1+
- visionOS 1.0+

## Declaration

```swift
func batchToSpace(_ tensor: MPSGraphTensor, spatialAxes: [NSNumber], batchAxis: Int, blockDimensions: [NSNumber], usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

This operation outputs a copy of the input tensor, where values from the `batchAxis` dimension are moved in spatial blocks of size `blockDimensions` to the `spatialAxes` dimensions (for `usePixelShuffleOrder=YES` 1,2 or 3 axes supported, otherwise limited only by `MPSNDArray` rank limitations).  Use the `usePixelShuffleOrder` parameter to control how the data within spatial blocks is ordered in the `batchAxis` dimension: with `usePixelShuffleOrder = YES` MPSGraph stores the values of the spatial block contiguosly within the `batchAxis` dimension whereas without it they are stored interleaved with existing values in the `batchAxis` dimension. Note: This operation is the inverse of [`spaceToBatch(_:spatialAxes:batchAxis:blockDimensions:usePixelShuffleOrder:name:)`](mpsgraph/spacetobatch(_:spatialaxes:batchaxis:blockdimensions:usepixelshuffleorder:name:).md). Note: This operation is a generalization of [`depth(toSpace2DTensor:widthAxis:heightAxis:depthAxis:blockSize:usePixelShuffleOrder:name:)`](mpsgraph/depth(tospace2dtensor:widthaxis:heightaxis:depthaxis:blocksize:usepixelshuffleorder:name:).md).

## Parameters

- `tensor`: The input tensor.
- `spatialAxes`: The axes that define the dimensions containing the spatial blocks.
- `batchAxis`: The axis that defines the destination dimension, where to copy the blocks.
- `blockDimensions`: An array of numbers that defines the size of the rectangular spatial sub-block.
- `usePixelShuffleOrder`: A parameter that controls layout of the sub-blocks within the batch dimension.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/batchtospace(_:spatialaxes:batchaxis:blockdimensions:usepixelshuffleorder:name:))*