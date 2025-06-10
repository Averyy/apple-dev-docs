# MTLAccelerationStructureCommandEncoder

**Framework**: Metal  
**Kind**: protocol

An object for encoding commands that build or refit acceleration structures.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLAccelerationStructureCommandEncoder : MTLCommandEncoder
```

## Mentions

- [Understanding the Metal 4 core API](understanding-the-metal-4-core-api.md)
- [Sampling GPU Data into Counter Sample Buffers](sampling-gpu-data-into-counter-sample-buffers.md)

#### Overview

Don’t implement this protocol yourself; instead you call methods on an [`MTLCommandBuffer`](mtlcommandbuffer.md) object to create command encoders. Command encoders are lightweight objects that you re-create every time you need to send commands to the GPU.

## Topics

### Building an Acceleration Structure
- [func build(accelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, scratchBuffer: any MTLBuffer, scratchBufferOffset: Int)](mtlaccelerationstructurecommandencoder/build(accelerationstructure:descriptor:scratchbuffer:scratchbufferoffset:).md)
  Encodes a command to build a new acceleration structure.
### Copying an Acceleration Structure
- [func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtlaccelerationstructurecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes a command to copy the data from one acceleration structure to another.
- [func writeCompactedSize(accelerationStructure: any MTLAccelerationStructure, buffer: any MTLBuffer, offset: Int)](mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure:buffer:offset:).md)
  Encodes a command to calculate the compacted size of an acceleration structure.
- [func writeCompactedSize(accelerationStructure: any MTLAccelerationStructure, buffer: any MTLBuffer, offset: Int, sizeDataType: MTLDataType)](mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure:buffer:offset:sizedatatype:).md)
  Encodes a command to calculate the compacted size of an acceleration structure, taking into account the size of the output data.
- [func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtlaccelerationstructurecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes a command to compact an acceleration structure’s data and copy it into a different acceleration structure.
### Refitting an Acceleration Structure
- [func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: (any MTLBuffer)?, scratchBufferOffset: Int)](mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:scratchbufferoffset:).md)
  Updates an acceleration structure with new geometry or instance data.
### Synchronizing Command Execution for Untracked Resources
- [func updateFence(any MTLFence)](mtlaccelerationstructurecommandencoder/updatefence(_:).md)
  Encodes a command that instructs the GPU to update a fence, which signals passes waiting on the fence.
- [func waitForFence(any MTLFence)](mtlaccelerationstructurecommandencoder/waitforfence(_:).md)
  Encodes a command that instructs the GPU to pause before starting the acceleration structure commands until another pass updates a fence.
### Specifying Resource Usage for Argument Buffers
- [func useHeap(any MTLHeap)](mtlaccelerationstructurecommandencoder/useheap(_:).md)
  Makes the resources contained in the specified heap available to the acceleration structure pass.
- [func useHeaps([any MTLHeap])](mtlaccelerationstructurecommandencoder/useheaps(_:).md)
  Makes the resources contained in the specified heaps available to the acceleration structure pass.
- [func useResource(any MTLResource, usage: MTLResourceUsage)](mtlaccelerationstructurecommandencoder/useresource(_:usage:).md)
  Makes a resource available to the acceleration structure pass.
- [func useResources([any MTLResource], usage: MTLResourceUsage)](mtlaccelerationstructurecommandencoder/useresources(_:usage:).md)
  Makes multiple resources available to the acceleration structure pass.
- [struct MTLResourceUsage](mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.
### Sampling Acceleration Structure Execution Data
- [func sampleCounters(sampleBuffer: any MTLCounterSampleBuffer, sampleIndex: Int, barrier: Bool)](mtlaccelerationstructurecommandencoder/samplecounters(samplebuffer:sampleindex:barrier:).md)
  Encodes a command to sample hardware counters at this point in the acceleration structure pass and store the samples into a counter sample buffer.
### Instance Methods
- [func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: (any MTLBuffer)?, scratchBufferOffset: Int, options: MTLAccelerationStructureRefitOptions)](mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:scratchbufferoffset:options:).md)

## Relationships

### Inherits From
- [MTLCommandEncoder](mtlcommandencoder.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Improving Ray-Tracing Data Access Using Per-Primitive Data](improving-ray-tracing-data-access-using-per-primitive-data.md)
  Simplify data access and improve GPU utilization by storing custom primitive data directly in the acceleration structure.
- [protocol MTLAccelerationStructure](mtlaccelerationstructure.md)
  A collection of model data for GPU-accelerated intersection of rays with the model.
- [class MTL4AccelerationStructureDescriptor](mtl4accelerationstructuredescriptor.md)
  Base class for Metal 4 acceleration structure descriptors.
- [class MTLAccelerationStructureDescriptor](mtlaccelerationstructuredescriptor.md)
  A base class for classes that define the configuration for a new acceleration structure.
- [class MTL4PrimitiveAccelerationStructureDescriptor](mtl4primitiveaccelerationstructuredescriptor.md)
  Descriptor for a primitive acceleration structure that directly references geometric shapes, such as triangles and bounding boxes.
- [class MTLPrimitiveAccelerationStructureDescriptor](mtlprimitiveaccelerationstructuredescriptor.md)
  A description of an acceleration structure that contains geometry primitives.
- [class MTL4InstanceAccelerationStructureDescriptor](mtl4instanceaccelerationstructuredescriptor.md)
  Descriptor for an instance acceleration structure.
- [class MTLInstanceAccelerationStructureDescriptor](mtlinstanceaccelerationstructuredescriptor.md)
  A description of an acceleration structure that derives from instances of primitive acceleration structures.
- [struct MTLAccelerationStructureUsage](mtlaccelerationstructureusage.md)
  Options that describe which tasks you can perform on an acceleration structure and how the system performs those tasks.
- [struct MTLAccelerationStructureRefitOptions](mtlaccelerationstructurerefitoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder)*