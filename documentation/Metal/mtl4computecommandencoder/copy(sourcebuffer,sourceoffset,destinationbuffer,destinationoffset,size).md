# copy(sourceBuffer:sourceOffset:destinationBuffer:destinationOffset:size:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) copyFromBuffer:(id<MTLBuffer>) sourceBuffer sourceOffset:(NSUInteger) sourceOffset toBuffer:(id<MTLBuffer>) destinationBuffer destinationOffset:(NSUInteger) destinationOffset size:(NSUInteger) size;
```

## Parameters

- `sourceBuffer`: An [`MTLBuffer`](../mtlbuffer.md) instance the command copies data from.
- `sourceOffset`: A byte offset within `sourceBuffer` the command copies from.
- `destinationBuffer`: An [`MTLBuffer`](../mtlbuffer.md) instance the command copies data to.
- `destinationOffset`: A byte offset within `destinationBuffer` the command copies to.
- `size`: The number of bytes the command copies from `sourceBuffer` to `destinationBuffer`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcebuffer:sourceoffset:destinationbuffer:destinationoffset:size:))*