# setFragmentBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Assigns a buffer to an entry in the fragment shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setFragmentBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Mentions

- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)

#### Discussion

By default, the buffer at each index is `nil`.

## Parameters

- `buffer`: An   instance the command assigns to an entry in the fragment shader argument table for buffers.
- `offset`: See the   to check for offset alignment requirements for buffers in   and   address space.
- `index`: An integer that represents the entry in the fragment shader argument table for buffers that stores a record of   and  .

## See Also

- [func setFragmentBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setfragmentbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the fragment shader argument table.
- [func setFragmentBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setfragmentbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.
- [func setFragmentBufferOffset(Int, index: Int)](mtlrendercommandencoder/setfragmentbufferoffset(_:index:).md)
  Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentbuffer(_:offset:index:))*