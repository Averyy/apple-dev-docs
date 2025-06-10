# copyAndCompact(sourceAccelerationStructure:destinationAccelerationStructure:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command to copy and compact an acceleration structure.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func copyAndCompact(sourceAccelerationStructure: any MTLAccelerationStructure, destinationAccelerationStructure: any MTLAccelerationStructure)
```

#### Discussion

You are responsible for ensuring that the source and destination acceleration structures don’t overlap in memory. If this is an instance acceleration structure, Metal preserves references to primitive acceleration structures it references.

This operation requires that the destination acceleration structure is at least as large as the compacted size of the source acceleration structure. You can compute this size by calling the [`writeCompactedSize(sourceAccelerationStructure:destinationBuffer:)`](mtl4computecommandencoder/writecompactedsize(sourceaccelerationstructure:destinationbuffer:).md) method.

## Parameters

- `sourceAccelerationStructure`: Acceleration structure to copy and compact.
- `destinationAccelerationStructure`: Acceleration structure to copy to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copyandcompact(sourceaccelerationstructure:destinationaccelerationstructure:))*