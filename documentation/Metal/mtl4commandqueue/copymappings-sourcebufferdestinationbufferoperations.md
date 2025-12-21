# copyMappings(sourceBuffer:destinationBuffer:operations:)

**Framework**: Metal  
**Kind**: method

Copies multiple offsets within a source placement sparse buffer to a destination placement sparse buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copyMappings(sourceBuffer: any MTLBuffer, destinationBuffer: any MTLBuffer, operations: [MTL4CopySparseBufferMappingOperation])
```

#### Discussion

You are responsible for ensuring the source destination sparse buffers have the same `placementSparsePageSize` when you create them via [`makeBuffer(length:options:placementSparsePageSize:)`](mtldevice/makebuffer(length:options:placementsparsepagesize:).md).

Additionally, you are responsible for ensuring both the source and destination sparse buffers don’t use the same aliased tiles at the same time.

> **Note**: If a sparse texture and a sparse buffer share the same backing tiles, these don’t provide you with meaningful views of the other resource’s data.

## Parameters

- `sourceBuffer`: The source placement sparse  .
- `destinationBuffer`: The destination placement sparse  .
- `operations`: An array of   instances to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4commandqueue/copymappings(sourcebuffer:destinationbuffer:operations:))*