# setMeshBufferOffset(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setMeshBufferOffset(_ offset: Int, index: Int)
```

```objc
- (void) setMeshBufferOffset:(NSUInteger) offset atIndex:(NSUInteger) index;
```

#### Discussion

The command this method encodes changes the offset for a mesh buffer that already has a previous assignment from one of your earlier commands.

For more information, see:

- [`setMeshBuffer(_:offset:index:)`](./setmeshbuffer%28_,offset,index%29.md)
- [`setMeshBuffers(_:offsets:range:)`](./setmeshbuffers%28_,offsets,range%29.md) (Swift)
- [`setMeshBuffers:offsets:withRange:`](./setmeshbuffers_offsets_withrange_.md) (Objective-C)

The command can also adjust the offset for an entry that you previously set with the [`setMeshBytes(_:length:index:)`](./setmeshbytes%28_,length,index%29.md) method.

> 💡 **Tip**:  If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

## Parameters

- `offset`: An integer that represents the location, in bytes, from the start of `buffer` where the mesh shader argument data begins.

  See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `index`: An integer that represents the entry in the mesh shader argument table for buffers that already stores a record of an [`MTLBuffer`](../mtlbuffer.md).

## See Also

### Assigning buffers for mesh shaders
- [func setMeshBuffer((any MTLBuffer)?, offset: Int, index: Int)](./setmeshbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the mesh shader argument table.
- [func setMeshBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setmeshbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the mesh shader argument table.
- [func setMeshBytes(UnsafeRawPointer, length: Int, index: Int)](./setmeshbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.
- [- setMeshBuffers:offsets:withRange:](./setmeshbuffers_offsets_withrange_.md)
  Assigns multiple buffers to a range of entries in the mesh shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshbufferoffset(_:index:))*