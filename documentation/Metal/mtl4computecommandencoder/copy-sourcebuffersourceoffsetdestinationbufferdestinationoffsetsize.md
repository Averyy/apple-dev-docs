# copy(sourceBuffer:sourceOffset:destinationBuffer:destinationOffset:size:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that copies data from a buffer instance into another.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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