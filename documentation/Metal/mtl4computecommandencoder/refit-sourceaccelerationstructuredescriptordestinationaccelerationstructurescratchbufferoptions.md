# refit(sourceAccelerationStructure:descriptor:destinationAccelerationStructure:scratchBuffer:options:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes an acceleration structure refit operation into the command buffer, providing additional options.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func refit(sourceAccelerationStructure: any MTLAccelerationStructure, descriptor: MTL4AccelerationStructureDescriptor, destinationAccelerationStructure: (any MTLAccelerationStructure)?, scratchBuffer: MTL4BufferRange, options: MTLAccelerationStructureRefitOptions = [])
```

#### Discussion

You refit an acceleration structure to update it when the geometry it references changes. This operation is typically much faster than rebuilding the acceleration structure from scratch. The trade off is that after you refit the acceleration structure, its quality, as well as the performance of any subsequent ray tracing operation degrades, depending on how much the geometry changes.

After certain operations, refitting an acceleration structure may not be possible, for example, after adding or removing geometry.

When you refit an acceleration structure, you can do so in place, by specifying the same source and destination acceleration structures, or by providing a `nil` destination acceleration structure. If the source and destination acceleration structures aren’t the same, then you are responsible for ensuring they don’t overlap in memory.

Typically, the destination acceleration structure is at least as large as the source acceleration structure, except in cases where you compact the source acceleration structure. In this case, you need to allocate the destination acceleration to be at least as large as the compacted size of the source acceleration structure.

The scratch buffer you provide for the refit operation needs to be at least as large as the size that the query [`accelerationStructureSizes(descriptor:)`](mtldevice/accelerationstructuresizes(descriptor:).md) returns. If the size this query returns is zero, you can omit providing a scratch buffer by passing `0` as the address to the `scratchBuffer` parameter.

Use an instance of [`MTLResidencySet`](mtlresidencyset.md) to mark residency of the scratch buffer the `scratchBuffer` parameter references, as well as for all the instance and primitive acceleration structures you directly and indirectly reference.

## Parameters

- `sourceAccelerationStructure`: Acceleration structure to refit.
- `descriptor`: A descriptor for the acceleration structure to refit.
- `destinationAccelerationStructure`: Acceleration structure to store the refit result into.   If   is  , Metal performs an in-place   refit operation of the  .
- `scratchBuffer`: Scratch buffer Metal can use while refitting the acceleration structure.   Metal may overwrite the contents of this buffer, and you should consider   them “undefined” after the refit operation starts and completes.
- `options`: Options specifying the elements of the acceleration structure to refit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/refit(sourceaccelerationstructure:descriptor:destinationaccelerationstructure:scratchbuffer:options:))*