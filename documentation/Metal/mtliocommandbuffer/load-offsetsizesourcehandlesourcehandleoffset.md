# load(_:offset:size:sourceHandle:sourceHandleOffset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that loads data from a file handle into a GPU buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func load(_ buffer: any MTLBuffer, offset: Int, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)
```

## Parameters

- `buffer`: A buffer instance the method loads data into.
- `offset`: A starting location relative to the beginning of the buffer, in bytes, the method copies data to.
- `size`: The number of bytes the method loads from the file into the buffer.
- `sourceHandle`: A handle to a source file.
- `sourceHandleOffset`: A starting location relative to the beginning of the file, in bytes, the method copies data from.

## See Also

- [func load(any MTLTexture, slice: Int, level: Int, size: MTLSize, sourceBytesPerRow: Int, sourceBytesPerImage: Int, destinationOrigin: MTLOrigin, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)](mtliocommandbuffer/load(_:slice:level:size:sourcebytesperrow:sourcebytesperimage:destinationorigin:sourcehandle:sourcehandleoffset:).md)
  Encodes a command that loads data from a file handle into a GPU texture.
- [func loadBytes(UnsafeMutableRawPointer, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)](mtliocommandbuffer/loadbytes(_:size:sourcehandle:sourcehandleoffset:).md)
  Encodes a command that loads data from a file handle into CPU-accessible memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/load(_:offset:size:sourcehandle:sourcehandleoffset:))*