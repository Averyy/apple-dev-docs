# setObjectBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setObjectBuffer:(id<MTLBuffer>) buffer offset:(NSUInteger) offset atIndex:(NSUInteger) index;
```

## Mentions

- [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md)

#### Discussion

By default, the texture at each index is `nil`.

## Parameters

- `buffer`: An [`MTLBuffer`](../mtlbuffer.md) instance the command assigns to an entry in the object shader argument table for buffers.
- `offset`: An integer that represents the location, in bytes, from the start of `buffer` where the object shader argument data begins.

  See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `index`: An integer that represents the entry in the object shader argument table for buffers that stores a record of `buffer` and `offset`.

## See Also

### Assigning buffers for object shaders
- [func setObjectBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setobjectbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the object shader argument table.
- [func setObjectBytes(UnsafeRawPointer, length: Int, index: Int)](./setobjectbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the object shader argument table.
- [func setObjectBufferOffset(Int, index: Int)](./setobjectbufferoffset%28_,index%29.md)
  Updates an entry in the object shader argument table with a new location within the entry’s current buffer.
- [- setObjectBuffers:offsets:withRange:](./setobjectbuffers_offsets_withrange_.md)
  Encodes a command that assigns multiple buffers to a range of entries in the object shader argument table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setobjectbuffer(_:offset:index:))*