# refit(sourceAccelerationStructure:descriptor:destinationAccelerationStructure:scratchBuffer:scratchBufferOffset:options:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Updates an acceleration structure with new geometry or instance data, with options that control the refitting process.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: (any MTLBuffer)?, scratchBufferOffset: Int, options: MTLAccelerationStructureRefitOptions = [])
```

```objc
- (void) refitAccelerationStructure:(id<MTLAccelerationStructure>) sourceAccelerationStructure descriptor:(MTLAccelerationStructureDescriptor *) descriptor destination:(id<MTLAccelerationStructure>) destinationAccelerationStructure scratchBuffer:(id<MTLBuffer>) scratchBuffer scratchBufferOffset:(NSUInteger) scratchBufferOffset options:(MTLAccelerationStructureRefitOptions) options;
```

## Discussion

Use refitting to update an acceleration structure when you make small changes to the underlying geometry. Refitting performs much faster than rebuilding an acceleration structure from scratch. However, ray-tracing performance may degrade, based on how many changes you make to the geometry data.

You can’t use refitting to add or remove geometry in the acceleration structure.

If the source and destination acceleration structures are not the same, they need to avoid overlapping in memory. The destination acceleration structure and the scratch buffer need to have enough space in memory to hold the acceleration structure data. Call the [`accelerationStructureSizes(descriptor:)`](../mtldevice/accelerationstructuresizes%28descriptor%29.md) method on the Metal device object to get the required space. If you compact the source structure, the destination needs to be at least as large as the compacted size of the source acceleration structure.

## Parameters

- `sourceAccelerationStructure`: The source acceleration structure.
- `descriptor`: A description of the updated acceleration structure.
- `destinationAccelerationStructure`: The destination to write the new acceleration structure to. Pass the same acceleration structure or `nil` to refit the structure in place.
- `scratchBuffer`: A buffer used to hold data while building the acceleration structure. Pass `nil` if [`refitScratchBufferSize`](../mtlaccelerationstructuresizes/refitscratchbuffersize.md) returns zero.
- `scratchBufferOffset`: An offset, in bytes, in the scratch buffer where the scratch memory starts.
- `options`: Options that control the refitting process.

## See Also

### Refitting an acceleration structure
- [func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTLAccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: (any MTLBuffer)?, scratchBufferOffset: Int)](./refit%28sourceaccelerationstructure,descriptor,destinationaccelerationstructure,scratchbuffer,scratchbufferoffset%29.md)
  Updates an acceleration structure with new geometry or instance data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:scratchbufferoffset:options:))*