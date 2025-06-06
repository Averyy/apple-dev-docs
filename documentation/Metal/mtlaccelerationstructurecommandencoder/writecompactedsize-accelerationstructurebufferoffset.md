# writeCompactedSize(accelerationStructure:buffer:offset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to calculate the compacted size of an acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func writeCompactedSize(accelerationStructure: any MTLAccelerationStructure, buffer: any MTLBuffer, offset: Int)
```

#### Discussion

The GPU writes the compacted size to the buffer as a 32-bit unsigned integer representing the compacted size in bytes. The compacted size may be smaller than the source acceleration structure.

To compact an acceleration structure, encode a command to get the minimum size. After the command completes, read the size from the buffer and allocate a new acceleration structure with at least that much storage. Then create another encoder and call the  [`copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)`](mtlaccelerationstructurecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md) method to copy it into the new structure.

## Parameters

- `accelerationStructure`: The acceleration structure to measure.
- `buffer`: The buffer to write the size into.
- `offset`: An offset, in bytes, where the GPU should write the result.

## See Also

- [func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtlaccelerationstructurecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes a command to copy the data from one acceleration structure to another.
- [func writeCompactedSize(accelerationStructure: any MTLAccelerationStructure, buffer: any MTLBuffer, offset: Int, sizeDataType: MTLDataType)](mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure:buffer:offset:sizedatatype:).md)
  Encodes a command to calculate the compacted size of an acceleration structure, taking into account the size of the output data.
- [func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtlaccelerationstructurecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes a command to compact an acceleration structure’s data and copy it into a different acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure:buffer:offset:))*