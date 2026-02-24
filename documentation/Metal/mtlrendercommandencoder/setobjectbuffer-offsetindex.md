# setObjectBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a buffer to an entry in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setObjectBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Mentions

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)

#### Discussion

By default, the texture at each index is `nil`.

## Parameters

- `buffer`: An [`MTLBuffer`](mtlbuffer.md) instance the command assigns to an entry in the object shader argument table for buffers.
- `offset`: An integer that represents the location, in bytes, from the start of `buffer` where the object shader argument data begins. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `index`: An integer that represents the entry in the object shader argument table for buffers that stores a record of `buffer` and `offset`.

## See Also

- [func setObjectBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setobjectbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the object shader argument table.
- [func setObjectBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setobjectbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the object shader argument table.
- [func setObjectBufferOffset(Int, index: Int)](mtlrendercommandencoder/setobjectbufferoffset(_:index:).md)
  Updates an entry in the object shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectbuffer(_:offset:index:))*