# load(_:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a command that loads data from a file handle into a GPU texture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func load(_ texture: any MTLTexture, slice: Int, level: Int, size: MTLSize, sourceBytesPerRow: Int, sourceBytesPerImage: Int, destinationOrigin: MTLOrigin, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)
```

## Parameters

- `texture`: A texture instance the method loads data into.
- `slice`: A slice within the texture.
- `level`: A level within the texture.
- `size`: The region of the texture the method copies to.
- `sourceBytesPerRow`: The number of bytes in a row of data from the source file.
- `sourceBytesPerImage`: The number of bytes in an image from the source file.
- `destinationOrigin`: A starting location within the texture the method copies data to.
- `sourceHandle`: A handle to a source file.
- `sourceHandleOffset`: A starting location relative to the beginning of the file, in bytes, the method copies data from.

## See Also

- [func load(any MTLBuffer, offset: Int, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)](mtliocommandbuffer/load(_:offset:size:sourcehandle:sourcehandleoffset:).md)
  Encodes a command that loads data from a file handle into a GPU buffer.
- [func loadBytes(UnsafeMutableRawPointer, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)](mtliocommandbuffer/loadbytes(_:size:sourcehandle:sourcehandleoffset:).md)
  Encodes a command that loads data from a file handle into CPU-accessible memory buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/load(_:slice:level:size:sourcebytesperrow:sourcebytesperimage:destinationorigin:sourcehandle:sourcehandleoffset:))*