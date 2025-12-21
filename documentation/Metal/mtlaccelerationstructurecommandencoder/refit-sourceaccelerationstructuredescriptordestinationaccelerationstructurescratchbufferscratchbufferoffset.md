# refit(sourceAccelerationStructure:descriptor:destinationAccelerationStructure:scratchBuffer:scratchBufferOffset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Updates an acceleration structure with new geometry or instance data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: (any MTLBuffer)?, scratchBufferOffset: Int)
```

#### Discussion

Use refitting to update an acceleration structure when you make small changes to the underlying geometry. Refitting performs much faster than rebuilding an acceleration structure from scratch. However, ray-tracing performance may degrade, based on how many changes you make to the geometry data.

You can’t use refitting to add or remove geometry in the acceleration structure.

If the source and destination acceleration structures aren’t the same, they can’t overlap in memory. The destination acceleration structure and the scratch buffer need to have enough space in memory to hold the acceleration structure data. Get the minimum amount of space it needs by calling the [`accelerationStructureSizes(descriptor:)`](mtldevice/accelerationstructuresizes(descriptor:).md) method of the Metal device instance. If you’re compacting the source structure, the destination needs to be at least as large as the compact size of the source acceleration structure.

## Parameters

- `sourceAccelerationStructure`: The source acceleration structure.
- `descriptor`: A description of the updated acceleration structure.
- `destinationAccelerationStructure`: The destination to write the new acceleration structure to. Pass the same acceleration structure or   to refit the structure in place.
- `scratchBuffer`: A buffer used to hold data while building the acceleration structure. Pass   if   returns zero.
- `scratchBufferOffset`: An offset, in bytes, in the scratch buffer where the scratch memory starts.

## See Also

- [func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: (any MTLBuffer)?, scratchBufferOffset: Int, options: MTLAccelerationStructureRefitOptions)](mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:scratchbufferoffset:options:).md)
  Updates an acceleration structure with new geometry or instance data, with options that control the refitting process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:scratchbufferoffset:))*