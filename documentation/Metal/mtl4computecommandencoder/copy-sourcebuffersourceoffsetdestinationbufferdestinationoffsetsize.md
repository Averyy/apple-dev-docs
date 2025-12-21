# copy(sourceBuffer:sourceOffset:destinationBuffer:destinationOffset:size:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies data from a buffer instance into another.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func copy(sourceBuffer: any MTLBuffer, sourceOffset: Int, destinationBuffer: any MTLBuffer, destinationOffset: Int, size: Int)
```

## Parameters

- `sourceBuffer`: An   instance the command copies data from.
- `sourceOffset`: A byte offset within   the command copies from.
- `destinationBuffer`: An   instance the command copies data to.
- `destinationOffset`: A byte offset within   the command copies to.
- `size`: The number of bytes the command copies from   to  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:destinationbuffer:destinationoffset:size:))*