# MTLIOCompressionMethod

**Framework**: Metal  
**Kind**: enum

The compression codecs that Metal supports for input/output handles.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum MTLIOCompressionMethod
```

#### Overview

For more information on the individual codecs, see the [`Algorithm`](https://developer.apple.com/documentation/Compression/Algorithm) enumeration in the [`Compression`](https://developer.apple.com/documentation/Compression) framework.

## Topics

### Compression codecs
- [MTLIOCompressionMethod.zlib](mtliocompressionmethod/zlib.md)
  Indicates that a file uses the zlib compression algorithm codec.
- [MTLIOCompressionMethod.lzfse](mtliocompressionmethod/lzfse.md)
  Indicates that a file uses the LZFSE compression algorithm codec.
- [MTLIOCompressionMethod.lz4](mtliocompressionmethod/lz4.md)
  Indicates that a file uses the LZ4 compression algorithm codec.
- [MTLIOCompressionMethod.lzma](mtliocompressionmethod/lzma.md)
  Indicates that a file uses the LZMA compression algorithm codec.
- [MTLIOCompressionMethod.lzBitmap](mtliocompressionmethod/lzbitmap.md)
  Indicates that a file uses the LZBitmap compression algorithm codec.
### Initializers
- [init?(rawValue: Int)](mtliocompressionmethod/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func MTLIOCreateCompressionContext(String, MTLIOCompressionMethod, Int) -> MTLIOCompressionContext?](mtliocreatecompressioncontext(_:_:_:).md)
  Creates a compression context that you use to compress data into a single file.
- [func MTLIOCompressionContextDefaultChunkSize() -> Int](mtliocompressioncontextdefaultchunksize().md)
  Returns a compression chunk size you can use as a default for creating a compression context.
- [typealias MTLIOCompressionContext](mtliocompressioncontext.md)
  A pointer that represents the state of a file compression session in progress.
- [func MTLIOCompressionContextAppendData(MTLIOCompressionContext, UnsafeRawPointer, Int)](mtliocompressioncontextappenddata(_:_:_:).md)
  Adds data to a compression context.
- [func MTLIOFlushAndDestroyCompressionContext(MTLIOCompressionContext) -> MTLIOCompressionStatus](mtlioflushanddestroycompressioncontext(_:).md)
  Finishes compressing and saves the file that a compression context represents.
- [enum MTLIOCompressionStatus](mtliocompressionstatus.md)
  Represents the final state of a compression context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocompressionmethod)*