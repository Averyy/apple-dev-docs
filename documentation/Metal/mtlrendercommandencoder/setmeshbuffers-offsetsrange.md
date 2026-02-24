# setMeshBuffers(_:offsets:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple buffers to a range of entries in the mesh shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setMeshBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setMeshBuffers:offsets:withRange:`](mtlrendercommandencoder/setmeshbuffers:offsets:withrange:.md).

## Parameters

- `buffers`: An array of [`MTLBuffer`](mtlbuffer.md) instances the command assigns to entries in the mesh shader argument table for buffers.
- `offsets`: An array of integers. Each element represents the location, in bytes, from the start of the corresponding [`MTLBuffer`](mtlbuffer.md) element in `buffers` where the mesh shader argument data begins. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `range`: A span of integers that represent the entries in the mesh shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## See Also

- [func setMeshBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setmeshbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the mesh shader argument table.
- [func setMeshBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setmeshbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.
- [func setMeshBufferOffset(Int, index: Int)](mtlrendercommandencoder/setmeshbufferoffset(_:index:).md)
  Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshbuffers(_:offsets:range:))*