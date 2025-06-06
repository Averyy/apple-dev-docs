# COMPRESSION_LZBITMAP

**Framework**: Compression  
**Kind**: var

The LZBITMAP compression algorithm, which is designed to exploit the vector instruction set of current CPUs.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var COMPRESSION_LZBITMAP: compression_algorithm { get }
```

#### Discussion

The LZBITMAP compression algorithm provides compression ratios as close as possible to [`COMPRESSION_ZLIB`](compression_zlib.md) and [`COMPRESSION_LZFSE`](compression_lzfse.md), with a lower compression cost. This compression algorithm is available only for the Compression buffer API functions, [`compression_encode_buffer(_:_:_:_:_:_:)`](compression_encode_buffer(_:_:_:_:_:_:).md) and [`compression_decode_buffer(_:_:_:_:_:_:)`](compression_decode_buffer(_:_:_:_:_:_:).md).

[`COMPRESSION_LZBITMAP`](compression_lzbitmap.md) is available only on Apple devices.

## See Also

- [var COMPRESSION_LZFSE: compression_algorithm](compression_lzfse.md)
  The LZFSE compression algorithm, which is recommended for use on Apple platforms.
- [var COMPRESSION_LZ4: compression_algorithm](compression_lz4.md)
  The LZ4 compression algorithm for fast compression.
- [var COMPRESSION_LZ4_RAW: compression_algorithm](compression_lz4_raw.md)
  The LZ4 compression algorithm, without frame headers.
- [var COMPRESSION_LZMA: compression_algorithm](compression_lzma.md)
  The LZMA compression algorithm, which is recommended for high-compression ratio.
- [var COMPRESSION_ZLIB: compression_algorithm](compression_zlib.md)
  The zlib compression algorithm, which is recommended for cross-platform compression.
- [var COMPRESSION_BROTLI: compression_algorithm](compression_brotli.md)
  The Brotli compression algorithm, which is recommended for text compression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_lzbitmap)*