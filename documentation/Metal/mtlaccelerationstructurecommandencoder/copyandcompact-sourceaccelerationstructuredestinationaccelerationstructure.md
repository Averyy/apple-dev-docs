# copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to compact an acceleration structure’s data and copy it into a different acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)
```

#### Discussion

The source and destination acceleration structures must not overlap in memory. The destination acceleration structure must be at least as large as the compacted size of the source acceleration structure, which you obtain by using the [`writeCompactedSize(accelerationStructure:buffer:offset:)`](mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure:buffer:offset:).md) method.

If the source acceleration structure contains references to other acceleration structures, the copied acceleration structure references the same child structures.

## Parameters

- `sourceAccelerationStructure`: The source acceleration structure.
- `destinationAccelerationStructure`: The destination acceleration structure.

## See Also

- [func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](mtlaccelerationstructurecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:).md)
  Encodes a command to copy the data from one acceleration structure to another.
- [func writeCompactedSize(accelerationStructure: any MTLAccelerationStructure, buffer: any MTLBuffer, offset: Int)](mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure:buffer:offset:).md)
  Encodes a command to calculate the compacted size of an acceleration structure.
- [func writeCompactedSize(accelerationStructure: any MTLAccelerationStructure, buffer: any MTLBuffer, offset: Int, sizeDataType: MTLDataType)](mtlaccelerationstructurecommandencoder/writecompactedsize(accelerationstructure:buffer:offset:sizedatatype:).md)
  Encodes a command to calculate the compacted size of an acceleration structure, taking into account the size of the output data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:))*