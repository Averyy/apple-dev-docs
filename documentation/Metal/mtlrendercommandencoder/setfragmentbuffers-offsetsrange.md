# setFragmentBuffers(_:offsets:range:)

**Framework**: Metal  
**Kind**: method

Assigns multiple buffers to a range of entries in the fragment shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst ?+
- macOS 10.11+
- tvOS 8.0+
- visionOS ?+

## Declaration

```swift
func setFragmentBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

#### Discussion

By default, the buffer at each index is `nil`.

> **Note**:  The Objective-C version of this method is [`setFragmentBuffers:offsets:withRange:`](mtlrendercommandencoder/setfragmentbuffers:offsets:withrange:.md).

## Parameters

- `buffers`: An array of [`MTLBuffer`](mtlbuffer.md) instances the command assigns to entries in the fragment shader argument table for buffers.
- `offsets`: An array of integers. Each element represents the location, in bytes, from the start of the corresponding [`MTLBuffer`](mtlbuffer.md) element in `buffers` where the fragment shader argument data begins. See the [`Metal feature set tables (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `range`: A span of integers that represent the entries in the fragment shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## See Also

- [func setFragmentBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setfragmentbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the fragment shader argument table.
- [func setFragmentBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setfragmentbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.
- [func setFragmentBufferOffset(Int, index: Int)](mtlrendercommandencoder/setfragmentbufferoffset(_:index:).md)
  Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentbuffers(_:offsets:range:))*