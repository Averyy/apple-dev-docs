# writeCompactedSize(sourceAccelerationStructure:destinationBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func writeCompactedSize(sourceAccelerationStructure accelerationStructure: any MTLAccelerationStructure, destinationBuffer buffer: MTL4BufferRange)
```

#### Discussion

This size is potentially smaller than the acceleration structure. To perform compaction, you typically read this size from the buffer once the command buffer completes. You then use it to allocate a new, potentially smaller acceleration structure. Finally, you call the [`copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)`](mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md) method to perform the copy.

## Parameters

- `accelerationStructure`: Source acceleration structure.
- `buffer`: Destination size buffer. Metal writes the compacted size as a 64-bit unsigned integer   value, representing the compacted size in bytes.

## See Also

- [func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtl4computecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes an acceleration structure copy operation into the command buffer.
- [func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes a command to copy and compact an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure:destinationbuffer:))*