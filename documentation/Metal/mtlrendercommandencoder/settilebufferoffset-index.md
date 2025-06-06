# setTileBufferOffset(_:index:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Updates an entry in the tile shader argument table with a new location within the entry’s current buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
func setTileBufferOffset(_ offset: Int, index: Int)
```

#### Discussion

The command this method encodes changes the offset for a fragment buffer that already has a previous assignment from one of your earlier commands.

For more information, see:

- [`setTileBuffer(_:offset:index:)`](mtlrendercommandencoder/settilebuffer(_:offset:index:).md)
- [`setTileBuffers(_:offsets:range:)`](mtlrendercommandencoder/settilebuffers(_:offsets:range:).md) (Swift)
- [`setTileBuffers:offsets:withRange:`](mtlrendercommandencoder/settilebuffers:offsets:withrange:.md) (Objective-C)

The command can also adjust the offset for an entry that you previously set with the [`setTileBytes(_:length:index:)`](mtlrendercommandencoder/settilebytes(_:length:index:).md) method.

> 💡 **Tip**:  If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

 If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

By default, the buffer at each index is `nil`.

## Parameters

- `offset`: See the   to check for offset alignment requirements for buffers in   and   address space.
- `index`: An integer that represents the entry in the tile shader argument table for buffers that already stores a record of an  .

## See Also

- [func setTileBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/settilebuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the tile shader argument table.
- [func setTileBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/settilebuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the tile shader argument table.
- [func setTileBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/settilebytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilebufferoffset(_:index:))*