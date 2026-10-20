# copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a command to copy and compact an acceleration structure.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)
```

```objc
- (void) copyAndCompactAccelerationStructure:(id<MTLAccelerationStructure>) sourceAccelerationStructure toAccelerationStructure:(id<MTLAccelerationStructure>) destinationAccelerationStructure;
```

#### Discussion

You are responsible for ensuring that the source and destination acceleration structures don’t overlap in memory. If this is an instance acceleration structure, Metal preserves references to primitive acceleration structures it references.

This operation requires that the destination acceleration structure is at least as large as the compacted size of the source acceleration structure. You can compute this size by calling the [`writeCompactedSize(sourceAccelerationStructure:destinationBuffer:)`](./writecompactedsize%28sourceaccelerationstructure,destinationbuffer%29.md) method.

## Parameters

- `sourceAccelerationStructure`: Acceleration structure to copy and compact.
- `destinationAccelerationStructure`: Acceleration structure to copy to.

## See Also

### Encoding acceleration structure copy commands
- [func copy(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)](./copy%28sourceaccelerationstructure,destinationaccelerationstructure%29.md)
  Encodes an acceleration structure copy operation into the command buffer.
- [func writeCompactedSize(sourceAccelerationStructure: any MTLAccelerationStructure, destinationBuffer: MTL4BufferRange)](./writecompactedsize%28sourceaccelerationstructure,destinationbuffer%29.md)
  Encodes a command to compute the size an acceleration structure can compact into, writing the result into a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:))*