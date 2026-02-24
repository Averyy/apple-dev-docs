# setTileBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a buffer to an entry in the tile shader argument table.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func setTileBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Mentions

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)

#### Discussion

By default, the buffer at each index is `nil`.

## Parameters

- `buffer`: An [`MTLBuffer`](mtlbuffer.md) instance the command assigns to an entry in the tile shader argument table for buffers.
- `offset`: An integer that represents the location, in bytes, from the start of `buffer` where the tile shader argument data begins. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `index`: An integer that represents the entry in the tile shader argument table for buffers that stores a record of `buffer` and `offset`.

## See Also

- [func setTileBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/settilebuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the tile shader argument table.
- [func setTileBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/settilebytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.
- [func setTileBufferOffset(Int, index: Int)](mtlrendercommandencoder/settilebufferoffset(_:index:).md)
  Updates an entry in the tile shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilebuffer(_:offset:index:))*