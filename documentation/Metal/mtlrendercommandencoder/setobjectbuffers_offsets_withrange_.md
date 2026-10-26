# setObjectBuffers:offsets:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Encodes a command that assigns multiple buffers to a range of entries in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setObjectBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets withRange:(NSRange) range;
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Swift version of this method is [`setObjectBuffers(_:offsets:range:)`](./setobjectbuffers%28_,offsets,range%29.md).

## Parameters

- `buffers`: A pointer to a C array of [`MTLBuffer`](../mtlbuffer.md) instances the command assigns to entries in the object shader argument table for buffers.
- `offsets`: A pointer to a C array of unsigned integers. Each element represents the location, in bytes, from the start of the corresponding [`MTLBuffer`](../mtlbuffer.md) element in `buffers` where the object shader argument data begins.

  See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `range`: A span of integers that represent the entries in the object shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## See Also

### Assigning buffers for object shaders
- [func setObjectBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setobjectbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the object shader argument table.
- [func setObjectBytes(UnsafeRawPointer, length: Int, index: Int)](./setobjectbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the object shader argument table.
- [func setObjectBufferOffset(Int, index: Int)](./setobjectbufferoffset%28_,index%29.md)
  Updates an entry in the object shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectbuffers:offsets:withrange:)*