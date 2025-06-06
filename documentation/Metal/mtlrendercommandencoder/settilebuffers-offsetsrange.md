# setTileBuffers(_:offsets:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple buffers to a range of entries in the tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS ?+

## Declaration

```swift
func setTileBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

#### Discussion

By default, the buffer at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setTileBuffers:offsets:withRange:`](mtlrendercommandencoder/settilebuffers:offsets:withrange:.md).

## Parameters

- `buffers`: An array of   instances the command assigns to entries in the tile shader argument table for buffers.
- `offsets`: See the   to check for offset alignment requirements for buffers in   and   address space.
- `range`: A span of integers that represent the entries in the tile shader argument table for buffers. Each entry stores a record of the corresponding element in   and  .

## See Also

- [func setTileBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/settilebuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the tile shader argument table.
- [func setTileBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/settilebytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.
- [func setTileBufferOffset(Int, index: Int)](mtlrendercommandencoder/settilebufferoffset(_:index:).md)
  Updates an entry in the tile shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilebuffers(_:offsets:range:))*