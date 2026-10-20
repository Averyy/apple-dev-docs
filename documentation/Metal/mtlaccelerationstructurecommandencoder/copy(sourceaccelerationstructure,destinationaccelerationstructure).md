# copy(sourceAccelerationStructure:destinationAccelerationStructure:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a command to copy the data from one acceleration structure to another.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)
```

```objc
- (void) copyAccelerationStructure:(id<MTLAccelerationStructure>) sourceAccelerationStructure toAccelerationStructure:(id<MTLAccelerationStructure>) destinationAccelerationStructure;
```

#### Discussion

The destination acceleration structure needs to be at least as large as the source acceleration structure, unless you’re compacting the source acceleration structure. In that case, the destination acceleration structure needs be at least as large as the compact size of the source acceleration structure.

If the source acceleration structure contains references to other acceleration structures, the copy of the acceleration structure also refers to the same child structures.

## Parameters

- `sourceAccelerationStructure`: The source acceleration structure.
- `destinationAccelerationStructure`: The destination acceleration structure.

## See Also

### Copying an acceleration structure
- [func writeCompactedSize(accelerationStructure: any MTLAccelerationStructure, buffer: any MTLBuffer, offset: Int)](./writecompactedsize%28accelerationstructure,buffer,offset%29.md)
  Encodes a command to calculate the compacted size of an acceleration structure.
- [func writeCompactedSize(accelerationStructure: any MTLAccelerationStructure, buffer: any MTLBuffer, offset: Int, sizeDataType: MTLDataType)](./writecompactedsize%28accelerationstructure,buffer,offset,sizedatatype%29.md)
  Encodes a command to calculate the compacted size of an acceleration structure, taking into account the size of the output data.
- [func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](./copyandcompact%28sourceaccelerationstructure,destinationaccelerationstructure%29.md)
  Encodes a command to compact an acceleration structure’s data and copy it into a different acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecommandencoder/copy(sourceaccelerationstructure:destinationaccelerationstructure:))*