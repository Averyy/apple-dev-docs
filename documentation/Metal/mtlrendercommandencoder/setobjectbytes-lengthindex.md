# setObjectBytes(_:length:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a buffer from bytes and assigns it to an entry in the object shader argument table.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func setObjectBytes(_ bytes: UnsafeRawPointer, length: Int, index: Int)
```

#### Discussion

The method is equivalent to creating an [`MTLBuffer`](mtlbuffer.md) instance that contains the same data as `bytes` and calling the [`setObjectBufferOffset(_:index:)`](mtlrendercommandencoder/setobjectbufferoffset(_:index:).md) method. However, this method avoids the overhead of creating a buffer to store your data; instead, Metal manages the data.

> ❗ **Important**:  Only call this method for single-use data that’s smaller than 4 KB.

For data that’s more than 4 KB, create an [`MTLBuffer`](mtlbuffer.md) instance and pass it to [`setObjectBuffer(_:offset:index:)`](mtlrendercommandencoder/setobjectbuffer(_:offset:index:).md).

## Parameters

- `bytes`: A pointer to argument data the method copies to an   and assigns to an entry in the object shader argument table for buffers.
- `length`: The number of bytes the method copies from the   pointer.
- `index`: An integer that represents the entry in the object shader argument table for buffers that stores a record of the   the method creates from  .

## See Also

- [func setObjectBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setobjectbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the object shader argument table.
- [func setObjectBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setobjectbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the object shader argument table.
- [func setObjectBufferOffset(Int, index: Int)](mtlrendercommandencoder/setobjectbufferoffset(_:index:).md)
  Updates an entry in the object shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectbytes(_:length:index:))*