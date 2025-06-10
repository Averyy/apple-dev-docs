# writeCompactedSize(sourceAccelerationStructure:destinationBuffer:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func writeCompactedSize(sourceAccelerationStructure accelerationStructure: any MTLAccelerationStructure, destinationBuffer buffer: MTL4BufferRange)
```

#### Discussion

This size is potentially smaller than the acceleration structure. To perform compaction, you typically read this size from the buffer once the command buffer completes. You then use it to allocate a new, potentially smaller acceleration structure. Finally, you call the [`copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)`](mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md) method to perform the copy.

## Parameters

- `accelerationStructure`: Source acceleration structure.
- `buffer`: Destination size buffer. Metal writes the compacted size as a 64-bit unsigned integer   value, representing the compacted size in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure:destinationbuffer:))*