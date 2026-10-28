# setTileBufferOffset(_:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setTileBufferOffset:(NSUInteger) offset atIndex:(NSUInteger) index;
```

## Discussion

The command this method encodes changes the offset for a fragment buffer that already has a previous assignment from one of your earlier commands.

For more information, see:

- [`setTileBuffer(_:offset:index:)`](./settilebuffer%28_,offset,index%29.md)
- [`setTileBuffers(_:offsets:range:)`](./settilebuffers%28_,offsets,range%29.md) (Swift)
- [`setTileBuffers:offsets:withRange:`](./settilebuffers_offsets_withrange_.md) (Objective-C)

The command can also adjust the offset for an entry that you previously set with the [`setTileBytes(_:length:index:)`](./settilebytes%28_,length,index%29.md) method.

> 💡 **Tip**:  If you’re only updating an offset, this method is typically more efficient than rebinding a buffer or byte block with the methods above.

By default, the buffer at each index is `nil`.

## Parameters

- `offset`: An integer that represents the location, in bytes, from the start of `buffer` where the tile shader argument data begins.

  See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `index`: An integer that represents the entry in the tile shader argument table for buffers that already stores a record of an [`MTLBuffer`](../mtlbuffer.md).

## See Also

### Assigning buffers
- [func setTileBuffer((any MTLBuffer)?, offset: Int, index: Int)](./settilebuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the tile shader argument table.
- [func setTileBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./settilebuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the tile shader argument table.
- [func setTileBytes(UnsafeRawPointer, length: Int, index: Int)](./settilebytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.
- [- setTileBuffers:offsets:withRange:](./settilebuffers_offsets_withrange_.md)
  Assigns multiple buffers to a range of entries in the tile shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settilebufferoffset(_:index:))*