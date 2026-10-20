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

LZBITMAP is the Apple compression algorithm designed around the SIMD vector instruction set found on modern CPUs. Its encoding scheme arranges literal and match data so that both encoder and decoder hot loops can advance multiple symbols per vector operation, which delivers substantially higher throughput than scalar LZ-family codecs at comparable compression ratios.

LZBITMAP sits between [`COMPRESSION_LZ4`](compression_lz4.md) and [`COMPRESSION_LZMESH`](compression_lzmesh.md) in the speed-ratio tradeoff. It achieves compression ratios close to [`COMPRESSION_ZLIB`](compression_zlib.md) at a lower compression cost. When compression ratio and performance are equally important, prefer [`COMPRESSION_LZMESH`](compression_lzmesh.md) to favor ratio and LZBITMAP to favor decoder performance. If raw encoder speed matters more than ratio, use [`COMPRESSION_LZ4`](compression_lz4.md) instead.

LZBITMAP is available only on Apple devices, so don’t use it for payloads that need to be decoded on non-Apple platforms. For cross-platform interoperability, use [`COMPRESSION_ZLIB`](compression_zlib.md) or [`COMPRESSION_LZ4`](compression_lz4.md) instead.

LZBITMAP is available through the buffer API only — [`compression_encode_buffer(_:_:_:_:_:_:)`](compression_encode_buffer(_:_:_:_:_:_:).md) and [`compression_decode_buffer(_:_:_:_:_:_:)`](compression_decode_buffer(_:_:_:_:_:_:).md).

> ❗ **Important**:  The Compression stream API doesn’t support the LZBITMAP compression algorithm. Use [`COMPRESSION_LZFSE`](compression_lzfse.md) or [`COMPRESSION_ZLIB`](compression_zlib.md) if you need streaming behavior, such as compressing data as it arrives over the network or processing files larger than available memory.

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
- [var COMPRESSION_LZMESH: compression_algorithm](compression_lzmesh.md)
  The LZMESH compression algorithm, which is recommended for fast, general-purpose compression on Apple platforms.
- [var COMPRESSION_LZRAVEN: compression_algorithm](compression_lzraven.md)
  The LZRAVEN compression algorithm, which is recommended for high-compression ratio with fast decoding on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_lzbitmap)*