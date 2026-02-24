# setObjectBuffers(_:offsets:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple buffers to a range of entries in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+

## Declaration

```swift
func setObjectBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

#### Discussion

By default, the texture at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setObjectBuffers:offsets:withRange:`](mtlrendercommandencoder/setobjectbuffers:offsets:withrange:.md).

## Parameters

- `buffers`: An array of [`MTLBuffer`](mtlbuffer.md) instances the command assigns to entries in the object shader argument table for buffers.
- `offsets`: An array of integers. Each element represents the location, in bytes, from the start of the corresponding [`MTLBuffer`](mtlbuffer.md) element in `buffers` where the object shader argument data begins. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `range`: A span of integers that represent the entries in the object shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## See Also

- [func setObjectBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setobjectbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the object shader argument table.
- [func setObjectBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setobjectbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the object shader argument table.
- [func setObjectBufferOffset(Int, index: Int)](mtlrendercommandencoder/setobjectbufferoffset(_:index:).md)
  Updates an entry in the object shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectbuffers(_:offsets:range:))*