# COMPRESSION_LZMA

**Framework**: Compression  
**Kind**: var

The LZMA compression algorithm, which is recommended for high-compression ratio.

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
var COMPRESSION_LZMA: compression_algorithm { get }
```

#### Discussion

LZMA is a high-ratio compression algorithm that combines an LZ77 match finder with range coding driven by a Markov-chain context model. It typically achieves significantly higher compression ratios than [`COMPRESSION_ZLIB`](compression_zlib.md) or [`COMPRESSION_LZFSE`](compression_lzfse.md), at the cost of being roughly an order of magnitude slower than the other Compression library algorithms for both encoding and decoding. Use LZMA when output size is the dominant concern, for example, when bandwidth or storage is far more expensive than CPU time, or when the payload is compressed once and decompressed many times.

The Compression library implements the LZMA encoder at level 6 only. This is the default compression level for open-source LZMA and provides excellent compression. The decoder accepts data compressed at any level, so you can interoperate with files produced by other LZMA implementations regardless of the level they used.

The Compression library only supports LZMA2 embedded in the XZ container. Encoded buffers and streams produced by the Compression library are valid `.xz` payloads and standard `xz` tooling on other platforms can typically decoded these payloads. It’s recommended that you use:

- ZMA when you need cross-platform decompression and are able to trade LZMA’s speed for its higher ratio. *`COMPRESSION_ZLIB``if speed matters more than ratio for cross-platform interoperability.
- For Apple-only payloads, prefer [`COMPRESSION_LZRAVEN`](compression_lzraven.md) — it often matches or exceeds LZMA’s compression ratio, encodes a bit faster, and decodes 3x faster on Apple silicon.

LZMA is supported by both the buffer API — [`compression_encode_buffer(_:_:_:_:_:_:)`](compression_encode_buffer(_:_:_:_:_:_:).md) and [`compression_decode_buffer(_:_:_:_:_:_:)`](compression_decode_buffer(_:_:_:_:_:_:).md) — and the streaming API via [`compression_stream_init(_:_:_:)`](compression_stream_init(_:_:_:).md), so you can use it for in-memory payloads or for processing data incrementally as it arrives.

## See Also

- [var COMPRESSION_LZFSE: compression_algorithm](compression_lzfse.md)
  The LZFSE compression algorithm, which is recommended for use on Apple platforms.
- [var COMPRESSION_LZ4: compression_algorithm](compression_lz4.md)
  The LZ4 compression algorithm for fast compression.
- [var COMPRESSION_LZ4_RAW: compression_algorithm](compression_lz4_raw.md)
  The LZ4 compression algorithm, without frame headers.
- [var COMPRESSION_ZLIB: compression_algorithm](compression_zlib.md)
  The zlib compression algorithm, which is recommended for cross-platform compression.
- [var COMPRESSION_BROTLI: compression_algorithm](compression_brotli.md)
  The Brotli compression algorithm, which is recommended for text compression.
- [var COMPRESSION_LZBITMAP: compression_algorithm](compression_lzbitmap.md)
  The LZBITMAP compression algorithm, which is designed to exploit the vector instruction set of current CPUs.
- [var COMPRESSION_LZMESH: compression_algorithm](compression_lzmesh.md)
  The LZMESH compression algorithm, which is recommended for fast, general-purpose compression on Apple platforms.
- [var COMPRESSION_LZRAVEN: compression_algorithm](compression_lzraven.md)
  The LZRAVEN compression algorithm, which is recommended for high-compression ratio with fast decoding on Apple platforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/compression_lzma)*