# loadBytes(_:size:sourceHandle:sourceHandleOffset:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes a command that loads data from a file handle into CPU-accessible memory buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func loadBytes(_ pointer: UnsafeMutableRawPointer, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)
```

```objc
- (void) loadBytes:(void *) pointer size:(NSUInteger) size sourceHandle:(id<MTLIOFileHandle>) sourceHandle sourceHandleOffset:(NSUInteger) sourceHandleOffset;
```

## Parameters

- `pointer`: A pointer to memory the method loads data into.
- `size`: The number of bytes the method loads from the file.
- `sourceHandle`: A handle to a source file.
- `sourceHandleOffset`: A starting location relative to the beginning of the file, in bytes, the method copies data from.

## See Also

### Loading assets
- [func load(any MTLBuffer, offset: Int, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)](./load%28_,offset,size,sourcehandle,sourcehandleoffset%29.md)
  Encodes a command that loads data from a file handle into a GPU buffer.
- [func load(any MTLTexture, slice: Int, level: Int, size: MTLSize, sourceBytesPerRow: Int, sourceBytesPerImage: Int, destinationOrigin: MTLOrigin, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)](./load%28_,slice,level,size,sourcebytesperrow,sourcebytesperimage,destinationorigin,sourcehandle,sourcehandleoffset%29.md)
  Encodes a command that loads data from a file handle into a GPU texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/loadbytes(_:size:sourcehandle:sourcehandleoffset:))*