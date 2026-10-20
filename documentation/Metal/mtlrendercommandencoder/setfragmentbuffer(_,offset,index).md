# setFragmentBuffer(_:offset:index:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Assigns a buffer to an entry in the fragment shader argument table.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setFragmentBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

```objc
- (void) setFragmentBuffer:(id<MTLBuffer>) buffer offset:(NSUInteger) offset atIndex:(NSUInteger) index;
```

## Mentions

- [Improving CPU performance by using argument buffers](../improving-cpu-performance-by-using-argument-buffers.md)

#### Discussion

By default, the buffer at each index is `nil`.

## Parameters

- `buffer`: An [`MTLBuffer`](../mtlbuffer.md) instance the command assigns to an entry in the fragment shader argument table for buffers.
- `offset`: An integer that represents the location, in bytes, from the start of `buffer` where the fragment shader argument data begins.

  See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.
- `index`: An integer that represents the entry in the fragment shader argument table for buffers that stores a record of `buffer` and `offset`.

## See Also

### Assigning buffers
- [func setFragmentBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./setfragmentbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the fragment shader argument table.
- [func setFragmentBytes(UnsafeRawPointer, length: Int, index: Int)](./setfragmentbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.
- [func setFragmentBufferOffset(Int, index: Int)](./setfragmentbufferoffset%28_,index%29.md)
  Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentbuffer(_:offset:index:))*