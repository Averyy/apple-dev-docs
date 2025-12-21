# build(destinationAccelerationStructure:descriptor:scratchBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes an acceleration structure build into the command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func build(destinationAccelerationStructure accelerationStructure: any MTLAccelerationStructure, descriptor: MTL4AccelerationStructureDescriptor, scratchBuffer: MTL4BufferRange)
```

#### Discussion

Before you build an instance acceleration structure, you are responsible for ensuring the build operations for all primitive acceleration structures is complete. The built acceleration structure doesn’t retain any references to the input buffers of the descriptor, such as the vertex buffer or instance buffer, among others.

The acceleration structure build process may continue as long as the command buffer is not completed. However, you can safely encode ray tracing work against the acceleration structure if you schedule and synchronize the command buffers that contain this ray tracing work such that the command buffer with the build command is complete by the time ray tracing starts.

You are responsible for ensuring that the acceleration structure and scratch buffer are at least the size that the query [`accelerationStructureSizes(descriptor:)`](mtldevice/accelerationstructuresizes(descriptor:).md) returns.

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the scratch buffer the `scratchBuffer` parameter references, as well as for all the primitive acceleration structures you directly and indirectly reference.

## Parameters

- `accelerationStructure`: Acceleration structure storage to build into.
- `descriptor`: A descriptor for the acceleration structure Metal builds.
- `scratchBuffer`: Scratch buffer Metal can use while building the acceleration structure.   Metal may overwrite the contents of this buffer, and you should consider   them “undefined” after the refit operation starts and completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/build(destinationaccelerationstructure:descriptor:scratchbuffer:))*