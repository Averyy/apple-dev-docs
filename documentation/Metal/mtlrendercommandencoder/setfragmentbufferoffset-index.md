# setFragmentBufferOffset(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setFragmentBufferOffset(_ offset: Int, index: Int)
```

#### Discussion

The command this method encodes changes the offset for a fragment buffer that already has a previous assignment from one of your earlier commands.

For more information, see:

- [`setFragmentBuffer(_:offset:index:)`](mtlrendercommandencoder/setfragmentbuffer(_:offset:index:).md)
- [`setFragmentBuffers(_:offsets:range:)`](mtlrendercommandencoder/setfragmentbuffers(_:offsets:range:).md) (Swift)
- [`setFragmentBuffers:offsets:withRange:`](mtlrendercommandencoder/setfragmentbuffers:offsets:withrange:.md) (Objective-C)

The command can also adjust the offset for an entry that you previously set with the [`setFragmentBytes(_:length:index:)`](mtlrendercommandencoder/setfragmentbytes(_:length:index:).md) method.

> 💡 **Tip**:  If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

By default, the buffer at each index is `nil`.

## Parameters

- `offset`: See the   to check for offset alignment requirements for buffers in   and   address space.
- `index`: An integer that represents the entry in the fragment shader argument table for buffers that already stores a record of an  .

## See Also

- [func setFragmentBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setfragmentbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the fragment shader argument table.
- [func setFragmentBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setfragmentbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the fragment shader argument table.
- [func setFragmentBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setfragmentbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentbufferoffset(_:index:))*