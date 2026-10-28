# setMeshBuffers:offsets:withRange:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Assigns multiple buffers to a range of entries in the mesh shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
- (void) setMeshBuffers:(id<MTLBuffer> const[]) buffers offsets:(const NSUInteger[]) offsets withRange:(NSRange) range;
```

## Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Swift version of this method is [`setMeshBuffers(_:offsets:range:)`](./setmeshbuffers%28_,offsets,range%29.md).

## Parameters

- `buffers`: A pointer to a C array of [`MTLBuffer`](../mtlbuffer.md) instances the command assigns to entries in the mesh shader argument table for buffers.
- `offsets`: A pointer to a C array of unsigned integers. Each element represents the location, in bytes, from the start of the corresponding [`MTLBuffer`](../mtlbuffer.md) element in `buffers` where the mesh shader argument data begins.

  See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `range`: A span of integers that represent the entries in the mesh shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## See Also

### Assigning buffers for mesh shaders
- [func setMeshBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setmeshbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the mesh shader argument table.
- [func setMeshBytes(UnsafeRawPointer, length: Int, index: Int)](./setmeshbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.
- [func setMeshBufferOffset(Int, index: Int)](./setmeshbufferoffset%28_,index%29.md)
  Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshbuffers:offsets:withrange:)*