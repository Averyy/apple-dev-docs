# copy(sourceAccelerationStructure:destinationAccelerationStructure:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes an acceleration structure copy operation into the command buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)
```

#### Discussion

You are responsible for ensuring the source and destination acceleration structures don’t overlap in memory. If this is an instance acceleration structure, Metal preserves references to the primitive acceleration structures it references.

Typically, the destination acceleration structure is at least as large as the source acceleration structure, except in cases where you compact the source acceleration structure. In this case, you need to allocate the destination acceleration to be at least as large as the compacted size of the source acceleration structure.

## Parameters

- `sourceAccelerationStructure`: Acceleration structure to copy from.
- `destinationAccelerationStructure`: Acceleration structure to copy to.

## See Also

- [func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes a command to copy and compact an acceleration structure.
- [func writeCompactedSize(sourceAccelerationStructure: any MTLAccelerationStructure, destinationBuffer: MTL4BufferRange)](mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure:destinationbuffer:).md)
  Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:))*