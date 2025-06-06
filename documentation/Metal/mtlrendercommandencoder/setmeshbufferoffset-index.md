# setMeshBufferOffset(_:index:)

**Framework**: Metal  
**Kind**: method  
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

#### Discussion

The command this method encodes changes the offset for a mesh buffer that already has a previous assignment from one of your earlier commands.

For more information, see:

- [`setMeshBuffer(_:offset:index:)`](mtlrendercommandencoder/setmeshbuffer(_:offset:index:).md)
- [`setMeshBuffers(_:offsets:range:)`](mtlrendercommandencoder/setmeshbuffers(_:offsets:range:).md) (Swift)
- [`setMeshBuffers:offsets:withRange:`](mtlrendercommandencoder/setmeshbuffers:offsets:withrange:.md) (Objective-C)

The command can also adjust the offset for an entry that you previously set with the [`setMeshBytes(_:length:index:)`](mtlrendercommandencoder/setmeshbytes(_:length:index:).md) method.

> 💡 **Tip**:  If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

 If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

## Parameters

- `offset`: See the   to check for offset alignment requirements for buffers in   and   address space.
- `index`: An integer that represents the entry in the mesh shader argument table for buffers that already stores a record of an  .

## See Also

- [func setMeshBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setmeshbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the mesh shader argument table.
- [func setMeshBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setmeshbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the mesh shader argument table.
- [func setMeshBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setmeshbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshbufferoffset(_:index:))*