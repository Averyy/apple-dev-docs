# build(accelerationStructure:descriptor:scratchBuffer:scratchBufferOffset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to build a new acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func build(accelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, scratchBuffer: any MTLBuffer, scratchBufferOffset: Int)
```

#### Discussion

The destination acceleration structure and the scratch buffer must have enough space in memory to hold the acceleration structure data. Call the [`accelerationStructureSizes(descriptor:)`](mtldevice/accelerationstructuresizes(descriptor:).md) method on the Metal device object to get the required space.

The resulting acceleration structure contains references to any other acceleration structures referenced by the descriptor, but not any other underlying buffer data. As part of creating the structure, the GPU overwrites data in the scratch buffer.

By default, Metal automatically synchronizes GPU access to the acceleration structure and any resources contained in the acceleration descriptor. For example, you can use a single encoder to build multiple geometry acceleration structures and then build the instanced structure that uses them. Similarly, you can use the acceleration structure in an encoder scheduled after this encoder.

If you are using untracked resources, you are responsible for synchronizing access to any untracked resources, including the acceleration structure. For example, you could use one encoder to build the geometry acceleration structures and update a fence, and a second encoder that waits on the fence and builds the instance acceleration structure.

## Parameters

- `accelerationStructure`: The acceleration structure to build into.
- `descriptor`: A description of the new acceleration structure.
- `scratchBuffer`: A buffer used to hold data while building the acceleration structure.
- `scratchBufferOffset`: An offset, in, bytes, in the scratch buffer where the scratch memory starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/build(accelerationstructure:descriptor:scratchbuffer:scratchbufferoffset:))*