# space(toDepth2DTensor:widthAxis:heightAxis:depthAxis:blockSize:usePixelShuffleOrder:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a space-to-depth2D operation and returns the result tensor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func space(toDepth2DTensor tensor: MPSGraphTensor, widthAxis: Int, heightAxis: Int, depthAxis: Int, blockSize: Int, usePixelShuffleOrder: Bool, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

This operation outputs a copy of the `input` tensor, where values from the `widthAxis` and `heightAxis` dimensions are moved in spatial blocks of size `blockSize` to the `depthAxis` dimension. Use the `usePixelShuffleOrder` parameter to control how the data within spatial blocks is ordered in the `depthAxis` dimension: with `usePixelShuffleOrder=YES` MPSGraph stores the values of the spatial blocks  contiguosly within the `depthAxis` dimension, whereas otherwise they are stored interleaved with existing values in the `depthAxis` dimension. This operation is the inverse of `MPSGraph/depthToSpace2DTensor:widthAxis:heightAxis:depthAxis:blockSize:usePixelShuffleOrder:name:`.

## Parameters

- `tensor`: The input tensor.
- `widthAxis`: The axis that defines the fastest running dimension within the block.
- `heightAxis`: The axis that defines the 2nd fastest running dimension within the block.
- `depthAxis`: The axis that defines the destination dimension, where to copy the blocks.
- `blockSize`: The size of the square spatial sub-block.
- `usePixelShuffleOrder`: A parameter that controls the layout of the sub-blocks within the depth dimension.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/space(todepth2dtensor:widthaxis:heightaxis:depthaxis:blocksize:usepixelshuffleorder:name:))*