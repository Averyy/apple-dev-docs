# MTLIOCompressionMethod

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

The compression codecs that Metal supports for input/output handles.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum MTLIOCompressionMethod
```

```c
enum MTLIOCompressionMethod : NSInteger;
```

#### Overview

For more information on the individual codecs, see the [`Algorithm`](../Compression/algorithm.md) enumeration in the [Compression](../Compression/Compression.md) framework.

## Topics

### Compression codecs
- [MTLIOCompressionMethod.zlib](./mtliocompressionmethod/zlib.md)
  Indicates that a file uses the zlib compression algorithm codec.
- [MTLIOCompressionMethod.lzfse](./mtliocompressionmethod/lzfse.md)
  Indicates that a file uses the LZFSE compression algorithm codec.
- [MTLIOCompressionMethod.lz4](./mtliocompressionmethod/lz4.md)
  Indicates that a file uses the LZ4 compression algorithm codec.
- [MTLIOCompressionMethod.lzma](./mtliocompressionmethod/lzma.md)
  Indicates that a file uses the LZMA compression algorithm codec.
- [MTLIOCompressionMethod.lzBitmap](./mtliocompressionmethod/lzbitmap.md)
  Indicates that a file uses the LZBitmap compression algorithm codec.
### Initializers
- [init?(rawValue: Int)](./mtliocompressionmethod/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Asset compression
- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](./mtliocreatecompressioncontext%28_,_,_%29.md)
  Creates a compression context that you use to compress data into a single file.
- [func MTLIOCompressionContextDefaultChunkSize() -> Int](./mtliocompressioncontextdefaultchunksize%28%29.md)
  Returns a compression chunk size you can use as a default for creating a compression context.
- [typealias MTLIOCompressionContext](./mtliocompressioncontext.md)
  A pointer that represents the state of a file compression session in progress.
- [func MTLIOCompressionContextAppendData(MTLIOCompressionContext, UnsafeRawPointer, Int)](./mtliocompressioncontextappenddata%28_,_,_%29.md)
  Adds data to a compression context.
- [func MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext) -> MTLIOCompressionStatus](./mtlioflushanddestroycompressioncontext%28_%29.md)
  Finishes compressing and saves the file that a compression context represents.
- [enum MTLIOCompressionStatus](./mtliocompressionstatus.md)
  Represents the final state of a compression context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocompressionmethod)*