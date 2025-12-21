# setMeshBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a buffer to an entry in the mesh shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setMeshBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Mentions

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)

#### Discussion

By default, the texture at each index is `nil`.

## Parameters

- `buffer`: An   instance the command assigns to an entry in the mesh shader argument table for buffers.
- `offset`: See the   to check for offset alignment requirements for buffers in   and   address space.
- `index`: An integer that represents the entry in the mesh shader argument table for buffers that stores a record of   and  .

## See Also

- [func setMeshBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setmeshbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the mesh shader argument table.
- [func setMeshBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setmeshbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.
- [func setMeshBufferOffset(Int, index: Int)](mtlrendercommandencoder/setmeshbufferoffset(_:index:).md)
  Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setmeshbuffer(_:offset:index:))*