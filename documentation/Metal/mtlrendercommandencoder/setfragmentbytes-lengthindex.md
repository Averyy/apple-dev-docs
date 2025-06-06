# setFragmentBytes(_:length:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setFragmentBytes(_ bytes: UnsafeRawPointer, length: Int, index: Int)
```

#### Discussion

The method is equivalent to creating an [`MTLBuffer`](mtlbuffer.md) instance that contains the same data as `bytes` and calling the [`setFragmentBuffer(_:offset:index:)`](mtlrendercommandencoder/setfragmentbuffer(_:offset:index:).md) method. However, this method avoids the overhead of creating a buffer to store your data; instead, Metal manages the data.

> ❗ **Important**:  Only call this method for single-use data that’s smaller than 4 KB.

 Only call this method for single-use data that’s smaller than 4 KB.

For data that’s more than 4 KB, create an [`MTLBuffer`](mtlbuffer.md) instance and pass it to [`setFragmentBuffer(_:offset:index:)`](mtlrendercommandencoder/setfragmentbuffer(_:offset:index:).md).

By default, the buffer at each index is `nil`.

## Parameters

- `bytes`: A pointer to argument data the method copies to an   and assigns to an entry in the fragment shader argument table for buffers.
- `length`: The number of bytes the method copies from the   pointer.
- `index`: An integer that represents the entry in the fragment shader argument table for buffers that stores a record of the   the method creates from  .

## See Also

- [func setFragmentBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setfragmentbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the fragment shader argument table.
- [func setFragmentBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setfragmentbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the fragment shader argument table.
- [func setFragmentBufferOffset(Int, index: Int)](mtlrendercommandencoder/setfragmentbufferoffset(_:index:).md)
  Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentbytes(_:length:index:))*